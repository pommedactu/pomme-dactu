#!/bin/bash
# Script helper pour la routine quotidienne

echo "🍎 POMME D'ACTU - Routine quotidienne"
echo "======================================"
echo ""

# Étape 1 : Trouver la question
echo "📍 ÉTAPE 1/4 : Recherche de la question du jour"
echo ""
python3 find_question.py

if [ ! -f "daily_question.json" ]; then
    echo ""
    echo "❌ Aucune question trouvée. Réessaye plus tard."
    exit 1
fi

echo ""
echo "✅ Question trouvée !"
echo ""
echo "────────────────────────────────────────"
echo "📍 ÉTAPE 2/4 : Génération de l'article"
echo "────────────────────────────────────────"
echo ""
echo "1. Ouvre daily_question.json"
echo "2. Copie le contenu du champ 'prompt'"
echo "3. Colle-le dans Claude (claude.ai)"
echo "4. Copie la réponse JSON complète de Claude"
echo ""
read -p "Appuie sur Entrée quand tu as la réponse de Claude..."
echo ""

# Étape 3 : Publier
echo "────────────────────────────────────────"
echo "📍 ÉTAPE 3/4 : Publication"
echo "────────────────────────────────────────"
echo ""
python3 publish_article.py

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Erreur lors de la publication"
    exit 1
fi

echo ""
echo "✅ Article publié localement !"
echo ""

# Étape 4 : Déploiement
echo "────────────────────────────────────────"
echo "📍 ÉTAPE 4/4 : Déploiement sur Netlify"
echo "────────────────────────────────────────"
echo ""

# Récupérer le titre de l'article
if [ -f "articles/index.json" ]; then
    TITLE=$(python3 -c "import json; data=json.load(open('articles/index.json')); print(data[-1]['title'][:50])" 2>/dev/null || echo "Nouvel article")
else
    TITLE="Nouvel article"
fi

git add .
git commit -m "Article: $TITLE"

echo ""
read -p "Pusher sur GitHub maintenant ? (o/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Oo]$ ]]; then
    git push
    echo ""
    echo "✅ Déployé sur GitHub !"
    echo ""
    echo "🎉 TERMINÉ ! Ton article sera en ligne dans ~1 minute sur Netlify"
    echo ""
    echo "📊 Statistiques :"
    ARTICLE_COUNT=$(python3 -c "import json; print(len(json.load(open('articles/index.json'))))" 2>/dev/null || echo "1")
    echo "   - Articles publiés : $ARTICLE_COUNT"
    echo "   - URL : https://pomme-dactu.netlify.app"
else
    echo ""
    echo "⚠️  Push annulé. Lance 'git push' manuellement quand tu veux."
fi

echo ""
echo "À demain ! 👋"
