import matplotlib.pyplot as plt

years = [2019, 2020, 2021, 2022, 2023, 2024]
revenue_billions = [125.8, 143.0, 168.1, 198.3, 211.9, 245.1]

growth_rates = []
for i in range(1, len(revenue_billions)):
    growth = ((revenue_billions[i] - revenue_billions[i - 1]) / revenue_billions[i - 1]) * 100
    growth_rates.append(round(growth, 1))

growth_years = ["2020", "2021", "2022", "2023", "2024"]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].bar(years, revenue_billions, color="#4f81bd")
axes[0].set_title("Microsoft annual revenue")
axes[0].set_xlabel("Fiscal year")
axes[0].set_ylabel("Revenue (USD billions)")
axes[0].grid(axis="y", linestyle="--", alpha=0.3)

for year, value in zip(years, revenue_billions):
    axes[0].text(year, value + 4, f"{value}", ha="center", va="bottom", fontsize=9)

axes[1].plot(growth_years, growth_rates, marker="o", color="#c0504d", linewidth=2)
axes[1].set_title("Year-over-year revenue growth")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Growth (%)")
axes[1].grid(axis="y", linestyle="--", alpha=0.3)

for year, value in zip(growth_years, growth_rates):
    axes[1].text(year, value + 0.5, f"{value}%", ha="center", va="bottom", fontsize=9)

plt.suptitle("Microsoft revenue dashboard", fontsize=18, fontweight="bold")
plt.tight_layout()
plt.show()
