# 🔍 Choisir la source de questions

Tu as maintenant **3 scripts** pour trouver des questions Apple :

---

## 📋 Les 3 options disponibles

### 1️⃣ `find_question_simple.py` ⭐ **RECOMMANDÉ POUR COMMENCER**

**Source** : Liste de 20 questions pré-définies basées sur recherches Google

**Avantages** :
- ✅ Fonctionne immédiatement (0 configuration)
- ✅ Questions vérifiées et pertinentes
- ✅ Aucune dépendance externe
- ✅ Rapide et fiable

**Inconvénients** :
- ⚠️ Limité à 20 questions (mais tu peux en ajouter)

**Utilisation** :
```bash
python3 find_question_simple.py
```

**Quand l'utiliser** :
- Pour débuter
- Si tu veux du 100% fiable
- Pour les 3 premières semaines

---

### 2️⃣ `find_question_trends.py` 🔥 **POUR LES VRAIES TENDANCES**

**Source** : Google Trends (recherches réelles des utilisateurs)

**Avantages** :
- ✅ Questions **vraiment recherchées** en ce moment
- ✅ Toujours à jour avec les tendances
- ✅ Illimité (nouvelles questions chaque jour)
- ✅ Gratuit

**Inconvénients** :
- ⚠️ Peut ne pas trouver de questions certains jours
- ⚠️ Dépend de Google Trends (parfois lent)

**Utilisation** :
```bash
source venv/bin/activate
python3 find_question_trends.py
```

**Quand l'utiliser** :
- Après les 20 premières questions
- Si tu veux du contenu ultra-pertinent
- Pour suivre l'actualité Apple

---

### 3️⃣ `find_question.py` 📱 **AVEC REDDIT** (optionnel)

**Source** : Reddit (r/apple, r/AppleHelp, r/iphone, r/mac)

**Avantages** :
- ✅ Questions réelles d'utilisateurs
- ✅ Contexte riche (upvotes, commentaires)
- ✅ Gratuit

**Inconvénients** :
- ⚠️ Nécessite configuration Reddit API
- ⚠️ Plus complexe

**Utilisation** :
1. Configure Reddit API (voir README.md)
2. Édite `find_question.py` avec tes credentials
3. Lance : `python3 find_question.py`

**Quand l'utiliser** :
- Si tu veux diversifier les sources
- Si Reddit API fonctionne pour toi

---

## 🎯 Ma recommandation

### Semaines 1-3 : `find_question_simple.py`
- Publie les 20 questions pré-définies
- Concentre-toi sur la qualité des articles
- Observe le trafic

### Semaines 4+ : `find_question_trends.py`
- Passe aux tendances Google en temps réel
- Si pas de résultat un jour → utilise `find_question_simple.py` en backup

### Optionnel : Reddit
- Ajoute `find_question.py` si tu veux plus de diversité

---

## 🔄 Workflow quotidien adapté

**Option A : Simple (recommandé au début)**
```bash
python3 find_question_simple.py
# Copie le prompt → Claude → Copie la réponse
python3 publish_article.py
git add . && git commit -m "Article du jour" && git push
```

**Option B : Google Trends (après 3 semaines)**
```bash
source venv/bin/activate
python3 find_question_trends.py
# Si pas de résultat → python3 find_question_simple.py
# Copie le prompt → Claude → Copie la réponse
python3 publish_article.py
git add . && git commit -m "Article du jour" && git push
```

---

## 📊 Comparaison rapide

| Critère | Simple | Trends | Reddit |
|---------|--------|--------|--------|
| **Setup** | ✅ Aucun | ✅ Aucun | ⚠️ Config API |
| **Fiabilité** | ✅✅✅ | ✅✅ | ✅ |
| **Pertinence** | ✅✅ | ✅✅✅ | ✅✅ |
| **Nombre** | 20 | ♾️ Illimité | ♾️ Illimité |
| **Vitesse** | ✅✅✅ | ✅ | ✅✅ |

---

## 💡 Astuce Pro

**Combine les 3 sources !**

Crée un script `daily.sh` personnalisé :

```bash
#!/bin/bash
# Essaye d'abord Google Trends
source venv/bin/activate
python3 find_question_trends.py

# Si échec, fallback sur simple
if [ ! -f "daily_question.json" ]; then
    python3 find_question_simple.py
fi
```

---

## 🆘 Problèmes ?

**Google Trends ne trouve rien** :
- Normal certains jours (données pas encore à jour)
- Solution : utilise `find_question_simple.py` ce jour-là

**Reddit ne marche pas** :
- Vérifie les credentials dans `find_question.py`
- Ou ignore Reddit et utilise les 2 autres sources

---

**Pour aujourd'hui, utilise `find_question_simple.py` - c'est le plus fiable !** 🚀
