# 🍎 Pomme d'Actu - Résumé du projet

## 📊 Vue d'ensemble

**Nom** : Pomme d'Actu
**Type** : Blog automatisé de solutions Apple
**Workflow** : Hybride (semi-automatique)
**Coût** : 0€/mois (utilise ton abonnement Claude existant)
**Temps quotidien** : 10 minutes
**Hébergement** : Netlify (gratuit)

---

## 🎯 Objectif

Créer un blog qui publie **1 article par jour** répondant à LA question Apple la plus recherchée du moment.

---

## ⚙️ Architecture technique

### Frontend
- **HTML/CSS/JS statique** : ultra-rapide, SEO-friendly
- **Design responsive** : mobile-first
- **Gradients dynamiques** : visuellement attrayant

### Backend (Scripts Python)
1. **find_question.py** : Trouve la meilleure question quotidienne
   - Sources : Reddit (r/apple, r/AppleHelp, r/iphone, r/mac)
   - Scoring : upvotes × 2 + commentaires × 3
   - Évite les doublons via `covered_questions.json`

2. **publish_article.py** : Crée et publie l'article
   - Génère HTML avec SEO optimisé
   - Crée slug URL-friendly
   - Met à jour l'index JSON
   - Marque la question comme traitée

### Déploiement
- **Git** : versioning
- **GitHub** : hébergement du code
- **Netlify** : déploiement automatique (Git push = déploiement)

---

## 📁 Structure des fichiers

```
pomme-dactu/
├── 📄 index.html              # Page d'accueil
├── 🎨 style.css               # Design
├── ⚡ script.js               # Chargement articles
├── 📁 articles/
│   ├── index.json            # Index de tous les articles
│   └── *.html                # Pages d'articles individuels
├── 🐍 find_question.py        # Script recherche quotidienne
├── 🐍 publish_article.py      # Script publication
├── 📋 covered_questions.json  # Historique questions traitées
├── ⚙️ netlify.toml            # Config Netlify
├── 🔧 requirements.txt        # Dépendances Python
├── 🚀 daily.sh                # Script helper routine
└── 📚 Documentation/
    ├── README.md             # Guide complet
    ├── QUICKSTART.md         # Démarrage rapide
    ├── NEXT_STEPS.md         # Prochaines étapes
    ├── EXEMPLE_WORKFLOW.md   # Exemple détaillé
    └── TEMPLATE_ARTICLE.json # Template pour Claude
```

---

## 🔄 Workflow quotidien détaillé

### 1️⃣ Recherche (2 min)
```bash
python3 find_question.py
```
- Analyse 4 subreddits Apple
- Trouve les 50 posts "hot" de chaque
- Filtre les vraies questions techniques
- Score selon engagement
- Évite les questions déjà traitées
- Génère un prompt optimisé
- **Output** : `daily_question.json`

### 2️⃣ Génération (5 min)
- Ouvrir `daily_question.json`
- Copier le champ `"prompt"`
- Coller dans Claude (claude.ai)
- Claude génère l'article au format JSON
- Copier la réponse complète

### 3️⃣ Publication (2 min)
```bash
python3 publish_article.py
```
- Coller la réponse de Claude
- Le script crée :
  - Page HTML de l'article
  - Slug SEO-friendly
  - Meta tags OpenGraph
  - Schema.org markup
  - Mise à jour index.json

### 4️⃣ Déploiement (1 min)
```bash
git add .
git commit -m "Article: [titre]"
git push
```
- Netlify détecte le push
- Déploiement automatique en ~30s
- Article en ligne !

---

## 💰 Modèle économique

### Phase 1 : Croissance (Mois 1-3)
- Focus : Publier régulièrement
- Objectif : 50-100 articles
- Trafic : SEO organique Google
- Revenus : 0€

### Phase 2 : Monétisation (Mois 4+)
- **Google AdSense** : 50-200€/mois (selon trafic)
- **Affiliation Amazon** : 20-100€/mois
- **Liens sponsorisés** : variable

### Phase 3 : Scale (Mois 6+)
- Automatisation complète via API Claude (~30€/mois)
- Multi-langues (EN, ES, etc.)
- Newsletter + produits digitaux
- Objectif : 500-1000€/mois

---

## 📈 Métriques de succès

### Après 1 mois
- ✅ 30 articles publiés
- 📊 100-500 visiteurs/mois (Google)
- 🎯 Pages indexées par Google

### Après 3 mois
- ✅ 90 articles
- 📊 1000-3000 visiteurs/mois
- 💰 Premiers revenus AdSense

### Après 6 mois
- ✅ 180 articles
- 📊 5000-10000 visiteurs/mois
- 💰 300-800€/mois de revenus
- 🤖 Automatisation complète rentabilisée

---

## 🔧 Stack technique complète

**Langages** :
- HTML5
- CSS3 (Grid, Flexbox)
- JavaScript (ES6+)
- Python 3

**Dépendances** :
- praw (Reddit API)

**Services** :
- GitHub (gratuit)
- Netlify (gratuit)
- Reddit API (gratuit)
- Claude (abonnement existant 20€/mois)

**Optionnel** :
- Google Analytics (gratuit)
- Nom de domaine (~12€/an)
- API Claude pour automatisation (~30€/mois)

---

## 🎨 Design et UX

**Inspiration** : Apple.com
- Minimaliste
- Espacements généreux
- Typographie SF Pro (système)
- Gradients modernes
- Mobile-first

**Couleurs** :
- Primaire : #667eea → #764ba2 (gradient violet)
- Texte : #1d1d1f (noir Apple)
- Background : #f5f5f7 (gris clair Apple)
- Liens : #0071e3 (bleu Apple)

**Performance** :
- Pas de framework lourd
- CSS vanilla optimisé
- Images lazy-load (futur)
- Score Lighthouse : 95+

---

## 🔒 Sécurité

**Credentials Reddit** :
- Ne JAMAIS commit client_id/secret
- `.gitignore` protège les fichiers sensibles

**Déploiement** :
- HTTPS automatique via Netlify
- Headers de sécurité dans `netlify.toml`

---

## 📚 SEO

**On-page** :
- Titres H1/H2/H3 structurés
- Meta descriptions uniques
- URLs parlantes (slugs)
- Schema.org markup (Article)
- OpenGraph tags
- Alt text sur images

**Technique** :
- Sitemap.xml (généré auto)
- robots.txt
- Performance optimale
- Mobile-friendly

**Contenu** :
- 800-1200 mots/article
- Mots-clés naturels
- Questions réelles d'utilisateurs
- Réponses actionnables

---

## 🚀 Évolutions futures possibles

### Court terme (Mois 1-3)
- [ ] Google Analytics
- [ ] Newsletter (Mailchimp gratuit)
- [ ] Images automatiques (Unsplash API)
- [ ] Sitemap XML auto-généré

### Moyen terme (Mois 3-6)
- [ ] Nom de domaine custom
- [ ] Recherche interne
- [ ] Catégories (iPhone, Mac, iPad, etc.)
- [ ] Articles connexes

### Long terme (Mois 6+)
- [ ] API Claude pour full automation
- [ ] Multi-langues (EN, ES)
- [ ] Produits digitaux (ebooks, formations)
- [ ] Communauté Discord

---

## ✅ Avantages de cette approche

1. **Coût 0€** : utilise ton abonnement Claude existant
2. **Simple** : pas de CMS complexe, juste HTML/Python
3. **Scalable** : facile d'automatiser à 100% plus tard
4. **SEO-friendly** : site statique ultra-rapide
5. **Flexible** : contrôle total du code
6. **Pédagogique** : tu apprends Git, Python, déploiement
7. **Portable** : peut migrer facilement ailleurs que Netlify

---

## ⚠️ Limites actuelles

1. **Manuel** : 10 min/jour requis (mais automatisable)
2. **1 source** : Reddit uniquement (mais extensible)
3. **Pas de CMS** : édition manuelle si corrections
4. **Mono-langue** : FR uniquement pour l'instant

Mais toutes ces limites sont **facilement surmontables** !

---

## 🎯 Pour résumer

Tu as maintenant un **système complet** pour :

✅ Trouver automatiquement les meilleures questions Apple
✅ Générer des articles de qualité avec Claude
✅ Publier en 1 clic avec SEO optimisé
✅ Déployer automatiquement sur Netlify
✅ Construire un blog profitable

**Effort** : 10 min/jour
**Coût** : 0€ supplémentaire
**Résultat** : Blog professionnel en croissance continue

**C'est parti ! 🚀**
