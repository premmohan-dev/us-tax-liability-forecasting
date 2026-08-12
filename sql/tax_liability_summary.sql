SELECT
    AVG([Tax Liability Amount]) AS AverageTaxLiability,
    MIN([Tax Liability Amount]) AS MinimumTaxLiability,
    MAX([Tax Liability Amount]) AS MaximumTaxLiability
FROM TaxLiability;
