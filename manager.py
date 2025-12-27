#!/usr/bin/env python3
"""
🍎 POMME D'ACTU - Gestionnaire d'articles
Manager interactif pour gérer tout le blog facilement
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


class BlogManager:
    def __init__(self):
        self.articles_dir = Path('articles')
        self.articles_dir.mkdir(exist_ok=True)

    def clear_screen(self):
        """Efface l'écran"""
        os.system('clear' if os.name != 'nt' else 'cls')

    def show_header(self):
        """Affiche l'en-tête"""
        self.clear_screen()
        print("=" * 60)
        print("🍎 POMME D'ACTU - Gestionnaire d'articles")
        print("=" * 60)
        print()

    def get_stats(self):
        """Récupère les statistiques du blog"""
        try:
            with open('articles/index.json', 'r', encoding='utf-8') as f:
                articles = json.load(f)
                nb_articles = len(articles)
                dernier = articles[-1]['title'] if articles else "Aucun"
        except FileNotFoundError:
            nb_articles = 0
            dernier = "Aucun"

        try:
            with open('covered_questions.json', 'r', encoding='utf-8') as f:
                covered = json.load(f)
                questions_traitees = len(covered)
        except FileNotFoundError:
            questions_traitees = 0

        # Questions disponibles (20 en simple mode)
        questions_disponibles = 20 - questions_traitees

        return {
            'articles': nb_articles,
            'dernier': dernier,
            'questions_traitees': questions_traitees,
            'questions_disponibles': questions_disponibles
        }

    def show_menu(self):
        """Affiche le menu principal"""
        stats = self.get_stats()

        self.show_header()

        print(f"📊 Statistiques:")
        print(f"   Articles publiés : {stats['articles']}")
        print(f"   Dernier article : {stats['dernier'][:50]}...")
        print(f"   Questions disponibles : {stats['questions_disponibles']}")
        print()
        print("-" * 60)
        print()
        print("1. 🔍 Trouver une question tendance")
        print("2. ✍️  Générer un article (avec Claude)")
        print("3. 📤 Publier l'article sur le site")
        print("4. 📊 Voir tous les articles publiés")
        print("5. 🗑️  Supprimer un article")
        print("6. 🚀 Workflow complet (RECOMMANDÉ)")
        print("7. ⚙️  Paramètres")
        print("8. 🚪 Quitter")
        print()
        print("-" * 60)
        print()

        choice = input("Choix (1-8) : ").strip()
        return choice

    def find_question(self, source='reddit'):
        """Trouve une question"""
        self.show_header()
        print("🔍 Recherche d'une question...\n")

        if source == 'reddit':
            print("Source : Reddit (vraies questions d'utilisateurs)")
            print()
            result = subprocess.run(
                ['python3', 'find_question_reddit.py'],
                capture_output=False
            )
        elif source == 'trends':
            print("Source : Google Trends (recherches réelles)")
            print()
            result = subprocess.run(
                ['python3', 'find_question_trends.py'],
                capture_output=False
            )
        else:
            print("Source : Questions pré-définies")
            print()
            result = subprocess.run(
                ['python3', 'find_question_simple.py'],
                capture_output=False
            )

        if result.returncode == 0 and os.path.exists('daily_question.json'):
            with open('daily_question.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
        return None

    def generate_article(self):
        """Génère un article avec Claude"""
        self.show_header()

        # Vérifier qu'une question existe
        if not os.path.exists('daily_question.json'):
            print("❌ Aucune question trouvée !\n")
            print("Lance d'abord l'option 1 ou 6.\n")
            input("Appuie sur Entrée pour continuer...")
            return False

        with open('daily_question.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        question = data['question']['title']
        prompt = data['prompt']

        print(f"📝 Question : {question}\n")
        print("-" * 60)
        print()
        print("📋 PROMPT POUR CLAUDE :\n")
        print(prompt)
        print()
        print("-" * 60)
        print()
        print("✅ Copie le prompt ci-dessus (sélectionne tout + Cmd+C)")
        print()
        print("➡️  ÉTAPES :")
        print("   1. Ouvre https://claude.ai dans ton navigateur")
        print("   2. Colle le prompt (Cmd+V)")
        print("   3. Attends la réponse de Claude")
        print("   4. Copie TOUTE la réponse JSON (Cmd+A puis Cmd+C)")
        print("   5. Reviens ici")
        print()

        input("Appuie sur Entrée quand tu as la réponse de Claude...")
        print()

        # Demander la réponse
        print("📝 Colle la réponse JSON de Claude ci-dessous :")
        print("(Termine par une ligne vide)")
        print("-" * 60)

        lines = []
        while True:
            try:
                line = input()
                if not line and lines:
                    break
                lines.append(line)
            except EOFError:
                break

        response = '\n'.join(lines)

        # Sauvegarder la réponse
        with open('article_draft.json', 'w', encoding='utf-8') as f:
            f.write(response)

        print()
        print("✅ Article généré et sauvegardé !")
        print()
        input("Appuie sur Entrée pour continuer...")
        return True

    def publish_article(self):
        """Publie l'article"""
        self.show_header()

        if not os.path.exists('article_draft.json'):
            print("❌ Aucun article en attente !\n")
            print("Lance d'abord l'option 2 ou 6.\n")
            input("Appuie sur Entrée pour continuer...")
            return False

        print("📤 Publication de l'article...\n")

        # Lire l'article
        try:
            with open('article_draft.json', 'r', encoding='utf-8') as f:
                content = f.read()
                # Essayer d'extraire le JSON si Claude a ajouté du texte avant/après
                import re
                json_match = re.search(r'\{.*\}', content, re.DOTALL)
                if json_match:
                    content = json_match.group(0)
                article_data = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"❌ Erreur de format JSON : {e}\n")
            print("Le JSON de Claude n'est pas valide.")
            print("Vérifie que tu as copié UNIQUEMENT le JSON, sans texte avant/après.\n")
            input("Appuie sur Entrée pour continuer...")
            return False

        print(f"Titre : {article_data['title']}")
        print()

        confirm = input("Confirmer la publication ? (o/n) : ").strip().lower()

        if confirm != 'o':
            print("\n❌ Publication annulée")
            input("Appuie sur Entrée pour continuer...")
            return False

        # Publier avec le script
        with open('article_draft.json', 'r', encoding='utf-8') as f:
            content = f.read()

        result = subprocess.run(
            ['python3', 'publish_article.py'],
            input=content + '\n\n',
            text=True,
            capture_output=True
        )

        print()
        print(result.stdout)

        if result.returncode == 0:
            # Git commit et push
            print("\n🚀 Déploiement sur GitHub...\n")

            # Git add
            subprocess.run(['git', 'add', '.'])

            # Git commit
            commit_msg = f"Article: {article_data['title'][:50]}"
            subprocess.run(['git', 'commit', '-m', commit_msg])

            # Git push
            result = subprocess.run(['git', 'push'], capture_output=True, text=True)

            if result.returncode == 0:
                print("✅ Article publié et déployé sur Netlify !")
                print()
                print("🌐 Ton article sera en ligne dans ~1 minute")
                print()

                # Nettoyer
                if os.path.exists('article_draft.json'):
                    os.remove('article_draft.json')
                if os.path.exists('daily_question.json'):
                    os.remove('daily_question.json')
            else:
                print("⚠️  Push GitHub échoué :")
                print(result.stderr)

        input("\nAppuie sur Entrée pour continuer...")
        return result.returncode == 0

    def list_articles(self):
        """Liste tous les articles publiés"""
        self.show_header()
        print("📊 Articles publiés :\n")

        try:
            with open('articles/index.json', 'r', encoding='utf-8') as f:
                articles = json.load(f)

            if not articles:
                print("Aucun article publié pour le moment.\n")
            else:
                for i, article in enumerate(articles, 1):
                    print(f"{i}. {article['title']}")
                    print(f"   Date : {article['date']}")
                    print(f"   Slug : {article['slug']}")
                    print()

        except FileNotFoundError:
            print("Aucun article publié pour le moment.\n")

        input("Appuie sur Entrée pour continuer...")

    def delete_article(self):
        """Supprime un article"""
        self.show_header()
        print("🗑️  Suppression d'article :\n")

        try:
            with open('articles/index.json', 'r', encoding='utf-8') as f:
                articles = json.load(f)

            if not articles:
                print("Aucun article à supprimer.\n")
                input("Appuie sur Entrée pour continuer...")
                return

            # Afficher les articles
            for i, article in enumerate(articles, 1):
                print(f"{i}. {article['title']}")

            print()
            choice = input("Numéro de l'article à supprimer (0 pour annuler) : ").strip()

            if choice == '0':
                return

            idx = int(choice) - 1
            if 0 <= idx < len(articles):
                article = articles[idx]

                # Confirmer
                print()
                confirm = input(f"Supprimer '{article['title']}' ? (o/n) : ").strip().lower()

                if confirm == 'o':
                    # Supprimer le fichier HTML
                    html_file = self.articles_dir / f"{article['slug']}.html"
                    if html_file.exists():
                        html_file.unlink()

                    # Retirer de l'index
                    articles.pop(idx)

                    # Sauvegarder
                    with open('articles/index.json', 'w', encoding='utf-8') as f:
                        json.dump(articles, f, indent=2, ensure_ascii=False)

                    print("\n✅ Article supprimé !")

                    # Git commit
                    subprocess.run(['git', 'add', '.'])
                    subprocess.run(['git', 'commit', '-m', f'Suppression: {article["title"][:50]}'])
                    subprocess.run(['git', 'push'])

                    print("✅ Changements déployés !")

        except (FileNotFoundError, ValueError, IndexError):
            print("❌ Erreur lors de la suppression")

        input("\nAppuie sur Entrée pour continuer...")

    def workflow_complet(self):
        """Workflow complet automatisé"""
        self.show_header()
        print("🚀 WORKFLOW COMPLET - Publication d'un article\n")
        print("=" * 60)
        print()

        # Étape 1 : Choisir la source
        print("Source des questions :")
        print("1. Reddit (vraies questions d'utilisateurs) ⭐ RECOMMANDÉ")
        print("2. Google Trends (tendances de recherche)")
        print("3. Questions pré-définies (fiable)")
        print()
        source_choice = input("Choix (1-3) : ").strip()

        if source_choice == '1':
            source = 'reddit'
        elif source_choice == '2':
            source = 'trends'
        else:
            source = 'simple'

        # Étape 2 : Trouver une question
        print()
        print("=" * 60)
        question_data = self.find_question(source)

        if not question_data:
            print("\n❌ Aucune question trouvée")
            if source == 'trends':
                print("💡 Réessaye avec les questions pré-définies (option 2)")
            input("\nAppuie sur Entrée pour continuer...")
            return

        # Étape 3 : Générer l'article
        print()
        input("Appuie sur Entrée pour générer l'article...")

        if not self.generate_article():
            return

        # Étape 4 : Publier
        print()
        if not self.publish_article():
            return

        print()
        print("=" * 60)
        print("🎉 ARTICLE PUBLIÉ AVEC SUCCÈS !")
        print("=" * 60)
        input("\nAppuie sur Entrée pour revenir au menu...")

    def settings(self):
        """Paramètres"""
        self.show_header()
        print("⚙️  Paramètres :\n")
        print("1. Réinitialiser les questions traitées")
        print("2. Voir l'URL du site")
        print("3. Statistiques détaillées")
        print("0. Retour")
        print()

        choice = input("Choix : ").strip()

        if choice == '1':
            confirm = input("\nRéinitialiser les questions ? (o/n) : ").strip().lower()
            if confirm == 'o':
                with open('covered_questions.json', 'w', encoding='utf-8') as f:
                    json.dump([], f)
                print("✅ Questions réinitialisées !")
                input("\nAppuie sur Entrée...")

        elif choice == '2':
            print("\n🌐 URL du site : https://pommedactu.netlify.app")
            print("   (ou ton URL personnalisée)")
            input("\nAppuie sur Entrée...")

        elif choice == '3':
            stats = self.get_stats()
            print(f"\n📊 Statistiques détaillées :")
            print(f"   Articles publiés : {stats['articles']}")
            print(f"   Questions traitées : {stats['questions_traitees']}")
            print(f"   Questions disponibles : {stats['questions_disponibles']}")
            input("\nAppuie sur Entrée...")

    def run(self):
        """Boucle principale"""
        while True:
            choice = self.show_menu()

            if choice == '1':
                self.show_header()
                print("Source :")
                print("1. Reddit (recommandé)")
                print("2. Google Trends")
                print("3. Questions pré-définies")
                src = input("Choix : ").strip()
                if src == '1':
                    source = 'reddit'
                elif src == '2':
                    source = 'trends'
                else:
                    source = 'simple'
                self.find_question(source)
                input("\nAppuie sur Entrée pour continuer...")

            elif choice == '2':
                self.generate_article()

            elif choice == '3':
                self.publish_article()

            elif choice == '4':
                self.list_articles()

            elif choice == '5':
                self.delete_article()

            elif choice == '6':
                self.workflow_complet()

            elif choice == '7':
                self.settings()

            elif choice == '8':
                self.show_header()
                print("👋 À bientôt !\n")
                sys.exit(0)

            else:
                print("\n❌ Choix invalide")
                input("Appuie sur Entrée...")


def main():
    manager = BlogManager()
    manager.run()


if __name__ == "__main__":
    main()
