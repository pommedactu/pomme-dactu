#!/usr/bin/env python3
"""
Script pour trouver les vraies questions Apple depuis Reddit
SANS API - utilise le scraping du JSON public de Reddit
"""

import json
import requests
import random
from datetime import datetime
import time


class RedditQuestionFinder:
    def __init__(self):
        # Subreddits Apple à surveiller
        self.subreddits = ['apple', 'AppleHelp', 'iphone', 'mac', 'ios', 'iPad']
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        self.already_covered = self.load_covered_questions()

    def load_covered_questions(self):
        """Charge les questions déjà traitées"""
        try:
            with open('covered_questions.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def fetch_reddit_posts(self, subreddit, sort='hot', limit=50):
        """Récupère les posts d'un subreddit via JSON public"""
        try:
            url = f'https://www.reddit.com/r/{subreddit}/{sort}.json?limit={limit}'
            response = requests.get(url, headers=self.headers, timeout=10)

            if response.status_code == 200:
                data = response.json()
                posts = []

                for child in data['data']['children']:
                    post = child['data']
                    posts.append({
                        'title': post['title'],
                        'score': post['score'],
                        'num_comments': post['num_comments'],
                        'url': f"https://reddit.com{post['permalink']}",
                        'subreddit': subreddit
                    })

                return posts
            else:
                print(f"    ⚠️  Erreur HTTP {response.status_code} pour r/{subreddit}")
                return []

        except Exception as e:
            print(f"    ⚠️  Erreur avec r/{subreddit}: {e}")
            return []

    def is_valid_question(self, title):
        """Vérifie si c'est une vraie question technique"""
        title_lower = title.lower()

        # 1. FILTRER LES QUESTIONS VAGUES
        # Mots qui rendent une question trop vague sans contexte
        vague_indicators = [
            'is this', 'is that', 'does this', 'does that',
            'what is this', 'what is that', 'anyone else',
            'anyone know', 'just me', 'normal?'
        ]

        # Rejeter si la question est vague
        if any(indicator in title_lower for indicator in vague_indicators):
            return False

        # 2. LONGUEUR MINIMALE
        # Les bonnes questions techniques sont généralement détaillées
        if len(title) < 30:  # Moins de 30 caractères = trop court
            return False

        # 3. MOTS-CLÉS TECHNIQUES REQUIS
        # Au moins un produit Apple doit être mentionné
        apple_products = [
            'iphone', 'ipad', 'mac', 'macbook', 'imac', 'airpods',
            'apple watch', 'watch', 'apple tv', 'airtag', 'ios', 'macos'
        ]

        has_apple_product = any(product in title_lower for product in apple_products)
        if not has_apple_product:
            return False

        # 4. MOTS-CLÉS INDIQUANT UN PROBLÈME TECHNIQUE
        problem_keywords = [
            'problème', 'problem', 'bug', 'erreur', 'error', 'crash',
            'ne fonctionne pas', 'not working', "doesn't work", "won't",
            'how to', 'how do i', 'how can', 'pourquoi', 'why',
            "can't", 'unable', 'help', 'issue', 'broken', 'fix',
            'overheating', 'heating', 'chauffe', 'slow', 'lent',
            'battery', 'batterie', 'charging', 'charge',
            'freeze', 'frozen', 'stuck', 'bloqué', 'lag', 'lagging'
        ]

        # 5. EXCLURE LES POSTS NON-TECHNIQUES
        exclude_keywords = [
            'rumeur', 'rumor', 'leak', 'achat', 'buy', 'acheter',
            'should i buy', 'dois-je', 'worth', 'vaut-il', 'price',
            'deal', 'sale', 'promo', ' vs ', ' or ', 'which one', 'better',
            'upgrade', 'mise à jour', 'new release', 'announcement',
            'foldable', 'pliable', 'expected', 'smaller', 'larger',
            'may be', 'could be', 'might', 'future', 'coming',
            'release date', 'sortie', 'prediction', 'expect',
            'could launch', 'could still', 'next year', 'will be',
            'rumored', 'reportedly', 'selon', 'according', 'sources say'
        ]

        # Vérifier exclusions
        if any(word in title_lower for word in exclude_keywords):
            return False

        # Vérifier présence de mots-clés problème
        if any(word in title_lower for word in problem_keywords):
            return True

        return False

    def categorize_question(self, question):
        """Détermine la catégorie Apple"""
        q_lower = question.lower()

        if 'iphone' in q_lower or 'ios' in q_lower:
            return 'iPhone'
        elif 'mac' in q_lower or 'macbook' in q_lower or 'macos' in q_lower or 'imac' in q_lower:
            return 'Mac'
        elif 'ipad' in q_lower or 'ipados' in q_lower:
            return 'iPad'
        elif 'airpod' in q_lower:
            return 'AirPods'
        elif 'watch' in q_lower:
            return 'Apple Watch'
        elif 'apple tv' in q_lower or 'appletv' in q_lower:
            return 'Apple TV'
        elif 'airtag' in q_lower:
            return 'AirTag'
        else:
            return 'Apple'

    def extract_keywords(self, question):
        """Extrait les mots-clés de la question"""
        # Mots vides à retirer
        stop_words = {
            'the', 'a', 'an', 'is', 'are', 'was', 'were', 'le', 'la', 'les',
            'un', 'une', 'des', 'de', 'mon', 'ma', 'mes', 'my', 'your',
            'ne', 'pas', 'plus', 'not', 'no', 'qui', 'que', 'what', 'how'
        }

        words = question.lower().replace('?', '').replace('!', '').split()
        keywords = [w for w in words if len(w) > 3 and w not in stop_words]

        return keywords[:5]  # Max 5 mots-clés

    def find_best_question(self):
        """Trouve LA meilleure question du jour depuis Reddit"""
        print("🔍 Recherche des vraies questions Apple sur Reddit...\n")

        all_questions = []

        # Parcourir les subreddits
        for subreddit in self.subreddits:
            print(f"  📱 Analyse de r/{subreddit}...")
            posts = self.fetch_reddit_posts(subreddit)

            for post in posts:
                if self.is_valid_question(post['title']):
                    # Calculer un score de pertinence
                    base_score = (post['score'] * 2) + (post['num_comments'] * 3)

                    # BONUS : Favoriser les problèmes techniques clairs
                    title_lower = post['title'].lower()
                    bonus = 0

                    # +500 si commence par un mot-clé problème fort
                    strong_problem_starts = ['my ', 'iphone ', 'mac ', 'macbook ', 'ipad ', 'airpods ']
                    if any(title_lower.startswith(start) for start in strong_problem_starts):
                        bonus += 500

                    # +300 si contient des mots-clés de problème urgent
                    urgent_keywords = ['not working', 'won\'t', 'can\'t', 'broken', 'error', 'crash', 'overheating']
                    if any(keyword in title_lower for keyword in urgent_keywords):
                        bonus += 300

                    # +200 pour les questions "how to fix"
                    if 'how to fix' in title_lower or 'how do i fix' in title_lower:
                        bonus += 200

                    relevance_score = base_score + bonus

                    all_questions.append({
                        'title': post['title'],
                        'score': relevance_score,
                        'upvotes': post['score'],
                        'comments': post['num_comments'],
                        'subreddit': subreddit,
                        'url': post['url']
                    })

            # Pause pour être poli avec Reddit
            time.sleep(1)

        if not all_questions:
            print("\n❌ Aucune question trouvée sur Reddit")
            print("💡 Réessaye avec les questions pré-définies")
            return None

        print(f"\n✅ {len(all_questions)} questions trouvées sur Reddit\n")

        # Trier par score
        all_questions.sort(key=lambda x: x['score'], reverse=True)

        # Filtrer les questions déjà traitées
        covered_titles = [q.get('question', '') for q in self.already_covered]
        new_questions = [q for q in all_questions if q['title'] not in covered_titles]

        if not new_questions:
            print("⚠️  Toutes les questions Reddit ont déjà été traitées")
            print("💡 Réinitialise covered_questions.json ou réessaye demain")
            return None

        # Meilleure question
        best = new_questions[0]

        print(f"🎯 MEILLEURE QUESTION (vraie recherche Reddit) :")
        print(f"   Titre: {best['title']}")
        print(f"   Source: r/{best['subreddit']}")
        print(f"   Engagement: {best['upvotes']} upvotes, {best['comments']} commentaires")
        print(f"   Score: {best['score']}")
        print(f"   Catégorie: {self.categorize_question(best['title'])}")

        return {
            'title': best['title'],
            'category': self.categorize_question(best['title']),
            'keywords': self.extract_keywords(best['title']),
            'source': f"Reddit r/{best['subreddit']}",
            'engagement': {
                'upvotes': best['upvotes'],
                'comments': best['comments']
            }
        }

    def generate_article_prompt(self, question):
        """Génère le prompt pour Claude"""
        prompt = f"""Tu es un expert Apple qui écrit pour "Pomme d'Actu", un blog spécialisé.

QUESTION À TRAITER (vraie question Reddit d'un utilisateur réel):
{question['title']}

SOURCE: {question['source']}
CATÉGORIE: {question['category']}
ENGAGEMENT: {question['engagement']['upvotes']} upvotes, {question['engagement']['comments']} commentaires

MISSION:
Écris un article de blog complet (800-1200 mots) qui résout ce problème de manière claire et actionnable.

STRUCTURE ATTENDUE:
1. Introduction (2-3 phrases)
   - Reformule le problème
   - Rassure le lecteur (c'est un problème courant)

2. Solution principale (étapes numérotées)
   - Explications claires, pas à pas
   - Chaque étape doit être actionnable

3. Pourquoi ça marche (1 paragraphe)
   - Explication technique vulgarisée

4. Solutions alternatives (si la première ne marche pas)
   - 2-3 alternatives

5. Conclusion
   - Résumé rapide
   - Encouragement

CONTRAINTES:
- Ton professionnel mais accessible
- Pas de jargon technique sans explication
- Phrases courtes et claires
- Exemples concrets
- Public cible: utilisateur Apple moyennement technique

FORMAT DE SORTIE:
Retourne UNIQUEMENT un JSON avec cette structure:
{{
  "title": "Titre SEO-optimisé (60 caractères max)",
  "excerpt": "Résumé en 1-2 phrases (150 caractères max)",
  "content": "Le contenu complet en HTML (utilise <h2>, <h3>, <p>, <ol>, <ul>, <strong>)",
  "keywords": {question['keywords']}
}}

Important: Le contenu HTML doit être bien structuré avec des titres <h2> pour les sections principales."""

        return prompt


def main():
    print("🍎 POMME D'ACTU - Questions Reddit (vraies recherches)")
    print("=" * 60)
    print()

    finder = RedditQuestionFinder()

    # Trouver une question
    question = finder.find_best_question()

    if question:
        # Générer le prompt pour Claude
        prompt = finder.generate_article_prompt(question)

        # Sauvegarder pour utilisation
        output = {
            'date': datetime.now().isoformat(),
            'question': question,
            'prompt': prompt
        }

        with open('daily_question.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        print(f"\n✅ Question sauvegardée dans daily_question.json")
        print(f"\n📋 PROCHAINE ÉTAPE:")
        print(f"   1. Ouvre daily_question.json")
        print(f"   2. Copie le 'prompt'")
        print(f"   3. Colle-le dans Claude")
        print(f"   4. Lance: python3 publish_article.py")


if __name__ == "__main__":
    main()
