# ✅ Checklist d'installation et de démarrage

## 🔧 Installation (à faire une seule fois)

### Prérequis
- [ ] Python 3 installé (`python3 --version`)
- [ ] Git installé (`git --version`)
- [ ] Compte GitHub créé (github.com)
- [ ] Compte Claude avec abonnement 20€/mois (claude.ai)

### Configuration Reddit API (5 min)
- [ ] Aller sur https://www.reddit.com/prefs/apps
- [ ] Créer une app (type: script)
- [ ] Noter le `client_id` (sous le nom de l'app)
- [ ] Noter le `client_secret` (ligne "secret")
- [ ] Éditer `find_question.py` lignes 24-25 avec ces valeurs
- [ ] Tester : `python3 find_question.py`

### Installation des dépendances (2 min)
```bash
cd pomme-dactu
pip3 install -r requirements.txt
```
- [ ] Commande exécutée sans erreur
- [ ] Module `praw` installé

### Configuration Git et GitHub (5 min)
```bash
git config --global user.name "Ton Nom"
git config --global user.email "ton@email.com"
```
- [ ] Git configuré
- [ ] Créer un nouveau repo sur GitHub nommé `pomme-dactu`
- [ ] Connecter le repo local :
```bash
git remote add origin https://github.com/TON-USERNAME/pomme-dactu.git
git branch -M main
git add .
git commit -m "Initial commit - Pomme d'Actu"
git push -u origin main
```
- [ ] Code poussé sur GitHub avec succès

### Déploiement Netlify (5 min)
- [ ] Créer un compte sur https://app.netlify.com
- [ ] Connecter avec GitHub
- [ ] "Add new site" → "Import an existing project"
- [ ] Sélectionner le repo `pomme-dactu`
- [ ] Laisser build settings par défaut
- [ ] Cliquer "Deploy site"
- [ ] Attendre le déploiement (~1 min)
- [ ] Noter l'URL fournie : `https://________.netlify.app`
- [ ] Personnaliser l'URL : Site settings → Change site name → `pomme-dactu`
- [ ] Nouvelle URL : `https://pomme-dactu.netlify.app`

### Vérification finale
- [ ] Le site s'affiche sur l'URL Netlify
- [ ] `python3 find_question.py` fonctionne
- [ ] `python3 publish_article.py` est prêt

**✅ Installation terminée !**

---

## 📝 Premier article (10 min)

### Recherche de la question
- [ ] Lancer : `python3 find_question.py`
- [ ] Une question a été trouvée
- [ ] Le fichier `daily_question.json` existe

### Génération de l'article
- [ ] Ouvrir `daily_question.json`
- [ ] Copier le contenu du champ `"prompt"`
- [ ] Aller sur claude.ai
- [ ] Coller le prompt
- [ ] Attendre la réponse de Claude
- [ ] Copier la réponse JSON complète

### Publication
- [ ] Lancer : `python3 publish_article.py`
- [ ] Coller la réponse de Claude quand demandé
- [ ] Appuyer sur Entrée 2 fois
- [ ] Le script confirme la création de la page
- [ ] Le fichier `articles/index.json` existe
- [ ] Un fichier HTML existe dans `articles/`

### Déploiement
```bash
git add .
git commit -m "Premier article publié"
git push
```
- [ ] Commit créé
- [ ] Push réussi
- [ ] Attendre 30-60 secondes
- [ ] Visiter `https://pomme-dactu.netlify.app`
- [ ] L'article s'affiche sur la page d'accueil
- [ ] Cliquer sur l'article pour voir la page complète
- [ ] Tout s'affiche correctement

**🎉 Premier article publié !**

---

## 🔄 Routine quotidienne (10 min/jour)

### Checklist quotidienne

**Matin (ou moment de ton choix) :**

- [ ] 1. Recherche : `python3 find_question.py` (2 min)
- [ ] 2. Ouvrir `daily_question.json` et copier le prompt
- [ ] 3. Générer l'article avec Claude (5 min)
- [ ] 4. Publier : `python3 publish_article.py` (2 min)
- [ ] 5. Déployer : `git add . && git commit -m "Article du jour" && git push` (1 min)
- [ ] 6. Vérifier que l'article est en ligne sur Netlify

**OU utiliser le script helper :**
```bash
./daily.sh
```

**Temps total : ~10 minutes**

---

## 📊 Suivi hebdomadaire

### Chaque semaine

- [ ] Vérifier le nombre d'articles publiés
- [ ] Consulter covered_questions.json (historique)
- [ ] (Optionnel) Vérifier Google Analytics si configuré
- [ ] (Optionnel) Lire les articles publiés pour vérifier la qualité

### Statistiques à suivre

Après 1 semaine :
- [ ] 7 articles publiés ✅
- [ ] Aucune erreur de déploiement

Après 1 mois :
- [ ] 30 articles publiés ✅
- [ ] Trafic Google commençant (vérifier Search Console)

Après 3 mois :
- [ ] 90 articles publiés ✅
- [ ] Trafic significatif (100+ visiteurs/mois)
- [ ] Considérer la monétisation

---

## 🎯 Milestones

- [ ] ✅ **Milestone 1** : Projet configuré et premier article en ligne
- [ ] ✅ **Milestone 2** : 7 articles (1 semaine de routine)
- [ ] ✅ **Milestone 3** : 30 articles (1 mois)
- [ ] 📊 **Milestone 4** : 100 visiteurs/mois
- [ ] 💰 **Milestone 5** : Premier revenu AdSense
- [ ] 🚀 **Milestone 6** : 90 articles + automatisation API

---

## 🆘 Dépannage

### Problèmes fréquents

**❌ "Module praw not found"**
- [ ] Exécuter : `pip3 install praw`

**❌ "Invalid credentials" (Reddit)**
- [ ] Vérifier client_id dans find_question.py
- [ ] Vérifier client_secret dans find_question.py
- [ ] Pas d'espaces avant/après les valeurs

**❌ "Permission denied" (Git)**
- [ ] Configurer Git : `git config --global user.name "Ton Nom"`
- [ ] Configurer email : `git config --global user.email "ton@email.com"`

**❌ Netlify ne déploie pas**
- [ ] Vérifier que `git push` a réussi
- [ ] Aller sur Netlify → Deploys
- [ ] Vérifier les logs de déploiement
- [ ] Attendre 1-2 minutes

**❌ "Aucune question trouvée"**
- [ ] Vérifier la connexion Internet
- [ ] Réessayer plus tard dans la journée
- [ ] Vérifier que les credentials Reddit sont corrects

---

## 📚 Ressources

### Documentation du projet
- [ ] Lire `QUICKSTART.md` pour démarrage rapide
- [ ] Lire `README.md` pour la doc complète
- [ ] Consulter `EXEMPLE_WORKFLOW.md` pour un exemple détaillé
- [ ] Voir `RESUME_PROJET.md` pour la vue d'ensemble

### Commandes utiles

**Tester localement :**
```bash
open index.html  # macOS
```

**Voir les logs Git :**
```bash
git log --oneline
```

**Voir le statut :**
```bash
git status
```

**Voir les articles publiés :**
```bash
cat articles/index.json
```

**Compter les articles :**
```bash
python3 -c "import json; print(len(json.load(open('articles/index.json'))))"
```

---

## 🎉 Félicitations !

Une fois toutes les cases cochées dans "Installation" et "Premier article", tu es prêt pour la routine quotidienne !

**Objectif : cocher toutes les cases de la routine quotidienne pendant 30 jours d'affilée !**

Bon courage ! 🍎✨
