# 🎯 Prochaines étapes

**Ton projet "Pomme d'Actu" est prêt !** Voici ce que tu dois faire maintenant.

## ✅ Immédiatement (20 min)

### 1. Configure l'API Reddit

**C'est la SEULE configuration obligatoire.**

1. Va sur https://www.reddit.com/prefs/apps
2. Clique "create another app"
3. Remplis le formulaire :
   ```
   name: Pomme d'Actu
   App type: script (radio button)
   description: Blog automatisé
   about url: (laisse vide)
   redirect uri: http://localhost:8080
   ```
4. Clique "create app"
5. **Note ces valeurs** :
   - `client_id` : chaîne de ~14 caractères sous le nom de l'app
   - `client_secret` : chaîne de ~27 caractères à droite de "secret:"

6. Édite `find_question.py` et remplace lignes 24-25 :
   ```python
   client_id="TA_VALEUR_ICI",
   client_secret="TA_VALEUR_ICI"
   ```

**⚠️ Ne partage JAMAIS ces clés publiquement !**

### 2. Teste le script de recherche

```bash
cd pomme-dactu
python3 find_question.py
```

**Tu devrais voir** :
```
🔍 Recherche des questions Apple du jour...
  ✓ r/apple: X questions trouvées
  ...
🎯 MEILLEURE QUESTION DU JOUR:
  Titre: ...
```

**Si erreur** : vérifie que tu as bien installé `praw` :
```bash
pip3 install praw
```

### 3. Pousse sur GitHub

```bash
git add .
git commit -m "Initial commit - Pomme d'Actu"

# Crée un nouveau repo sur github.com/new
# Nom suggéré: pomme-dactu

# Puis :
git remote add origin https://github.com/TON-USERNAME/pomme-dactu.git
git branch -M main
git push -u origin main
```

### 4. Déploie sur Netlify

**Via interface web (plus simple) :**

1. Va sur https://app.netlify.com
2. Connecte-toi avec GitHub
3. Clique "Add new site" → "Import an existing project"
4. Autorise Netlify à accéder à GitHub
5. Sélectionne le repo `pomme-dactu`
6. **Build settings** : laisse TOUT par défaut
7. Clique "Deploy site"

**Attends 1 minute...**

✅ **Ton site est en ligne !**

URL : `https://random-name-123.netlify.app`

**Personnalise l'URL :**
- Site settings → Site details → Change site name
- Entre : `pomme-dactu`
- Nouvelle URL : `https://pomme-dactu.netlify.app`

---

## 📝 Ton premier article (10 min)

### Étape 1 : Trouve la question

```bash
python3 find_question.py
```

### Étape 2 : Génère l'article

1. Ouvre `daily_question.json`
2. Copie tout le contenu du champ `"prompt"` (sans les guillemets)
3. Va sur claude.ai (ton abonnement)
4. Colle le prompt
5. Claude génère un JSON → **copie toute sa réponse**

### Étape 3 : Publie

```bash
python3 publish_article.py
```

Colle la réponse de Claude quand demandé, puis appuie sur Entrée 2 fois.

### Étape 4 : Déploie

```bash
git add .
git commit -m "Premier article publié"
git push
```

**Attends 30-60 secondes → Ton article est en ligne !** 🎉

Visite : `https://pomme-dactu.netlify.app`

---

## 🔄 Routine quotidienne (ensuite)

**Chaque jour (10 minutes) :**

```bash
# 1. Trouve la question (2 min)
python3 find_question.py

# 2. Copie le prompt de daily_question.json
#    → Colle dans Claude
#    → Copie la réponse

# 3. Publie (3 min)
python3 publish_article.py
# Colle la réponse de Claude

# 4. Déploie (1 min)
git add . && git commit -m "Article du jour" && git push
```

**C'est tout !** Le blog se construit article par article. 📈

---

## 💡 Optimisations futures (quand tu veux)

### Nom de domaine personnalisé

**Coût : ~12€/an**

1. Achète un domaine (ex: Namecheap, Google Domains)
2. Dans Netlify : Domain settings → Add custom domain
3. Configure les DNS selon les instructions Netlify

### Google Analytics

1. Crée un compte Google Analytics
2. Crée une propriété
3. Copie le code de tracking
4. Ajoute-le dans `index.html` avant `</head>`
5. Ajoute-le aussi dans le template d'article (dans `publish_article.py`)

### Monétisation

**Quand tu as 50+ visiteurs/jour :**

1. **Google AdSense** :
   - Inscription : https://www.google.com/adsense
   - Ajoute le code pub dans tes articles

2. **Affiliation Amazon** :
   - Inscription : https://affiliate-program.amazon.fr
   - Ajoute des liens produits dans les articles pertinents

### Automatisation complète (Phase 2)

**Quand le blog génère des revenus :**

Budget : ~30€/mois pour l'API Claude

1. Crée un compte API Anthropic
2. Modifie `find_question.py` pour appeler l'API directement
3. Configure GitHub Actions pour exécution quotidienne automatique
4. Plus rien à faire manuellement !

---

## 📚 Documentation

- **QUICKSTART.md** : Guide ultra-rapide
- **README.md** : Documentation complète
- **EXEMPLE_WORKFLOW.md** : Exemple détaillé d'un article complet

---

## 🆘 Besoin d'aide ?

### Problèmes fréquents

**"Module praw not found"**
```bash
pip3 install praw
```

**"Invalid credentials" (Reddit)**
- Vérifie client_id et client_secret dans `find_question.py`
- Assure-toi qu'il n'y a pas d'espaces

**"Permission denied" (Git)**
- Configure Git : `git config --global user.name "Ton Nom"`
- Configure email : `git config --global user.email "ton@email.com"`

**Netlify ne déploie pas**
- Vérifie que le push GitHub a réussi
- Va dans Netlify → Deploys → Regarde les logs
- Le déploiement prend parfois 1-2 minutes

### Ressources

- **Documentation Reddit API** : https://www.reddit.com/dev/api
- **Documentation Netlify** : https://docs.netlify.com
- **Guide Git** : https://git-scm.com/book/fr/v2

---

## 🎯 Objectifs à 30 jours

**Si tu publies 1 article/jour pendant 30 jours :**

✅ 30 articles de qualité SEO-optimisés
✅ Trafic organique Google qui commence
✅ Autorité dans la niche Apple
✅ Base solide pour monétisation
✅ Portfolio de contenu réutilisable

**Effort total : 5 heures sur le mois (10 min/jour)**

---

## 🚀 C'est parti !

**Tu as tout ce qu'il faut. Maintenant :**

1. ✅ Configure Reddit (5 min)
2. ✅ Pousse sur GitHub (5 min)
3. ✅ Déploie sur Netlify (5 min)
4. ✅ Crée ton premier article (10 min)

**Total : 25 minutes pour être en ligne avec ton premier article !**

**Bon courage ! 🍎✨**

---

P.S. : Une fois que tout fonctionne, tu peux supprimer les fichiers de doc si tu veux :
- `NEXT_STEPS.md` (ce fichier)
- `EXEMPLE_WORKFLOW.md`
- `QUICKSTART.md`

Garde juste le `README.md` pour référence future.
