# 🍎 Pomme d'Actu

Blog automatisé de solutions quotidiennes pour l'écosystème Apple.

## 📋 Vue d'ensemble

Pomme d'Actu trouve automatiquement LA question Apple la plus recherchée du jour et publie un article de qualité pour y répondre.

**Workflow quotidien : ~10 minutes**

## 🚀 Installation initiale (à faire une seule fois)

### 1. Installer Python et les dépendances

```bash
# Vérifier que Python 3 est installé
python3 --version

# Installer les dépendances
pip3 install -r requirements.txt
```

### 2. Configurer l'API Reddit (GRATUIT)

L'API Reddit est **100% gratuite** et nécessaire pour trouver les questions.

**Étapes :**

1. Va sur https://www.reddit.com/prefs/apps
2. Clique sur "create another app" (en bas)
3. Remplis :
   - **name** : Pomme d'Actu
   - **type** : Script
   - **description** : Blog automatisé
   - **redirect uri** : http://localhost:8080
4. Clique "create app"
5. **Note ces infos** :
   - `client_id` : sous le nom de l'app (chaîne aléatoire)
   - `client_secret` : ligne "secret"

6. Ouvre `find_question.py` et remplace :
```python
client_id="YOUR_CLIENT_ID",      # ← Ta valeur ici
client_secret="YOUR_CLIENT_SECRET"  # ← Ta valeur ici
```

### 3. Déployer sur Netlify (GRATUIT)

#### Option A : Via GitHub (recommandé)

1. **Créer un repo GitHub** :
```bash
cd pomme-dactu
git add .
git commit -m "Initial commit - Pomme d'Actu"

# Créer le repo sur GitHub, puis :
git remote add origin https://github.com/TON-USERNAME/pomme-dactu.git
git branch -M main
git push -u origin main
```

2. **Connecter à Netlify** :
   - Va sur https://app.netlify.com
   - Clique "Add new site" → "Import an existing project"
   - Choisis GitHub et sélectionne ton repo `pomme-dactu`
   - **Build settings** : laisse tout par défaut
   - Clique "Deploy site"

3. **Récupère ton URL** :
   - Netlify te donne une URL : `https://random-name-123.netlify.app`
   - Tu peux la personnaliser : Site settings → Change site name → `pomme-dactu`
   - Nouvelle URL : `https://pomme-dactu.netlify.app`

#### Option B : Via Netlify CLI (alternative)

```bash
# Installer Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Déployer
netlify deploy --prod
```

---

## 📅 Workflow quotidien (10 minutes)

### Étape 1 : Trouver la question du jour (2 min)

```bash
cd pomme-dactu
python3 find_question.py
```

**Ce qui se passe** :
- Le script analyse Reddit (r/apple, r/AppleHelp, r/iphone, r/mac)
- Trouve LA question la plus populaire du jour
- Génère un prompt optimisé pour Claude
- Sauvegarde dans `daily_question.json`

**Sortie** :
```
🔍 Recherche des questions Apple du jour...

  ✓ r/apple: 12 questions trouvées
  ✓ r/AppleHelp: 23 questions trouvées
  ✓ r/iphone: 18 questions trouvées
  ✓ r/mac: 9 questions trouvées

🎯 MEILLEURE QUESTION DU JOUR:
   Titre: Mon iPhone 14 ne charge plus au-delà de 80%
   Source: r/AppleHelp
   Engagement: 156 upvotes, 47 commentaires
   Score: 453

✅ Question sauvegardée dans daily_question.json
```

### Étape 2 : Générer l'article avec Claude (5 min)

1. **Ouvre `daily_question.json`**
2. **Copie** le contenu du champ `"prompt"`
3. **Colle-le dans Claude** (ton abonnement actuel)
4. **Copie la réponse JSON** de Claude

**Exemple de réponse Claude** :
```json
{
  "title": "iPhone ne charge plus au-delà de 80% : Solution complète",
  "excerpt": "Découvrez pourquoi votre iPhone s'arrête à 80% et comment désactiver l'optimisation de batterie.",
  "content": "<h2>Le problème en détail</h2><p>Votre iPhone...</p>...",
  "keywords": ["iPhone", "batterie", "charge", "80%", "optimisation"]
}
```

### Étape 3 : Publier (3 min)

```bash
python3 publish_article.py
```

**Le script te demande** :
```
📝 Colle la réponse JSON de Claude ci-dessous (termine avec une ligne vide):
------------------------------------------------------------
```

**Tu colles** la réponse de Claude, puis appuie sur Entrée 2 fois.

**Le script fait automatiquement** :
- ✅ Crée la page HTML avec SEO optimisé
- ✅ Met à jour l'index du blog
- ✅ Marque la question comme traitée (pour ne pas la retraiter)

**Sortie** :
```
📄 Slug: iphone-ne-charge-plus-au-dela-de-80-solution-complete
✅ Page créée: articles/iphone-ne-charge-plus-au-dela-de-80-solution-complete.html
✅ Index mis à jour
✅ Question marquée comme traitée

🎉 ARTICLE PUBLIÉ AVEC SUCCÈS!
```

### Étape 4 : Déployer sur Netlify (1 min)

```bash
git add .
git commit -m "Article: iPhone ne charge plus au-delà de 80%"
git push
```

**Netlify détecte automatiquement** le push et déploie en ~30 secondes.

**Ton article est en ligne** ! 🎉

---

## 🎯 Résumé quotidien

```bash
# 1. Trouver la question (2 min)
python3 find_question.py

# 2. Dans daily_question.json : copier le prompt → Claude → copier la réponse

# 3. Publier (3 min)
python3 publish_article.py
# (colle la réponse de Claude)

# 4. Déployer (1 min)
git add . && git commit -m "Nouvel article" && git push
```

**Total : ~10 minutes par jour**

---

## 📁 Structure du projet

```
pomme-dactu/
├── index.html              # Page d'accueil
├── style.css               # Design du blog
├── script.js               # Chargement dynamique des articles
├── articles/               # Dossier des articles
│   ├── index.json         # Index de tous les articles
│   └── *.html             # Pages d'articles
├── find_question.py        # Script de recherche quotidienne
├── publish_article.py      # Script de publication
├── covered_questions.json  # Historique des questions traitées
├── netlify.toml           # Config Netlify
└── README.md              # Ce fichier
```

---

## 🔧 Personnalisation

### Changer les sources de questions

Édite `find_question.py` :

```python
self.subreddits = ['apple', 'AppleHelp', 'iphone', 'mac']  # Ajoute/retire des subreddits
```

### Modifier le design

Édite `style.css` pour personnaliser les couleurs, polices, etc.

### Ajuster le prompt pour Claude

Édite la méthode `generate_article_prompt()` dans `find_question.py`.

---

## 📊 Suivi et analytics (optionnel)

### Ajouter Google Analytics

1. Crée un compte Google Analytics
2. Ajoute le code de tracking avant `</head>` dans `index.html` et le template d'article dans `publish_article.py`

### Ajouter Plausible (alternative privacy-friendly)

1. Crée un compte sur https://plausible.io (payant mais respectueux de la vie privée)
2. Ajoute leur script

---

## 💰 Monétisation future

### Google AdSense

Une fois que tu as du trafic (50+ visiteurs/jour) :

1. Inscription Google AdSense
2. Ajoute le code pub dans le template d'article

### Affiliation Amazon

Pour les tutoriels mentionnant du matériel Apple :

1. Inscription Amazon Associates
2. Ajoute des liens affiliés dans les articles pertinents

---

## 🆘 Dépannage

### "Module 'praw' not found"

```bash
pip3 install praw
```

### "Invalid client_id"

Vérifie que tu as bien copié le client_id et client_secret de Reddit dans `find_question.py`.

### "Aucune question trouvée"

C'est rare, mais peut arriver. Solutions :
- Relance le script plus tard dans la journée
- Vérifie ta connexion Internet
- Vérifie que les subreddits existent toujours

### Le site ne se met pas à jour sur Netlify

1. Vérifie que le push GitHub a fonctionné
2. Va sur Netlify → Deploys → vérifie les logs
3. Force un re-deploy : Deploys → Trigger deploy → Deploy site

---

## 🚀 Évolution future (Phase 2)

Quand le blog génère des revenus, tu pourras :

1. **Automatiser à 100%** avec l'API Claude
   - Script GitHub Actions qui tourne tous les jours à 9h
   - Génération et publication automatiques
   - Coût : ~30€/mois

2. **Multi-sources avancées**
   - Google Trends API
   - Stack Overflow
   - Forums Apple officiels

3. **Images automatiques**
   - Intégration DALL-E pour images hero
   - Screenshots automatisés

4. **Newsletter**
   - Capturer emails
   - Envoi auto du nouvel article

---

## 📞 Support

En cas de problème :

1. Vérifie ce README
2. Consulte les logs d'erreur
3. Google le message d'erreur exact

---

**Bon blogging ! 🍎✨**
