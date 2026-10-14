import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("precios_consolas.csv")
kontsolak = ["Xbox", "PS5", "Switch"]
kolumnaGuztiak = kontsolak + ["PC"]

means = df[kolumnaGuztiak].to_numpy(dtype=float).mean(axis=0)
plt.figure(figsize=(8, 5))
bars = plt.bar(kolumnaGuztiak, means)
plt.title("Batez besteko prezioa")
plt.xlabel("Gailua")
plt.ylabel("Prezioa")
plt.grid(axis="y", alpha=0.3)
for bar, value in zip(bars, means):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f"{value:.2f}", ha="center", va="bottom")
plt.tight_layout()
plt.show()
plt.close()

kontsolaPrezioak = df[kontsolak].to_numpy(dtype=float)
pcPrezioak = df["PC"].to_numpy(dtype=float)
egunak = (pcPrezioak[:, None] > kontsolaPrezioak).sum(axis=0)
plt.figure(figsize=(8, 5))
bars = plt.bar(kontsolak, egunak)
plt.title("PC-a kontsola bakoitza baino garestiagoa izan den egunak")
plt.xlabel("Konparatutako kontsola")
plt.ylabel("Egun kopurua")
plt.grid(axis="y", alpha=0.3)
for bar, value in zip(bars, egunak):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), str(int(value)), ha="center", va="bottom")
plt.tight_layout()
plt.show()
plt.close()

zenbat = kontsolaPrezioak.min(axis=1, keepdims=True)
egunMerkeak = (kontsolaPrezioak == zenbat).sum(axis=0)
plt.figure(figsize=(8, 5))
bars = plt.bar(kontsolak, egunMerkeak)
plt.title("Kontsola bakoitza merkeena izan den egunak")
plt.xlabel("Kontsola")
plt.ylabel("Egun kopurua")
plt.grid(axis="y", alpha=0.3)
for bar, value in zip(bars, egunMerkeak):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), str(int(value)), ha="center", va="bottom")
plt.tight_layout()
plt.show()
plt.close()