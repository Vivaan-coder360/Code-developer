import matplotlib.pyplot as plt
years = [1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 ]
popularity = [0, 10000000, 3000000, 21000000, 1000000000, 1500000000, 2000000000, 2500000000, 3000000000]
comparitive_os = ["windows", "macos", "lunix", "other"]
users = [3000000000, 100000000, 50000000, 300000000]
figs, axs = plt.subplots(1, 3, figsize = (15, 5))
axs[0].bar(years, popularity, width=5)
axs[0].set_title("Popularity of Microsoft over the years", fontsize=16)
axs[0].set_xlabel("years")
axs[0].set_ylabel("users")
axs[1].plot(years, popularity, color="blue", marker='o')
axs[1].set_title("Popularity growth", fontsize=16)
axs[1].set_xlabel("years")
axs[1].set_ylabel("users")
axs[2].pie(users, labels=comparitive_os, autopct="%.2f%%")
axs[2].set_title("Global internet users using os", fontsize=16)
plt.suptitle("Microsoft popularity history", fontsize=18, fontweight='bold')
plt.show()