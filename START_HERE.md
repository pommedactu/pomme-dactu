# 👋 COMMENCE ICI !

**Bienvenue sur Pomme d'Actu !**

Tu as maintenant un blog complet prêt à être déployé. Voici par où commencer :

---

## 🎯 Choisis ton parcours

### 🚀 Je veux démarrer VITE (20 min)

➡️ **Lis : `QUICKSTART.md`**

Ce guide te fait passer de zéro à blog en ligne en 20 minutes chrono.

### 📚 Je veux tout comprendre en détail

➡️ **Lis : `README.md`**

Documentation complète avec toutes les explications, personnalisations possibles, et dépannage.

### ✅ Je veux suivre une checklist étape par étape

➡️ **Lis : `CHECKLIST.md`**

Liste de cases à cocher pour l'installation, le premier article, et la routine quotidienne.

---

## 📖 Autres fichiers utiles

- **`NEXT_STEPS.md`** : Que faire après avoir lu ce fichier
- **`EXEMPLE_WORKFLOW.md`** : Exemple concret d'un article du début à la fin
- **`RESUME_PROJET.md`** : Vue d'ensemble technique du projet
- **`TEMPLATE_ARTICLE.json`** : Format attendu pour les articles générés par Claude

---

## ⚡ Quick start ultra-rapide

**Si tu veux juste tester maintenant :**

1. **Configure Reddit** (5 min) :
   - Va sur https://www.reddit.com/prefs/apps
   - Crée une app (type: script)
   - Copie client_id et client_secret dans `find_question.py` lignes 24-25

2. **Installe les dépendances** (1 min) :
   ```bash
   pip3 install praw
   ```

3. **Teste** (1 min) :
   ```bash
   python3 find_question.py
   ```

**Si ça marche**, tu verras une question Apple s'afficher ! 🎉

Ensuite suis `QUICKSTART.md` pour le reste.

---

## 🆘 Besoin d'aide ?

**Erreur "Module praw not found"** :
```bash
pip3 install praw
```

**Erreur "Invalid credentials"** :
- Vérifie que tu as bien copié client_id et client_secret de Reddit

**Autre problème** :
- Consulte la section "Dépannage" dans `README.md`

---

## 📊 Ce que tu vas créer

Un blog qui :
- ✅ Publie 1 article/jour automatiquement
- ✅ Répond aux vraies questions des utilisateurs Apple
- ✅ Est hébergé gratuitement sur Netlify
- ✅ Est SEO-optimisé pour Google
- ✅ Ne coûte rien (utilise ton abonnement Claude actuel)
- ✅ Prend seulement 10 min/jour de ton temps

**Prêt ? Choisis ton parcours ci-dessus et lance-toi ! 🚀**

---

**💡 Conseil : Commence par `QUICKSTART.md` si tu veux être en ligne aujourd'hui.**
