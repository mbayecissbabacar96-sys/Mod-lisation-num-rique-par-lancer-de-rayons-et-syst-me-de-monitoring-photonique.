# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:15:09 2026

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt

# =========================
# PARAMÈTRES GÉNÉRAUX
# =========================
n_rays = 100
z_lens = 10
z_max = 25
z = np.linspace(0, z_max, 500)

y0 = np.linspace(-5, 5, n_rays)
theta = np.linspace(-0.1, 0.1, n_rays)

# ==========================================================
# FIGURE 1 : TRAJECTOIRES DES RAYONS (f = 10)
# ==========================================================
f = 10

plt.figure(figsize=(7,5))

for i in range(n_rays):
    y = []

    for zi in z:
        if zi < z_lens:
            yi = y0[i] + theta[i] * zi
        else:
            y_lens = y0[i] + theta[i] * z_lens
            theta_new = theta[i] - y_lens / f
            yi = y_lens + theta_new * (zi - z_lens)

        y.append(yi)

    plt.plot(z, y, linewidth=0.5)

plt.axvline(z_lens, linestyle='--', label="Lentille")
plt.title("Figure 1 : Propagation des rayons lumineux")
plt.xlabel("z")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()


# ==========================================================
# FIGURE 2 : ZOOM FOYER
# ==========================================================
f = 10

plt.figure(figsize=(7,5))

for i in range(n_rays):
    y = []

    for zi in z:
        if zi < z_lens:
            yi = y0[i] + theta[i] * zi
        else:
            y_lens = y0[i] + theta[i] * z_lens
            theta_new = theta[i] - y_lens / f
            yi = y_lens + theta_new * (zi - z_lens)

        y.append(yi)

    plt.plot(z, y, linewidth=0.5)

plt.axvline(z_lens, linestyle='--')
plt.xlim(8, 15)
plt.ylim(-2, 2)
plt.title("Figure 2 : Zoom sur la zone de focalisation")
plt.xlabel("z")
plt.ylabel("y")
plt.grid()
plt.show()


# ==========================================================
# FIGURE 3 : INFLUENCE DE LA FOCALE
# ==========================================================
f_values = [5, 10, 20]

plt.figure(figsize=(7,5))

for f in f_values:

    for i in range(0, n_rays, 5):  # moins de rayons pour lisibilité
        y = []

        for zi in z:
            if zi < z_lens:
                yi = y0[i] + theta[i] * zi
            else:
                y_lens = y0[i] + theta[i] * z_lens
                theta_new = theta[i] - y_lens / f
                yi = y_lens + theta_new * (zi - z_lens)

            y.append(yi)

        plt.plot(z, y, linewidth=0.5, label=f"f={f}" if i == 0 else "")

plt.axvline(z_lens, linestyle='--')
plt.title("Figure 3 : Influence de la distance focale")
plt.xlabel("z")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()