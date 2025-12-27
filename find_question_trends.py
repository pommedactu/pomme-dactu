#!/usr/bin/env python3
"""
Script pour trouver les questions Apple tendances via Google Trends
Utilise les vraies recherches des utilisateurs
"""

import json
import random
from datetime import datetime
from pytrends.request import TrendReq
import time


class TrendsQuestionFinder:
    def __init__(self):
        # Initialiser pytrends
        self.pytrends = TrendReq(hl='fr-FR', tz=60)

        # Mots-clés Apple à surveiller
        self.apple_keywords = [
            'iPhone problème',
            'Mac lent',
            'iPad bug',
            'AirPods déconnexion',
            'Apple Watch erreur',
            'iOS problème',
            'macOS problème',
            'iPhone ne charge pas',
            'Mac qui chauffe',
            'Face ID ne marche pas'
        ]

        self.already_covered = self.load_covered_questions()

    def load_covered_questions(self):
        """Charge les questions déjà traitées"""
        try:
            with open('covered_questions.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def get_related_queries(self, keyword):
        """Récupère les questions liées depuis Google Trends"""
        try:
            print(f"  🔍 Recherche pour : {keyword}")

            # Construire la payload pour Google Trends
            self.pytrends.build_payload([keyword], timeframe='now 7-d', geo='FR')

            # Récupérer les requêtes associées
            related = self.pytrends.related_queries()

            questions = []

            # Extraire les top queries
            if keyword in related and related[keyword]['top'] is not None:
                top_queries = related[keyword]['top']
                for _, row in top_queries.iterrows():
                    query = row['query']
                    # Filtrer pour garder uniquement les questions
                    if self.is_valid_question(query):
                        questions.append(query)

            # Extraire les rising queries (tendances montantes)
            if keyword in related and related[keyword]['rising'] is not None:
                rising_queries = related[keyword]['rising']
                for _, row in rising_queries.iterrows():
                    query = row['query']
                    if self.is_valid_question(query):
                        questions.append(query)

            return questions

        except Exception as e:
            print(f"    ⚠️  Erreur: {e}")
            return []

    def is_valid_question(self, query):
        """Vérifie si c'est une question technique pertinente"""
        query_lower = query.lower()

        # Mots-clés de problèmes techniques
        problem_keywords = [
            'problème', 'bug', 'erreur', 'ne marche pas', 'ne fonctionne pas',
            'comment', 'pourquoi', 'bloqué', 'lent', 'chauffe', 'crash',
            'ne charge pas', 'déconnecte', 'impossible', 'pas de', 'plus de'
        ]

        # Exclure les requêtes non pertinentes
        exclude_keywords = [
            'prix', 'achat', 'acheter', 'promo', 'soldes', 'occasion',
            'pas cher', 'meilleur', 'comparatif', 'vs', 'ou'
        ]

        # Vérifier exclusions
        if any(word in query_lower for word in exclude_keywords):
            return False

        # Vérifier présence de mots-clés problème
        if any(word in query_lower for word in problem_keywords):
            return True

        return False

    def categorize_question(self, question):
        """Détermine la catégorie Apple de la question"""
        q_lower = question.lower()

        if 'iphone' in q_lower or 'ios' in q_lower:
            return 'iPhone'
        elif 'mac' in q_lower or 'macbook' in q_lower or 'macos' in q_lower:
            return 'Mac'
        elif 'ipad' in q_lower or 'ipados' in q_lower:
            return 'iPad'
        elif 'airpods' in q_lower:
            return 'AirPods'
        elif 'apple watch' in q_lower or 'watch' in q_lower:
            return 'Apple Watch'
        elif 'apple tv' in q_lower:
            return 'Apple TV'
        elif 'airtag' in q_lower:
            return 'AirTag'
        else:
            return 'Apple'

    def extract_keywords(self, question):
        """Extrait les mots-clés de la question"""
        # Mots vides à retirer
        stop_words = {'le', 'la', 'les', 'un', 'une', 'des', 'de', 'mon', 'ma', 'mes',
                      'ne', 'pas', 'plus', 'qui', 'que', 'comment', 'pourquoi'}

        words = question.lower().split()
        keywords = [w for w in words if len(w) > 3 and w not in stop_words]

        return keywords[:5]  # Max 5 mots-clés

    def find_best_question(self):
        """Trouve LA meilleure question tendance du jour"""
        print("🔍 Recherche des questions Apple tendances sur Google...\n")

        all_questions = []

        # Parcourir les mots-clés Apple
        for keyword in self.apple_keywords:
            queries = self.get_related_queries(keyword)
            all_questions.extend(queries)

            # Pause pour ne pas surcharger Google Trends
            time.sleep(2)

        # Dédupliquer
        all_questions = list(set(all_questions))

        if not all_questions:
            print("\n⚠️  Aucune question tendance trouvée aujourd'hui")
            print("💡 Solutions:")
            print("   1. Réessaye dans quelques heures (Google Trends se met à jour)")
            print("   2. Utilise find_question_simple.py à la place")
            return None

        print(f"\n✅ {len(all_questions)} questions tendances trouvées")

        # Filtrer les questions déjà traitées
        covered_titles = [q.get('question', '') for q in self.already_covered]
        new_questions = [q for q in all_questions if q not in covered_titles]

        if not new_questions:
            print("\n⚠️  Toutes les questions tendances ont déjà été traitées")
            print("💡 Utilise find_question_simple.py pour accéder à plus de questions")
            return None

        # Choisir une question aléatoire
        selected = random.choice(new_questions)

        print(f"\n🎯 QUESTION SÉLECTIONNÉE:")
        print(f"   Titre: {selected}")
        print(f"   Catégorie: {self.categorize_question(selected)}")
        print(f"   Source: Google Trends (recherches réelles)")

        return {
            'title': selected,
            'category': self.categorize_question(selected),
            'keywords': self.extract_keywords(selected),
            'source': 'Google Trends'
        }

    def generate_article_prompt(self, question):
        """Génère le prompt pour Claude"""
        prompt = f"""Tu es un expert Apple qui écrit pour "Pomme d'Actu", un blog spécialisé.

QUESTION À TRAITER (issue de Google Trends - vraie recherche d'utilisateurs):
{question['title']}

CATÉGORIE: {question['category']}

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
    print("🍎 POMME D'ACTU - Questions tendances Google Trends")
    print("=" * 60)
    print()

    finder = TrendsQuestionFinder()

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
