import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlp
import numpy as np
fig, ax1 = plt.subplots()
x = np.arange(0, 5, 0.1)
y1=np.sin(x)
ax1.plot(x, y1, 'orange', linestyle=":", label="sin(x)")
ax1.set_yticks(np.linspace(-1,1,9))
ax1.set_ylim(-1,1)
ax1.set_xlim(0,5)
ax1.set_title("To jest tytuł wykresu")
ax1.set_xlabel("oś dolna")
ax1.set_ylabel("oś lewa", color="darkgreen")
ax2 = ax1.twinx()
ax1.legend(loc="right")
y2 = np.cos(x)
ax2.plot(x, y2, "brown", linestyle=":", label="cos(x)")
ax2.set_yticks(np.linspace(-2,2,9))
ax2.set_ylim(-2,2)
ax2.set_ylabel("oś prawa", color="red")
ax2.legend(loc="lower center")
fig.tight_layout()
plt.savefig('wykres1.jpg')
plt.show()


