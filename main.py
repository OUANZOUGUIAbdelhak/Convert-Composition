import pandas as pd

# Oxide to Element Conversion Factors (oxide wt% to element wt%)
# Source: Atomic weights & molar masses
oxide_conversion = {
    'Al2O3': {'Al': (2 * 26.9815385) / 101.961276},
    'B2O3':  {'B': (2 * 10.81) / 69.620},
    'BaO':   {'Ba': 137.327 / 153.326},
    'CaO':   {'Ca': 40.078 / 56.077},
    'Fe2O3': {'Fe': (2 * 55.845) / 159.687},
    'K2O':   {'K': (2 * 39.0983) / 94.196},
    'Li2O':  {'Li': (2 * 6.94) / 29.881},
    'MgO':   {'Mg': 24.305 / 40.304},
    'Na2O':  {'Na': (2 * 22.989769) / 61.979},
    'SiO2':  {'Si': 28.0855 / 60.084},
    'SrO':   {'Sr': 87.62 / 103.62},
    'ZrO2':  {'Zr': 91.224 / 123.218}
}

# Read the input CSV
input_file = '/home/intra.cea.fr/ao280403/Bureau/documents_bd_finale/Convert Composition/Data.csv'
df = pd.read_csv(input_file)

# Create new columns for elements
for oxide, elements in oxide_conversion.items():
    if oxide in df.columns:
        for element, factor in elements.items():
            df[element] = df.get(element, 0) + df[oxide] * factor

# Optional: drop original oxide columns
oxide_columns = list(oxide_conversion.keys())
composition_columns = [col for col in df.columns if col not in oxide_columns]

# Create new DataFrame with required columns (you can customize this)
df_elements = df[composition_columns + list({el for v in oxide_conversion.values() for el in v})]

# Save to new CSV and Excel files
df_elements.to_csv('converted_elements.csv', index=False)
df_elements.to_excel('converted_elements.xlsx', index=False)

print("Conversion complete. Files saved as 'converted_elements.csv' and 'converted_elements.xlsx'.")
