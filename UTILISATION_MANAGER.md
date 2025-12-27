# 🎮 Manager - Guide d'utilisation

Le **manager** est ton interface tout-en-un pour gérer Pomme d'Actu facilement !

## 🚀 Lancement

```bash
python3 manager.py
```

---

## 📋 Menu principal

```
🍎 POMME D'ACTU - Gestionnaire d'articles
=========================================

📊 Statistiques:
   Articles publiés : 1
   Dernier article : Apple TV 4K qui lag...
   Questions disponibles : 19

1. 🔍 Trouver une question tendance
2. ✍️  Générer un article (avec Claude)
3. 📤 Publier l'article sur le site
4. 📊 Voir tous les articles publiés
5. 🗑️  Supprimer un article
6. 🚀 Workflow complet (RECOMMANDÉ)
7. ⚙️  Paramètres
8. 🚪 Quitter
```

---

## 🎯 Option 6 : Workflow complet (UTILISE CELLE-CI !)

**C'est l'option la plus pratique** - elle fait tout d'un coup !

### Étapes automatiques :

1. **Choisis la source** :
   - Google Trends (recherches réelles) OU
   - Questions pré-définies (fiable)

2. **Le script trouve une question** automatiquement

3. **Le prompt est affiché** :
   - Tu copies le prompt
   - Tu vas sur claude.ai
   - Tu colles le prompt
   - Claude génère l'article
   - Tu copies la réponse JSON

4. **Tu reviens au script** :
   - Tu colles la réponse
   - Le script publie automatiquement
   - Commit + push GitHub automatique

5. **✅ Article en ligne !**

**Temps total : 2-3 minutes**

---

## 📖 Détail des options

### 1. 🔍 Trouver une question tendance

Lance juste la recherche de question sans générer l'article.

**Quand l'utiliser** : Si tu veux juste voir quelle question est disponible

### 2. ✍️ Générer un article

Génère l'article avec Claude (nécessite qu'une question ait été trouvée avant).

**Quand l'utiliser** : Si tu as déjà lancé l'option 1

### 3. 📤 Publier l'article

Publie un article déjà généré.

**Quand l'utiliser** : Si tu as généré un article mais pas encore publié

### 4. 📊 Voir tous les articles

Liste tous les articles déjà publiés sur le blog.

**Affiche** :
- Titre
- Date de publication
- Slug (URL)

### 5. 🗑️ Supprimer un article

Supprime un article publié.

**Attention** : Cette action est irréversible !

**Processus** :
1. Liste les articles
2. Tu choisis le numéro
3. Confirmation
4. Suppression + commit Git automatique

### 6. 🚀 Workflow complet

**OPTION RECOMMANDÉE** - Fait tout automatiquement du début à la fin !

### 7. ⚙️ Paramètres

**Options** :
- Réinitialiser les questions traitées (pour recommencer la liste)
- Voir l'URL du site
- Statistiques détaillées

### 8. 🚪 Quitter

Ferme le manager.

---

## 💡 Workflow quotidien recommandé

**Chaque jour (2-3 minutes) :**

```bash
python3 manager.py
```

1. Choisis **Option 6** (Workflow complet)
2. Choisis **Google Trends** (option 1) ou **Pré-défini** (option 2)
3. Copie le prompt → va sur claude.ai → colle
4. Copie la réponse JSON de Claude
5. Reviens au script → colle la réponse
6. ✅ **C'est tout !**

**Ton article est automatiquement publié et déployé sur Netlify !**

---

## 🔄 Gestion des fichiers temporaires

Le manager crée des fichiers temporaires :

- **`daily_question.json`** : Question du jour (supprimé après publication)
- **`article_draft.json`** : Article en attente (supprimé après publication)

**Ces fichiers sont automatiquement nettoyés après publication.**

---

## 🆘 Problèmes fréquents

### "Aucune question trouvée" (Google Trends)

**Solution** : Utilise les questions pré-définies à la place
- Dans le workflow, choisis option 2 au lieu de 1

### "Erreur JSON lors de la publication"

**Cause** : La réponse de Claude n'est pas au bon format

**Solution** :
1. Assure-toi de copier TOUT le JSON de Claude
2. Vérifie qu'il n'y a pas de texte avant/après le JSON
3. Réessaye en demandant à Claude de retourner UNIQUEMENT le JSON

### "Git push échoué"

**Cause** : Problème de connexion GitHub

**Solution** :
```bash
git push
```
Lance manuellement pour voir l'erreur exacte

---

## 📊 Statistiques

Le manager affiche en permanence :
- **Articles publiés** : Nombre total d'articles sur le blog
- **Dernier article** : Titre du dernier article publié
- **Questions disponibles** : Combien il reste de questions non traitées

---

## 🎯 Astuces pro

### 1. Prépare plusieurs articles d'avance

Tu peux lancer l'option 1-2 plusieurs fois pour générer des articles, puis les publier progressivement.

### 2. Vérifie avant de publier

L'option 3 te demande confirmation avant de publier. Profites-en pour relire rapidement.

### 3. Sauvegarde ton travail

Même si tu fermes le manager, tes fichiers temporaires restent. Tu peux continuer plus tard !

---

## 🚀 Évolution future

Quand ton blog génère des revenus, tu pourras :

- **Automatisation complète** : Le script appelle l'API Claude automatiquement (0 intervention)
- **Planification** : Programme les articles à l'avance
- **Analytics** : Stats de visite intégrées
- **Multi-langues** : Articles en FR + EN automatiquement

---

**Le manager rend la gestion de ton blog ULTRA simple !**

**Utilise l'option 6 tous les jours et c'est parti ! 🎉**
