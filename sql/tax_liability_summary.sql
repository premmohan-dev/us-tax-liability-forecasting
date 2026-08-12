-- Research Question 2
-- What do the descriptive statistics reveal about historical U.S. tax liability?
-- Purpose: Calculates summary statistics used in the descriptive analysis.

SELECT
    AVG([Tax Liability Amount]) AS AverageTaxLiability,
    MIN([Tax Liability Amount]) AS MinimumTaxLiability,
    MAX([Tax Liability Amount]) AS MaximumTaxLiability
FROM TaxLiability;
