# 🔬 Modélisation d'un Système Optique par Lancer de Rayons
**Projet de Simulation Numérique — Master 2 Physique Appliquée**

Ce projet porte sur la simulation et l'analyse de la propagation de rayons lumineux à travers une **lentille mince convergente** en utilisant l'approximation de l'optique géométrique.

---

## 🎯 Objectifs du Projet
L'étude vise à prédire le comportement de la lumière à travers plusieurs axes :
* **Modélisation numérique** de la trajectoire des rayons.
* **Visualisation** de la formation du point focal (foyer).
* **Analyse de l'influence** de la distance focale ($f$) sur la qualité de la focalisation.
* **Étude de la dispersion** du faisceau lumineux après le foyer.

---

## 🧠 Principes Théoriques
Le simulateur repose sur les lois fondamentales de l'optique géométrique :

1.**Loi de la lentille mince** : 
La déviation angulaire suit la formule $\theta' = \theta - \frac{y}{f}$.

2. **Équations de propagation** : 
   - Avant lentille : $y(z) = y_0 + \theta z$.
   - Après lentille : $y(z) = y_{lens} + \theta' (z - z_{lens})$.



---

## 📊 Résultats & Analyse
La simulation réalisée sous **Python** met en évidence :
* **Convergence** : Après la lentille, une modification de la direction des rayons entraîne une convergence progressive vers une zone de focalisation.
* **Puissance de la lentille** : Plus la distance focale est petite ($f=5$), plus la convergence est forte et rapide.
* **Limites** : Le modèle néglige les aberrations sphériques/chromatiques ainsi que la diffraction.

---

## 🔗 Ressources & Liens

* **📜 Rapport d'Étude :**
* **[📄 Consulter le Rapport Technique Complet (PDF)](Optique_par_lancer_de_rayons.pdf)**
* **[🐍 Voir le Code Python d'Analyse](analysis.py)**


---

## 👤 Auteur
**Babacar Ndiaye** 
*Master 2 Physique Appliquée – Nanophysique et Optique Avancée* 

⸻
*Ce travail constitue une base essentielle pour la compréhension et la conception de systèmes optiques complexes.*
