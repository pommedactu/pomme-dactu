# ⚡ Démarrage rapide - Pomme d'Actu

**Mets ton blog en ligne en 20 minutes chrono !**

## ✅ Checklist d'installation

### 1️⃣ Installer Python (2 min)

```bash
# Vérifier Python
python3 --version

# Si pas installé : télécharge sur python.org
```

### 2️⃣ Installer les dépendances (1 min)

```bash
cd pomme-dactu
pip3 install -r requirements.txt
```

### 3️⃣ Configurer Reddit API (5 min)

1. ➡️ Va sur https://www.reddit.com/prefs/apps
2. ➡️ Clique **"create another app"**
3. ➡️ Remplis :
   - name: `Pomme d'Actu`
   - type: `script` ✓
   - redirect: `http://localhost:8080`
4. ➡️ Copie :
   - **client_id** (sous le nom de l'app)
   - **client_secret** (ligne "secret")
5. ➡️ Édite `find_question.py` lignes 24-25 :

```python
client_id="COLLE_TON_CLIENT_ID_ICI",
client_secret="COLLE_TON_CLIENT_SECRET_ICI"
```

### 4️⃣ Créer le repo GitHub (5 min)

```bash
# Dans pomme-dactu/
git add .
git commit -m "Initial commit"

# Créer un nouveau repo sur github.com
# Puis :
git remote add origin https://github.com/TON-USERNAME/pomme-dactu.git
git branch -M main
git push -u origin main
```

### 5️⃣ Déployer sur Netlify (5 min)

1. ➡️ Va sur https://app.netlify.com
2. ➡️ Clique **"Add new site"** → **"Import an existing project"**
3. ➡️ Choisis **GitHub**
4. ➡️ Sélectionne **pomme-dactu**
5. ➡️ Laisse tout par défaut
6. ➡️ Clique **"Deploy site"**

**Attends 30 secondes...**

✅ Ton site est en ligne ! (ex: `https://wonderful-name-123.netlify.app`)

**Personnalise l'URL** :
- Site settings → Change site name → `pomme-dactu`
- Nouvelle URL : `https://pomme-dactu.netlify.app`

---

## 🎯 Premier article (10 min)

### Étape 1 : Trouve la question

```bash
python3 find_question.py
```

### Étape 2 : Génère avec Claude

1. Ouvre `daily_question.json`
2. Copie le champ `"prompt"`
3. Colle dans Claude (ton abonnement)
4. Copie la réponse JSON complète

### Étape 3 : Publie

```bash
python3 publish_article.py
```

Colle la réponse de Claude, appuie sur Entrée 2 fois.

### Étape 4 : Déploie

```bash
git add .
git commit -m "Premier article"
git push
```

**Attends 30 secondes → Ton article est en ligne !** 🎉

---

## 📅 Routine quotidienne (10 min/jour)

```bash
# Matin (9h)
python3 find_question.py
# → Copie le prompt → Claude → Copie la réponse

python3 publish_article.py
# → Colle la réponse

git add . && git commit -m "Article du jour" && git push
```

**C'est tout !** ✨

---

## 🆘 Problèmes ?

**"Module praw not found"**
```bash
pip3 install praw
```

**"Invalid client_id"**
- Vérifie que tu as bien copié le client_id et secret de Reddit
- Pas d'espaces avant/après

**Le site ne se met pas à jour**
- Attends 1 minute (Netlify peut prendre 30-60s)
- Va sur Netlify → Deploys → vérifie les logs

**Aucune question trouvée**
- Relance plus tard dans la journée
- Vérifie ta connexion internet

---

## 🚀 Tu es prêt !

Maintenant consulte le `README.md` pour plus de détails et personnalisations.

**Bon blogging ! 🍎**
