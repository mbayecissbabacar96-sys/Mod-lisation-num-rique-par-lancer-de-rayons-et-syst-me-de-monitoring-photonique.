# 🔬 Modélisation d'un Système Optique par Lancer de Rayons
**Projet de Simulation Numérique — Master 2 Physique Appliquée**

[cite_start]Ce projet porte sur la simulation et l'analyse de la propagation de rayons lumineux à travers une **lentille mince convergente** en utilisant l'approximation de l'optique géométrique [cite: 3, 9].

---

## 🎯 Objectifs du Projet
L'étude vise à prédire le comportement de la lumière à travers plusieurs axes :
* [cite_start]**Modélisation numérique** de la trajectoire des rayons [cite: 8, 12].
* [cite_start]**Visualisation** de la formation du point focal (foyer) [cite: 8, 14].
* [cite_start]**Analyse de l'influence** de la distance focale ($f$) sur la qualité de la focalisation [cite: 8, 15].
* [cite_start]**Étude de la dispersion** du faisceau lumineux après le foyer [cite: 16].

---

## 🧠 Principes Théoriques
Le simulateur repose sur les lois fondamentales de l'optique géométrique :
1. [cite_start]**Loi de la lentille mince** : La déviation angulaire suit la formule $\theta' = \theta - \frac{y}{f}$ [cite: 24, 25].
2. **Équations de propagation** :
   - [cite_start]Avant lentille : $y(z) = y_0 + \theta z$ [cite: 33].
   - [cite_start]Après lentille : $y(z) = y_{lens} + \theta' (z - z_{lens})$ [cite: 35].



---

## 📊 Résultats & Analyse
La simulation réalisée sous **Python** met en évidence :
* [cite_start]**Convergence** : Après la lentille, une modification de la direction des rayons entraîne une convergence progressive vers une zone de focalisation [cite: 76, 77].
* [cite_start]**Puissance de la lentille** : Plus la distance focale est petite ($f=5$), plus la convergence est forte et rapide [cite: 130, 133].
* [cite_start]**Limites** : Le modèle néglige les aberrations sphériques/chromatiques ainsi que la diffraction [cite: 154, 156].

---

## 🔗 Ressources & Liens

* **📜 Rapport d'Étude :**
* **[📄 Consulter le Rapport Technique Complet (PDF)](Optique_par_lancer_de_rayons.pdf)**
* **[🐍 Voir le Code Python d'Analyse](analysis.py)**


---

## 👤 Auteur
[cite_start]**Babacar Ndiaye** [cite: 1]  
[cite_start]*Master 2 Physique Appliquée – Nanophysique et Optique Avancée* [cite: 2]

⸻
[cite_start]*Ce travail constitue une base essentielle pour la compréhension et la conception de systèmes optiques complexes[cite: 176].*
