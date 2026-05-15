# Prompt : Calculateur TJM vers Revenu Net Mensuel (Micro-Entrepreneur)

## Objectif
Créer une page HTML unique qui calcule le **revenu mensuel net après impôt** pour un micro-entrepreneur français (BNC - services), à partir de son taux journalier moyen (TJM).

## Entrées (Inputs)
1. **TJM (Taux Journalier Moyen)** : champ numérique, défaut = 600 €
2. **Nombre de jours travaillés par mois (moyenne)** : champ numérique, défaut = 20
3. **Première année (bénéfice ACRE)** : bouton radio — « Première année (ACRE) » ou « Pas première année »
4. **Parts fiscales du foyer** : valeurs sélectionnables : 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5

## Hypothèses
- Le freelance est **micro-entrepreneur** dans la catégorie **« Autres prestations de services » (BNC)**
- Le seul revenu du foyer provient de cette activité freelance (les autres ne travaillent pas)
- Taux applicables : année 2026

## Étapes de Calcul

### Étape 1 : Chiffre d'Affaires Annuel (CA)
- CA = TJM × jours/mois × 12

### Étape 2 : Cotisations Sociales
- **Sans ACRE** : 25,6% du CA
- **Avec ACRE (première année)** : 12,8% du CA (réduction de 50%)
- **CFP (Contribution à la Formation Professionnelle)** : 0,2% du CA
- Total charges = Cotisations sociales + CFP

### Étape 3 : Revenu Net Imposable
- Pour les micro-BNC, un **abattement forfaitaire de 34%** s'applique (minimum 305€)
- Revenu net imposable = CA × (1 - 34%) = CA × 66%

### Étape 4 : Calcul de l'Impôt sur le Revenu (Barème 2026 sur revenus 2025)
1. Diviser le revenu net imposable par le nombre de parts (quotient familial)
2. Appliquer le barème progressif :
   - Jusqu'à 11 600€ : 0%
   - De 11 601€ à 29 579€ : 11%
   - De 29 580€ à 84 577€ : 30%
   - De 84 578€ à 181 917€ : 41%
   - Au-delà de 181 917€ : 45%
3. Multiplier le résultat par le nombre de parts

### Étape 5 : Décote (pour revenus modestes)
- Célibataire (1 part) : si impôt brut ≤ 1 982€ → décote = 897 - 45,25% × impôt brut
- Couple (≥ 2 parts) : si impôt brut ≤ 3 277€ → décote = 1 483 - 45,25% × impôt brut
- La décote ne peut pas être négative

### Étape 6 : Revenu Net Mensuel Final
- Net annuel = CA - Total charges - Impôt après décote
- Net mensuel = Net annuel / 12

## Exigences d'Affichage
- Afficher **toutes les formules et détails de calcul intermédiaires** à chaque étape pour que l'utilisateur puisse vérifier
- Thème clair (pas sombre)
- Calculer au chargement de la page (onload)
- Recalculer à chaque modification d'un input

## Fonctionnalités Supplémentaires
- Bouton **Export CSV** : séparateur = « ; », décimale = « . », encodage = UTF-8
- **LocalStorage** : sauvegarder toutes les valeurs d'entrée pour qu'elles persistent à la prochaine visite

## Sources de Données
- Taux de cotisations sociales : economie.gouv.fr (2026)
- Taux ACRE : service-public.fr
- Barème impôt sur le revenu : economie.gouv.fr (Loi de finances 2026)
