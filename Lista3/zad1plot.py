import matplotlib.pyplot as plt
import numpy as np

with open("data/zad1.txt") as reader:
    n = []
    radius = []
    for line in reader.readlines():
        data = [float(s) for s in line.split()]
        n.append(data[0])
        radius.append(data[2])
    plt.loglog(n, radius)
    plt.loglog(n, np.array(n) ** 0.5, label="N^(1/2)")
    print(np.polyfit(n, radius, 1))
    print(np.polyfit(n, radius, 1))

plt.tight_layout()
plt.legend()
plt.xlabel("N")
plt.ylabel("Radius")
plt.show()