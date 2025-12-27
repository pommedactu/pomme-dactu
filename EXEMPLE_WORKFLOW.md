# 📖 Exemple de workflow complet

Ce document montre un exemple concret du workflow quotidien.

## Jour 1 : Premier article

### 1. Lancer la recherche

```bash
$ python3 find_question.py

🔍 Recherche des questions Apple du jour...

  ✓ r/apple: 12 questions trouvées
  ✓ r/AppleHelp: 23 questions trouvées
  ✓ r/iphone: 18 questions trouvées
  ✓ r/mac: 9 questions trouvées

🎯 MEILLEURE QUESTION DU JOUR:
   Titre: Mon MacBook Pro M2 chauffe énormément depuis Sonoma
   Source: r/mac
   Engagement: 234 upvotes, 89 commentaires
   Score: 735

✅ Question sauvegardée dans daily_question.json

📋 PROCHAINE ÉTAPE:
   1. Ouvre daily_question.json
   2. Copie le 'prompt'
   3. Colle-le dans Claude
   4. Lance: python publish_article.py
```

### 2. Contenu de daily_question.json

Le fichier contient :

```json
{
  "date": "2025-12-27T10:30:00",
  "question": {
    "title": "Mon MacBook Pro M2 chauffe énormément depuis Sonoma",
    "score": 735,
    "subreddit": "mac",
    "upvotes": 234,
    "comments": 89
  },
  "prompt": "Tu es un expert Apple qui écrit pour \"Pomme d'Actu\", un blog spécialisé.\n\nQUESTION À TRAITER:\nMon MacBook Pro M2 chauffe énormément depuis Sonoma\n\nMISSION:\nÉcris un article de blog complet (800-1200 mots) qui résout ce problème...\n\n[Le prompt complet généré automatiquement]"
}
```

### 3. Copier le prompt dans Claude

Tu ouvres ton abonnement Claude et tu colles :

```
Tu es un expert Apple qui écrit pour "Pomme d'Actu", un blog spécialisé.

QUESTION À TRAITER:
Mon MacBook Pro M2 chauffe énormément depuis Sonoma

MISSION:
Écris un article de blog complet (800-1200 mots) qui résout ce problème...
```

### 4. Réponse de Claude (exemple)

Claude te retourne :

```json
{
  "title": "MacBook Pro M2 qui chauffe sous Sonoma : 5 solutions",
  "excerpt": "Votre MacBook Pro M2 chauffe depuis la mise à jour Sonoma ? Découvrez les 5 causes principales et leurs solutions.",
  "content": "<h2>Pourquoi votre MacBook chauffe depuis Sonoma</h2><p>Depuis la mise à jour macOS Sonoma, de nombreux utilisateurs de MacBook Pro M2 rapportent une surchauffe inhabituelle. Ce problème est généralement lié à l'indexation Spotlight ou à des processus en arrière-plan mal optimisés.</p><h2>Solution 1 : Réinitialiser le SMC</h2><ol><li>Éteignez complètement votre MacBook</li><li>Appuyez simultanément sur Shift + Control + Option (côté gauche) + bouton Power pendant 10 secondes</li><li>Relâchez tous les boutons</li><li>Rallumez normalement</li></ol><p>Cette manipulation réinitialise le System Management Controller qui gère la température.</p><h2>Solution 2 : Vérifier l'activité du moniteur</h2><p>Ouvrez le Moniteur d'activité (Applications > Utilitaires) et triez par \"% CPU\". Si vous voyez :</p><ul><li><strong>mds_stores</strong> à plus de 100% : Spotlight indexe encore. Laissez-le finir (peut prendre 2-3 heures)</li><li><strong>WindowServer</strong> élevé : Réduisez les effets visuels (Préférences Système > Accessibilité > Affichage > Réduire la transparence)</li></ul><h2>Solution 3 : Désactiver temporairement l'indexation Spotlight</h2><p>Si l'indexation ne se termine jamais :</p><ol><li>Ouvrez Terminal</li><li>Tapez : <code>sudo mdutil -a -i off</code></li><li>Attendez 5 minutes</li><li>Réactivez : <code>sudo mdutil -a -i on</code></li></ol><h2>Solution 4 : Mettre à jour les apps tierces</h2><p>Certaines applications ne sont pas encore optimisées pour Sonoma. Mettez à jour :</p><ul><li>Antivirus (souvent problématiques)</li><li>Apps de cloud (Google Drive, Dropbox)</li><li>Apps de virtualisation (Parallels, VMware)</li></ul><h2>Solution 5 : Clean install en dernier recours</h2><p>Si rien ne fonctionne après 3-4 jours, une installation propre peut être nécessaire. Avant :</p><ol><li>Sauvegardez avec Time Machine</li><li>Téléchargez l'installateur Sonoma</li><li>Créez une clé USB bootable</li><li>Réinstallez depuis zéro</li></ol><h2>Pourquoi ça marche</h2><p>macOS Sonoma a introduit de nouveaux processus d'indexation et de synchronisation iCloud. Sur les M2, la gestion thermique est différente des Intel : les ventilateurs se déclenchent plus tard. C'est normal que ça chauffe un peu plus, mais pas au point d'être inconfortable.</p><h3>Quand s'inquiéter ?</h3><p>Contactez Apple si :</p><ul><li>Le MacBook est trop chaud pour être touché</li><li>Les ventilateurs tournent à fond en permanence (après 1 semaine)</li><li>Des ralentissements apparaissent</li></ul><h2>Conclusion</h2><p>Dans 90% des cas, la surchauffe post-Sonoma se résout en 48-72h une fois l'indexation terminée. Patience et surveillance sont les maîtres-mots. Si le problème persiste au-delà d'une semaine, passez aux solutions avancées ou contactez le support Apple.</p>",
  "keywords": ["MacBook Pro", "M2", "Sonoma", "surchauffe", "chauffe", "température"]
}
```

### 5. Publier l'article

```bash
$ python3 publish_article.py

🚀 PUBLICATION D'ARTICLE - Pomme d'Actu

📝 Colle la réponse JSON de Claude ci-dessous (termine avec une ligne vide):
------------------------------------------------------------
```

**Tu colles la réponse de Claude** puis appuies sur Entrée 2 fois.

```bash
📄 Slug: macbook-pro-m2-qui-chauffe-sous-sonoma-5-solutions
✅ Page créée: articles/macbook-pro-m2-qui-chauffe-sous-sonoma-5-solutions.html
✅ Index mis à jour
✅ Question marquée comme traitée

🎉 ARTICLE PUBLIÉ AVEC SUCCÈS!

📋 PROCHAINES ÉTAPES:
   1. Teste localement: ouvre index.html dans un navigateur
   2. Commite et push sur GitHub:
      git add .
      git commit -m 'Nouvel article: MacBook Pro M2 qui chauffe sous Sonoma : 5 solu'
      git push
   3. Netlify déploiera automatiquement!
```

### 6. Tester localement

Tu peux ouvrir `index.html` dans ton navigateur pour vérifier que tout s'affiche bien.

### 7. Déployer

```bash
$ git add .
$ git commit -m "Article: MacBook Pro M2 qui chauffe sous Sonoma"
[main abc1234] Article: MacBook Pro M2 qui chauffe sous Sonoma
 3 files changed, 250 insertions(+)
 create mode 100644 articles/macbook-pro-m2-qui-chauffe-sous-sonoma-5-solutions.html

$ git push
Énumération des objets: 8, fait.
...
To https://github.com/ton-username/pomme-dactu.git
   abc1234..def5678  main -> main
```

### 8. Netlify déploie automatiquement

Tu vas sur https://app.netlify.com et tu vois :

```
✅ Deploy successful!
   https://pomme-dactu.netlify.app
```

**C'est fait ! Ton article est en ligne !** 🎉

---

## Jour 2 : Deuxième article

Le workflow est exactement le même :

```bash
# 1. Trouver la question
python3 find_question.py

# 2. Copier le prompt de daily_question.json → Claude

# 3. Publier
python3 publish_article.py
# (coller la réponse)

# 4. Déployer
git add . && git commit -m "Article jour 2" && git push
```

**Le script évite automatiquement** les questions déjà traitées grâce à `covered_questions.json`.

---

## Aperçu du résultat

### Page d'accueil (index.html)

```
┌─────────────────────────────────────────────┐
│         🍎 Pomme d'Actu                     │
│   Votre dose quotidienne de solutions Apple │
└─────────────────────────────────────────────┘

  Solutions aux problèmes Apple les plus recherchés
  Chaque jour, une réponse claire et détaillée à LA
  question que se posent les utilisateurs Apple.

┌──────────────────┐  ┌──────────────────┐
│  [Gradient]      │  │  [Gradient]      │
│                  │  │                  │
│ 27 décembre 2025 │  │ 26 décembre 2025 │
│                  │  │                  │
│ MacBook Pro M2   │  │ iPhone 14 ne     │
│ qui chauffe sous │  │ charge plus au-  │
│ Sonoma : 5 sol..│  │ delà de 80%      │
│                  │  │                  │
│ Lire la suite →  │  │ Lire la suite →  │
└──────────────────┘  └──────────────────┘
```

### Page article

```
🍎 Pomme d'Actu
Votre dose quotidienne de solutions Apple

← Retour aux articles

MacBook Pro M2 qui chauffe sous Sonoma : 5 solutions

Publié le 27 décembre 2025

[Contenu de l'article bien formaté avec H2, H3, listes, etc.]
```

---

## Statistiques après 1 mois

**Effort total** : ~5 heures (10 min × 30 jours)

**Résultat** :
- ✅ 30 articles de qualité publiés
- ✅ SEO optimisé pour chaque article
- ✅ Blog professionnel et responsive
- ✅ Historique des questions traitées
- ✅ Prêt pour monétisation

**Coût** : 0€ (tu utilises ton abonnement Claude existant)

---

**Prêt à démarrer ? Suis le README.md !** 🚀
