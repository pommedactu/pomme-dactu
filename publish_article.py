#!/usr/bin/env python3
"""
Script pour publier un article sur Pomme d'Actu
Prend la réponse de Claude et crée la page HTML
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path


class ArticlePublisher:
    def __init__(self):
        self.articles_dir = Path('articles')
        self.articles_dir.mkdir(exist_ok=True)

    def slugify(self, text):
        """Convertit un titre en slug URL-friendly"""
        text = text.lower()
        text = re.sub(r'[éèêë]', 'e', text)
        text = re.sub(r'[àâä]', 'a', text)
        text = re.sub(r'[îï]', 'i', text)
        text = re.sub(r'[ôö]', 'o', text)
        text = re.sub(r'[ùûü]', 'u', text)
        text = re.sub(r'[ç]', 'c', text)
        text = re.sub(r'[^a-z0-9]+', '-', text)
        text = re.sub(r'^-|-$', '', text)
        return text[:60]  # Max 60 caractères

    def load_article_data(self):
        """Charge la réponse de Claude depuis le presse-papier ou fichier"""
        print("📝 Colle la réponse JSON de Claude ci-dessous (termine avec une ligne vide):")
        print("-" * 60)

        lines = []
        while True:
            try:
                line = input()
                if not line and lines:  # Ligne vide après du contenu = fin
                    break
                lines.append(line)
            except EOFError:
                break

        json_text = '\n'.join(lines)

        # Extraire le JSON si Claude a ajouté du texte autour
        json_match = re.search(r'\{.*\}', json_text, re.DOTALL)
        if json_match:
            json_text = json_match.group(0)

        try:
            return json.loads(json_text)
        except json.JSONDecodeError as e:
            print(f"\n❌ Erreur: Le JSON n'est pas valide: {e}")
            print("💡 Assure-toi de copier UNIQUEMENT la réponse JSON de Claude")
            return None

    def create_article_html(self, article_data, slug):
        """Crée la page HTML de l'article"""
        date = datetime.now()
        date_str = date.strftime('%Y-%m-%d')
        date_readable = date.strftime('%d %B %Y')

        # Traduire le mois en français
        months_fr = {
            'January': 'janvier', 'February': 'février', 'March': 'mars',
            'April': 'avril', 'May': 'mai', 'June': 'juin',
            'July': 'juillet', 'August': 'août', 'September': 'septembre',
            'October': 'octobre', 'November': 'novembre', 'December': 'décembre'
        }
        for en, fr in months_fr.items():
            date_readable = date_readable.replace(en, fr)

        html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{article_data['excerpt']}">
    <meta name="keywords" content="{', '.join(article_data.get('keywords', []))}">
    <title>{article_data['title']} - Pomme d'Actu</title>
    <link rel="stylesheet" href="../style.css">

    <!-- SEO Meta Tags -->
    <meta property="og:title" content="{article_data['title']}">
    <meta property="og:description" content="{article_data['excerpt']}">
    <meta property="og:type" content="article">

    <!-- Schema.org markup -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{article_data['title']}",
      "description": "{article_data['excerpt']}",
      "datePublished": "{date_str}",
      "author": {{
        "@type": "Organization",
        "name": "Pomme d'Actu"
      }}
    }}
    </script>
</head>
<body>
    <header>
        <div class="container">
            <h1>🍎 Pomme d'Actu</h1>
            <p class="tagline">Votre dose quotidienne de solutions Apple</p>
        </div>
    </header>

    <main>
        <article class="article-full">
            <a href="../index.html" class="back-link">← Retour aux articles</a>

            <h1>{article_data['title']}</h1>

            <div class="meta">
                Publié le {date_readable}
            </div>

            <div class="content">
                {article_data['content']}
            </div>
        </article>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2025 Pomme d'Actu - Tous droits réservés</p>
        </div>
    </footer>
</body>
</html>
"""
        return html

    def update_index(self, article_data, slug):
        """Met à jour l'index JSON des articles"""
        index_file = self.articles_dir / 'index.json'

        # Charger l'index existant
        if index_file.exists():
            with open(index_file, 'r', encoding='utf-8') as f:
                articles = json.load(f)
        else:
            articles = []

        # Ajouter le nouvel article
        articles.append({
            'title': article_data['title'],
            'excerpt': article_data['excerpt'],
            'slug': slug,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'keywords': article_data.get('keywords', [])
        })

        # Sauvegarder
        with open(index_file, 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=2, ensure_ascii=False)

    def mark_question_as_covered(self):
        """Marque la question comme traitée"""
        try:
            with open('daily_question.json', 'r', encoding='utf-8') as f:
                daily = json.load(f)

            # Charger l'historique
            try:
                with open('covered_questions.json', 'r', encoding='utf-8') as f:
                    covered = json.load(f)
            except FileNotFoundError:
                covered = []

            # Ajouter
            covered.append({
                'question': daily['question']['title'],
                'date': datetime.now().isoformat(),
                'subreddit': daily['question']['subreddit']
            })

            # Sauvegarder
            with open('covered_questions.json', 'w', encoding='utf-8') as f:
                json.dump(covered, f, indent=2, ensure_ascii=False)

        except FileNotFoundError:
            pass  # Pas grave si daily_question.json n'existe pas

    def publish(self):
        """Processus complet de publication"""
        print("🚀 PUBLICATION D'ARTICLE - Pomme d'Actu\n")

        # Charger les données de l'article
        article_data = self.load_article_data()
        if not article_data:
            return

        # Vérifier les champs requis
        required = ['title', 'excerpt', 'content']
        missing = [f for f in required if f not in article_data]
        if missing:
            print(f"\n❌ Champs manquants: {', '.join(missing)}")
            return

        # Créer le slug
        slug = self.slugify(article_data['title'])
        print(f"\n📄 Slug: {slug}")

        # Créer la page HTML
        html = self.create_article_html(article_data, slug)
        html_path = self.articles_dir / f'{slug}.html'

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"✅ Page créée: {html_path}")

        # Mettre à jour l'index
        self.update_index(article_data, slug)
        print(f"✅ Index mis à jour")

        # Marquer la question comme couverte
        self.mark_question_as_covered()
        print(f"✅ Question marquée comme traitée")

        print(f"\n🎉 ARTICLE PUBLIÉ AVEC SUCCÈS!")
        print(f"\n📋 PROCHAINES ÉTAPES:")
        print(f"   1. Teste localement: ouvre index.html dans un navigateur")
        print(f"   2. Commite et push sur GitHub:")
        print(f"      git add .")
        print(f"      git commit -m 'Nouvel article: {article_data['title'][:50]}'")
        print(f"      git push")
        print(f"   3. Netlify déploiera automatiquement!")


def main():
    publisher = ArticlePublisher()
    publisher.publish()


if __name__ == "__main__":
    main()
