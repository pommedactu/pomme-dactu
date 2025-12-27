#!/usr/bin/env python3
"""
Script pour trouver LA meilleure question Apple du jour
Sources: Reddit (r/apple, r/AppleHelp, r/iphone, r/mac)
"""

import json
import os
from datetime import datetime
from collections import Counter
import re

# Note: Ce script utilise l'API Reddit gratuite via PRAW
# Installation: pip install praw

try:
    import praw
except ImportError:
    print("❌ Erreur: Installez praw avec: pip install praw")
    exit(1)


class AppleQuestionFinder:
    def __init__(self):
        # Configuration Reddit (gratuit, pas besoin de compte premium)
        # Tu devras créer une app Reddit sur: https://www.reddit.com/prefs/apps
        self.reddit = praw.Reddit(
            client_id="YOUR_CLIENT_ID",  # À remplacer
            client_secret="YOUR_CLIENT_SECRET",  # À remplacer
            user_agent="PommeDactu/1.0"
        )

        self.subreddits = ['apple', 'AppleHelp', 'iphone', 'mac', 'ios', 'macOS']
        self.already_covered = self.load_covered_questions()

    def load_covered_questions(self):
        """Charge les questions déjà traitées"""
        try:
            with open('covered_questions.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_covered_question(self, question):
        """Sauvegarde la question traitée"""
        self.already_covered.append({
            'question': question,
            'date': datetime.now().isoformat()
        })
        with open('covered_questions.json', 'w') as f:
            json.dump(self.already_covered, f, indent=2)

    def is_valid_question(self, title):
        """Vérifie si c'est une vraie question technique"""
        # Mots-clés indiquant un problème technique
        problem_keywords = [
            'problème', 'problem', 'bug', 'erreur', 'error', 'crash',
            'ne fonctionne pas', 'not working', 'doesn\'t work',
            'comment', 'how to', 'pourquoi', 'why',
            'impossible', 'can\'t', 'unable'
        ]

        # Exclure les posts non-techniques
        exclude_keywords = [
            'rumeur', 'rumor', 'leak', 'achat', 'buy', 'acheter',
            'should i', 'dois-je', 'worth', 'vaut-il'
        ]

        title_lower = title.lower()

        # Vérifier exclusions
        if any(word in title_lower for word in exclude_keywords):
            return False

        # Vérifier présence de mots-clés problème
        if any(word in title_lower for word in problem_keywords):
            return True

        # Vérifier si c'est une question (point d'interrogation)
        if '?' in title:
            return True

        return False

    def extract_keywords(self, title):
        """Extrait les mots-clés principaux"""
        # Nettoyer et extraire
        words = re.findall(r'\b\w+\b', title.lower())
        # Retirer mots communs
        stop_words = {'the', 'a', 'an', 'is', 'are', 'was', 'were', 'le', 'la', 'les', 'un', 'une', 'des'}
        keywords = [w for w in words if w not in stop_words and len(w) > 3]
        return keywords

    def find_best_question(self):
        """Trouve LA meilleure question du jour"""
        questions = []

        print("🔍 Recherche des questions Apple du jour...\n")

        for subreddit_name in self.subreddits:
            try:
                subreddit = self.reddit.subreddit(subreddit_name)
                # Récupérer les posts "hot" des dernières 24h
                for post in subreddit.hot(limit=50):
                    if self.is_valid_question(post.title):
                        # Calculer un score de pertinence
                        score = (
                            post.score * 2 +  # Upvotes comptent double
                            post.num_comments * 3  # Commentaires = engagement
                        )

                        questions.append({
                            'title': post.title,
                            'score': score,
                            'url': post.url,
                            'subreddit': subreddit_name,
                            'upvotes': post.score,
                            'comments': post.num_comments
                        })

                print(f"  ✓ r/{subreddit_name}: {len([q for q in questions if q['subreddit'] == subreddit_name])} questions trouvées")
            except Exception as e:
                print(f"  ⚠️  Erreur avec r/{subreddit_name}: {e}")

        if not questions:
            print("\n❌ Aucune question trouvée aujourd'hui")
            return None

        # Trier par score
        questions.sort(key=lambda x: x['score'], reverse=True)

        # Filtrer les questions déjà couvertes
        covered_titles = [q['question'] for q in self.already_covered]
        new_questions = [q for q in questions if q['title'] not in covered_titles]

        if not new_questions:
            print("\n⚠️  Toutes les questions populaires ont déjà été traitées")
            print("💡 Conseil: Réinitialiser covered_questions.json ou attendre de nouvelles questions")
            return None

        # La meilleure question
        best = new_questions[0]

        print(f"\n🎯 MEILLEURE QUESTION DU JOUR:")
        print(f"   Titre: {best['title']}")
        print(f"   Source: r/{best['subreddit']}")
        print(f"   Engagement: {best['upvotes']} upvotes, {best['comments']} commentaires")
        print(f"   Score: {best['score']}")

        return best

    def generate_article_prompt(self, question):
        """Génère le prompt pour Claude"""
        prompt = f"""Tu es un expert Apple qui écrit pour "Pomme d'Actu", un blog spécialisé.

QUESTION À TRAITER:
{question['title']}

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
  "keywords": ["mot-clé1", "mot-clé2", "mot-clé3"]
}}

Important: Le contenu HTML doit être bien structuré avec des titres <h2> pour les sections principales."""

        return prompt


def main():
    finder = AppleQuestionFinder()

    # Vérifier si les credentials Reddit sont configurés
    if "YOUR_CLIENT_ID" in str(finder.reddit.config.client_id):
        print("⚠️  CONFIGURATION NÉCESSAIRE:")
        print("1. Va sur https://www.reddit.com/prefs/apps")
        print("2. Clique 'create another app'")
        print("3. Choisis 'script', donne un nom")
        print("4. Copie le client_id et client_secret dans find_question.py")
        print("\n💡 C'est gratuit et prend 2 minutes!")
        return

    # Trouver la meilleure question
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
        print(f"   4. Lance: python publish_article.py")


if __name__ == "__main__":
    main()
