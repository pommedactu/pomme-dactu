#!/usr/bin/env python3
"""
Version simplifiée : trouve les questions Apple populaires
Sans dépendance Reddit - utilise une base de questions courantes
"""

import json
import random
from datetime import datetime

# Questions Apple populaires et récurrentes
# Basées sur les recherches Google et forums Apple
APPLE_QUESTIONS = [
    {
        "title": "Mon iPhone ne charge plus au-delà de 80%",
        "category": "iPhone",
        "keywords": ["iPhone", "batterie", "charge", "80%", "optimisation"]
    },
    {
        "title": "MacBook Pro M2 qui chauffe énormément depuis Sonoma",
        "category": "Mac",
        "keywords": ["MacBook Pro", "M2", "Sonoma", "surchauffe", "température"]
    },
    {
        "title": "AirPods qui se déconnectent constamment",
        "category": "AirPods",
        "keywords": ["AirPods", "déconnexion", "Bluetooth", "problème"]
    },
    {
        "title": "Comment récupérer des photos supprimées sur iPhone",
        "category": "iPhone",
        "keywords": ["iPhone", "photos", "récupération", "supprimées", "iCloud"]
    },
    {
        "title": "iPad qui redémarre tout seul en boucle",
        "category": "iPad",
        "keywords": ["iPad", "redémarrage", "boucle", "crash", "bug"]
    },
    {
        "title": "Apple Watch ne compte pas les pas correctement",
        "category": "Apple Watch",
        "keywords": ["Apple Watch", "pas", "activité", "santé", "précision"]
    },
    {
        "title": "Impossible de mettre à jour vers iOS 18",
        "category": "iPhone",
        "keywords": ["iOS 18", "mise à jour", "installation", "erreur", "iPhone"]
    },
    {
        "title": "Mac ralenti après la mise à jour Sonoma",
        "category": "Mac",
        "keywords": ["Mac", "lenteur", "Sonoma", "performance", "ralentissement"]
    },
    {
        "title": "Comment libérer de l'espace de stockage sur iPhone",
        "category": "iPhone",
        "keywords": ["iPhone", "stockage", "espace", "mémoire", "plein"]
    },
    {
        "title": "Face ID ne fonctionne plus après une chute",
        "category": "iPhone",
        "keywords": ["Face ID", "reconnaissance faciale", "iPhone", "réparation"]
    },
    {
        "title": "HomePod mini qui ne répond plus aux commandes Siri",
        "category": "HomePod",
        "keywords": ["HomePod", "Siri", "commandes vocales", "problème"]
    },
    {
        "title": "Comment transférer des données d'un ancien iPhone vers un nouveau",
        "category": "iPhone",
        "keywords": ["iPhone", "transfert", "données", "migration", "nouveau"]
    },
    {
        "title": "MacBook ne se connecte plus au WiFi",
        "category": "Mac",
        "keywords": ["MacBook", "WiFi", "connexion", "réseau", "internet"]
    },
    {
        "title": "AirTag qui ne localise pas mes clés",
        "category": "AirTag",
        "keywords": ["AirTag", "localisation", "Localiser", "réseau", "Bluetooth"]
    },
    {
        "title": "Comment désactiver les achats intégrés sur iPhone enfant",
        "category": "iPhone",
        "keywords": ["iPhone", "achats intégrés", "contrôle parental", "enfant"]
    },
    {
        "title": "MacBook Pro touchpad qui ne répond plus",
        "category": "Mac",
        "keywords": ["MacBook Pro", "trackpad", "touchpad", "souris", "curseur"]
    },
    {
        "title": "iCloud photos ne se synchronisent pas entre appareils",
        "category": "iCloud",
        "keywords": ["iCloud", "photos", "synchronisation", "appareils", "cloud"]
    },
    {
        "title": "Apple TV 4K qui lag pendant le streaming",
        "category": "Apple TV",
        "keywords": ["Apple TV", "lag", "streaming", "saccades", "performance"]
    },
    {
        "title": "Comment activer le mode économie d'énergie sur Mac",
        "category": "Mac",
        "keywords": ["Mac", "batterie", "économie d'énergie", "autonomie"]
    },
    {
        "title": "iPhone bloqué sur le logo Apple au démarrage",
        "category": "iPhone",
        "keywords": ["iPhone", "logo Apple", "bloqué", "démarrage", "boot loop"]
    }
]


class SimpleQuestionFinder:
    def __init__(self):
        self.already_covered = self.load_covered_questions()

    def load_covered_questions(self):
        """Charge les questions déjà traitées"""
        try:
            with open('covered_questions.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def find_best_question(self):
        """Trouve une question non traitée"""
        # Filtrer les questions déjà couvertes
        covered_titles = [q.get('question', '') for q in self.already_covered]
        available_questions = [
            q for q in APPLE_QUESTIONS
            if q['title'] not in covered_titles
        ]

        if not available_questions:
            print("\n⚠️  Toutes les questions prédéfinies ont été traitées !")
            print("💡 Tu peux :")
            print("   1. Réinitialiser covered_questions.json (supprimer son contenu)")
            print("   2. Ajouter de nouvelles questions dans find_question_simple.py")
            return None

        # Choisir une question aléatoire parmi celles disponibles
        question = random.choice(available_questions)

        print(f"\n🎯 QUESTION SÉLECTIONNÉE:")
        print(f"   Titre: {question['title']}")
        print(f"   Catégorie: {question['category']}")
        print(f"   Questions restantes: {len(available_questions) - 1}")

        return {
            'title': question['title'],
            'category': question['category'],
            'keywords': question['keywords']
        }

    def generate_article_prompt(self, question):
        """Génère le prompt pour Claude"""
        prompt = f"""Tu es un expert Apple qui écrit pour "Pomme d'Actu", un blog spécialisé.

QUESTION À TRAITER:
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
    print("🍎 POMME D'ACTU - Recherche de question (version simplifiée)")
    print("=" * 60)

    finder = SimpleQuestionFinder()

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
