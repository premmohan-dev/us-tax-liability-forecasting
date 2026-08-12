"""
U.S. Tax Liability Forecasting

Author: Premsai Mohan

This analysis examines historical U.S. tax liability data from 
1990-2023 and uses a linear regression model to forecast 
future tax liability through 2033.
"""

# =====================================================
# Imports
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# =====================================================
# Load Dataset
# =====================================================

tax_data = xl("A1:B35", headers=True)

# =====================================================
# Research Question 1
# How has total U.S. tax liability changed between
# 1990 and 2023?
# =====================================================

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    tax_data["Year"],
    tax_data["Tax Liability Amount"],
    marker="o"
)

plt.title("Total U.S. Tax Liability (1990-2023)")
plt.xlabel("Year")
plt.ylabel("Tax Liability (Thousands of Dollars)")

plt.tight_layout()
plt.show()

# =====================================================
# Research Question 2
# What do the descriptive statistics reveal about
# historical U.S. tax liability?
# =====================================================

descriptive_stats = tax_data["Tax Liability Amount"].describe()

print("\nResearch Question 2: Descriptive Statistics")
print(descriptive_stats)

# =====================================================
# Research Question 3
# What does a forecasting model predict for future
# U.S. tax liability?
# =====================================================

X = tax_data[["Year"]]
y = tax_data["Tax Liability Amount"]

model = LinearRegression()
model.fit(X, y)

future_years = pd.DataFrame({
    "Year": [2024, 2025, 2026, 2027, 2028,
             2029, 2030, 2031, 2032, 2033]
})

predictions = model.predict(future_years)

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    tax_data["Year"],
    tax_data["Tax Liability Amount"],
    label="Historical",
    marker="o"
)

ax.plot(
    future_years["Year"],
    predictions,
    label="Forecast",
    linestyle="--",
    marker="o"
)

plt.title("Historical and Forecasted U.S. Tax Liability")
plt.xlabel("Year")
plt.ylabel("Tax Liability (Thousands of Dollars)")
plt.legend()

plt.tight_layout()
plt.show()

# =====================================================
# Research Question 4
# How closely do forecasted values follow
# historical trends?
# =====================================================

forecast = future_years.copy()
forecast["Predicted Tax Liability"] = predictions

print("\nResearch Question 4: Forecast Table")
print(forecast)
