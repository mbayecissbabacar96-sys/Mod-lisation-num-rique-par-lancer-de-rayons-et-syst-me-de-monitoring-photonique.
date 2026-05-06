# 🔬 Simulation d'un Système Optique par Lancer de Rayons
**Projet de Modélisation Numérique — Master 2 Physique Appliquée**

Ce projet propose une modélisation numérique d’un système optique basé sur le **lancer de rayons** (ray tracing). [cite_start]Il permet de simuler la propagation de rayons lumineux à travers une lentille mince, d'analyser le phénomène de focalisation et d'étudier les performances du système selon différents paramètres[cite: 3, 7, 8].

---

## 🎯 Objectifs
[cite_start]L'objectif principal est de comprendre et visualiser le comportement d'un faisceau lumineux en fonction des paramètres optiques[cite: 8]:
* [cite_start]**Simuler** la propagation rectiligne des rayons lumineux[cite: 12].
* [cite_start]**Modéliser** numériquement l'effet d'une lentille mince[cite: 13].
* [cite_start]**Visualiser** la formation du foyer et la focalisation du faisceau[cite: 14].
* [cite_start]**Étudier** l'influence de la distance focale ($f$) sur la qualité du système[cite: 15].

---

## 🧠 Principes Physiques
[cite_start]Le projet repose sur l'approximation de l'**optique géométrique**[cite: 9, 18]. [cite_start]La lumière est représentée par des rayons rectilignes dont la direction est modifiée par la lentille selon la relation[cite: 20, 24, 25]:

$$\theta' = \theta - \frac{y}{f}$$

Où :
* [cite_start]$\theta$ : angle incident du rayon[cite: 27].
* [cite_start]$y$ : hauteur du rayon à l'impact sur la lentille[cite: 29].
* [cite_start]$f$ : distance focale de la lentille[cite: 30].

---

## 🛠️ Technologies & Paramètres
* [cite_start]**Stack :** Python 3 (NumPy, Matplotlib)[cite: 74, 183, 184].
* **Configuration par défaut :**
    * [cite_start]Nombre de rayons : 100[cite: 44].
    * [cite_start]Position de la lentille : $z = 10$[cite: 45].
    * [cite_start]Domaine spatial : $z \in [0, 25]$[cite: 47].

---

## 📊 Résultats & Analyse
[cite_start]La simulation permet d'observer que la distance focale influence directement la dynamique de convergence[cite: 129, 174]:
* [cite_start]**Focale faible ($f=5$)** : Convergence forte et rapide[cite: 130].
* [cite_start]**Focale élevée ($f=20$)** : Convergence lente, foyer éloigné[cite: 132].
* [cite_start]**Sensibilité** : Le système est très sensible à la distribution angulaire initiale, ce qui peut entraîner une dispersion au foyer[cite: 138, 148].



---

## 🔗 Ressources & Liens
* **📜 Documentation :**
    * [Rapport complet : Modélisation et analyse (PDF)](Optique_par_lancer_de_rayons.pdf)
* **💻 Code Source :**
    * [Script Python de simulation (main.py)](analysis.py)

---

## 🚀 Perspectives d'Amélioration
* [cite_start]Ajout des **aberrations optiques** (sphériques et chromatiques)[cite: 162].
* [cite_start]Utilisation du formalisme des **matrices ABCD**[cite: 163].
* [cite_start]Extension du modèle en **3D**[cite: 164].
* [cite_start]Intégration d'un **faisceau Gaussien** pour modéliser des lasers réels[cite: 165].

---

## 👨‍💻 Auteur
[cite_start]**Babacar Ndiaye** *Master 2 Physique Appliquée – Nanophysique & Optique Avancée* [cite: 1, 2]


