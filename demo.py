import os, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures", exist_ok=True); os.makedirs("results", exist_ok=True)
rng = np.random.default_rng(0)
data = rng.lognormal(3, 0.6, 200)              # a skewed sample
B = 5000
means = np.array([rng.choice(data, data.size, replace=True).mean() for _ in range(B)])
lo, hi = np.percentile(means, [2.5, 97.5])
se = data.std(ddof=1) / np.sqrt(data.size)
nlo, nhi = data.mean() - 1.96*se, data.mean() + 1.96*se
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].hist(data, bins=30, color="#4C72B0"); ax[0].set_title("Skewed sample (n=200)"); ax[0].set_xlabel("value")
ax[1].hist(means, bins=40, color="#55A868")
ax[1].axvline(lo, c="k", ls="--"); ax[1].axvline(hi, c="k", ls="--", label=f"95% bootstrap CI [{lo:.1f}, {hi:.1f}]")
ax[1].axvline(nlo, c="#C44E52", ls=":"); ax[1].axvline(nhi, c="#C44E52", ls=":", label=f"normal-approx [{nlo:.1f}, {nhi:.1f}]")
ax[1].set_title("Bootstrap distribution of the mean"); ax[1].set_xlabel("resampled mean"); ax[1].legend(fontsize=8)
fig.suptitle("Bootstrap confidence interval (demo data)"); fig.tight_layout(); fig.savefig("figures/demo.png", dpi=150)
open("results/summary.csv", "w").write(f"estimate,{data.mean():.3f}\nci_low,{lo:.3f}\nci_high,{hi:.3f}\n")
print(f"mean={data.mean():.2f} 95% CI=[{lo:.2f},{hi:.2f}]"); print("ok")
