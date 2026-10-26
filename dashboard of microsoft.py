import matplotlib.pyplot as plt

years = [2019, 2020, 2021, 2022, 2023, 2024]
revenue_billions = [125.8, 143.0, 168.1, 198.3, 211.9, 245.1]
revenue_growth = []

for index in range(1, len(revenue_billions)):
    growth = ((revenue_billions[index] - revenue_billions[index - 1]) / revenue_billions[index - 1]) * 100
    revenue_growth.append(round(growth, 1))

revenue_growth_labels = ["2020", "2021", "2022", "2023", "2024"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.bar(years, revenue_billions, color="#4f81bd")
ax1.set_title("Microsoft annual revenue (official annual reports)", fontsize=14)
ax1.set_xlabel("Fiscal year")
ax1.set_ylabel("Revenue (USD billions)")
ax1.grid(axis="y", linestyle="--", alpha=0.3)

for year, value in zip(years, revenue_billions):
    ax1.text(year, value + 4, f"{value}", ha="center", va="bottom", fontsize=9)

ax2.plot(revenue_growth_labels, revenue_growth, marker="o", color="#c0504d", linewidth=2)
ax2.set_title("Year-over-year revenue growth", fontsize=14)
ax2.set_xlabel("Year")
ax2.set_ylabel("Growth (%)")
ax2.grid(axis="y", linestyle="--", alpha=0.3)

for label, value in zip(revenue_growth_labels, revenue_growth):
    ax2.text(label, value + 0.5, f"{value}%", ha="center", va="bottom", fontsize=9)

plt.suptitle("Microsoft revenue dashboard", fontsize=18, fontweight="bold")
plt.tight_layout()
plt.show()
