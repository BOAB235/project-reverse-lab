# Prompt: Micro-Entrepreneur TJM to Net Monthly Income Calculator

## Objective
Create a single-page HTML calculator that computes the **net monthly income after tax** for a French micro-entrepreneur (BNC - services), given their daily rate (TJM).

## Inputs
1. **TJM (Daily Rate)**: numeric input, default = 600 €
2. **Average working days per month**: numeric input, default = 20
3. **First year (ACRE benefit)**: radio button selection — "First year (ACRE)" or "Not first year"
4. **Household tax shares (parts fiscales)**: selectable values: 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5

## Assumptions
- The freelancer is a **micro-entrepreneur** in the category **"Autres prestations de services" (BNC)**
- The only household income comes from this freelance activity (sole earner)
- Year: 2026 rates

## Calculation Steps

### Step 1: Annual Turnover (Chiffre d'Affaires)
- CA = TJM × days/month × 12

### Step 2: Social Contributions
- **Without ACRE**: 25.6% of CA
- **With ACRE (first year)**: 12.8% of CA (50% reduction)
- **CFP (Professional Training Contribution)**: 0.2% of CA
- Total charges = Social contributions + CFP

### Step 3: Net Taxable Income (Revenu Net Imposable)
- For micro-BNC, a **34% flat-rate deduction (abattement)** applies (minimum 305€)
- Revenu net imposable = CA × (1 - 34%) = CA × 66%

### Step 4: Income Tax Calculation (Barème 2026 on 2025 income)
1. Divide net taxable income by number of parts (quotient familial)
2. Apply progressive tax brackets:
   - Up to 11,600€: 0%
   - 11,601€ to 29,579€: 11%
   - 29,580€ to 84,577€: 30%
   - 84,578€ to 181,917€: 41%
   - Above 181,917€: 45%
3. Multiply result by number of parts

### Step 5: Décote (for modest incomes)
- Single (1 part): if gross tax ≤ 1,982€ → décote = 897 - 45.25% × gross tax
- Couple (≥ 2 parts): if gross tax ≤ 3,277€ → décote = 1,483 - 45.25% × gross tax
- Décote cannot be negative

### Step 6: Final Net Monthly Income
- Annual net = CA - Total charges - Income tax after décote
- Monthly net = Annual net / 12

## Display Requirements
- Show **all formulas and intermediate calculation details** at each step so the user can verify
- Light theme (not dark)
- Compute on page load (onload)
- Recompute on any input change

## Additional Features
- **CSV Export** button: separator = ";", decimal = ".", encoding = UTF-8
- **LocalStorage**: save all input values so they persist on next visit

## Data Sources
- Social contribution rates: economie.gouv.fr (2026)
- ACRE rates: service-public.fr
- Income tax brackets: economie.gouv.fr (Loi de finances 2026)
