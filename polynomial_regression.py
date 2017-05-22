# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)
tempsChargementPages = np.random.normal(3.0, 1.0, 1000)
montantAchat = np.random.normal(50.0, 10.0, 1000) / (tempsChargementPages * tempsChargementPages)

axes = plt.axes()
axes.grid()
plt.xlabel('temps de chargement en secondes')
plt.ylabel('montant des achats euros')
plt.scatter(tempsChargementPages, montantAchat)
plt.show()

x = np.array(tempsChargementPages)
y = np.array(montantAchat)

p4 = np.poly1d(np.polyfit(x, y, 4))

xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')
plt.show()