# U.S. Tax Liability Forecasting

## Overview

This analysis examines IRS Statistics of Income (SOI) data from 1990 through 2023 to better understand how U.S. tax liability has changed over time. Historical tax return data is used to identify long-term trends and estimate future tax liability based on past patterns.

## Objectives

The objectives of this analysis are to:
- Examine historical trends in U.S. tax liability between 1990 and 2023.
- Measure how tax liability has changed over time.
- Develop a forecasting model based on historical IRS data.
- Estimate future tax liability using historical trends.
- Interpret forecast results and discuss factors that may affect model accuracy.

## Dataset

Source: Internal Revenue Service (IRS) Statistics of Income (SOI)

Publication: SOI Tax Stats - Individual income tax returns complete report (Publication 1304)

Table: Selected income and tax items for selected years (in current and constant dollars)

Tax Years: 1990-2023

> **Note:** Amounts are reported in thousands of dollars, as provided in the IRS dataset.

## Research Questions

1. How has total U.S. tax liability changed between 1990 and 2023?
2. What do the descriptive statistics reveal about historical U.S. tax liability?
3. What does a forecasting model predict for future tax liability?
4. How closely do forecasted values follow historical trends?

## Research Question 1

### How has total U.S. tax liability changed between 1990 and 2023?

<img width="1179" height="590" alt="historical tax liability" src="https://github.com/user-attachments/assets/6ec2a6ba-9e20-4984-b3b8-0b2588540d7b" />

### Key Findings

U.S. tax liability generally increased between 1990 and 2023. While there were a few periods of decline, the overall trend was upward, with the largest growth occurring after 2009. Tax liability reached its highest level in 2021 and remained near that level through 2023. These results suggest that the amount of tax owed by U.S. taxpayers has grown substantially over the past three decades.

## Research Question 2

### What do the descriptive statistics reveal about historical U.S. tax liability?

| Statistic | Value |
|------------|------------:|
| Count | 34 |
| Mean | 1,150,979,103 |
| Standard Deviation | 521,919,676 |
| Minimum | 470,909,018 |
| Median | 1,037,071,749 |
| Maximum | 2,385,860,259 |

### Key Findings

U.S. tax liability changed substantially between 1990 and 2023. Over the 34-year period, tax liability ranged from approximately 471 million to 2.39 billion (reported in thousands of dollars), with an average value of about 1.15 billion. The higher average and maximum values reflect the strong growth in tax liability seen in recent years. Overall, the descriptive statistics support the upward trend shown in the historical data.

## Research Question 3

### What does a forecasting model predict for future U.S. tax liability?

<img width="1190" height="590" alt="tax liability forecast" src="https://github.com/user-attachments/assets/b7b6e50d-4b37-42c9-a078-bc0e6e127353" />

### Key Findings

The forecasting model predicts that U.S. tax liability will continue to increase through 2033. Tax liability is projected to rise from approximately 2.02 billion in 2024 to 2.46 billion in 2033 (reported in thousands of dollars). Based on historical trends, the model suggests continued growth throughout the forecast period.

## Research Question 4

### How closely do forecasted values follow historical trends?

| Year | Predicted Tax Liability |
|------|------------------------:|
| 2024 | 2,015,433,839 |
| 2025 | 2,064,831,253 |
| 2026 | 2,114,228,666 |
| 2027 | 2,163,626,080 |
| 2028 | 2,213,023,493 |
| 2029 | 2,262,420,907 |
| 2030 | 2,311,818,320 |
| 2031 | 2,361,215,734 |
| 2032 | 2,410,613,147 |
| 2033 | 2,460,010,560 |

### Key Findings

The forecast follows the same overall trend as the historical data and suggests continued growth in U.S. tax liability. While the model provides a reasonable estimate based on past trends, future tax liability could be affected by economic conditions, inflation, changes in income levels, and future tax law changes.

## Methods

- Data preparation and cleaning
- SQL-based data extraction
- Descriptive statistical analysis
- Forecast modeling
- Data visualization

## Tools and Technologies

- SQL
- Python
- Pandas
- Matplotlib
- Microsoft Access
- Microsoft Excel
- GitHub

## How to Use This Project

1. Download the IRS Statistics of Income (SOI) dataset (`23intaba.xls`) included in the `data` folder.
2. Use the cleaned `tax_liability_1990_2023.xlsx` dataset for analysis and forecasting.
3. Import the dataset into Microsoft Access and run the SQL queries in the `sql` folder to retrieve and summarize historical tax liability data.
4. Run the Python analysis in the `python` folder to generate descriptive statistics, visualizations, and forecasts.
5. Review the charts, tables, and findings to understand historical tax liability trends and forecasted values.

## Conclusion

Overall, this analysis showed a clear increase in U.S. tax liability between 1990 and 2023. The historical data showed a consistent upward trend, and the forecasting model suggests that tax liability may continue to increase through 2033. Although future tax liability could be affected by economic conditions, inflation, and changes to tax laws, this analysis demonstrates how historical data can be used to identify trends and estimate future outcomes.
