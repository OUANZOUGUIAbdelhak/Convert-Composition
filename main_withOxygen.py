import pandas as pd

oxide_conversion = {
    'AL2O3': {'Al': (2 * 26.9815385) / 101.961276, 'O': (3 * 15.999) / 101.961276},
    'B2O3':  {'B': (2 * 10.81) / 69.620, 'O': (3 * 15.999) / 69.620},
    'BAO':   {'Ba': 137.327 / 153.326, 'O': 15.999 / 153.326},
    'CAO':   {'Ca': 40.078 / 56.077, 'O': 15.999 / 56.077},
    'FE2O3': {'Fe': (2 * 55.845) / 159.687, 'O': (3 * 15.999) / 159.687},
    'K2O':   {'K': (2 * 39.0983) / 94.196, 'O': 15.999 / 94.196},
    'LI2O':  {'Li': (2 * 6.94) / 29.881, 'O': 15.999 / 29.881},
    'MGO':   {'Mg': 24.305 / 40.304, 'O': 15.999 / 40.304},
    'NA2O':  {'Na': (2 * 22.989769) / 61.979, 'O': 15.999 / 61.979},
    'SIO2':  {'Si': 28.0855 / 60.084, 'O': (2 * 15.999) / 60.084},
    'SRO':   {'Sr': 87.62 / 103.62, 'O': 15.999 / 103.62},
    'ZRO2':  {'Zr': 91.224 / 123.218, 'O': (2 * 15.999) / 123.218}
}

# Alias FEMON to FE2O3
oxide_conversion['FEMON'] = oxide_conversion['FE2O3']

input_file = '/home/intra.cea.fr/ao280403/Bureau/documents_bd_finale/Convert Composition/SciGK-density data-vérifiée.csv'
df = pd.read_csv(input_file)

# Ensure column names are uppercase for matching
columns_upper = {col.upper(): col for col in df.columns}
df.columns = [col.upper() for col in df.columns]

# Compute elemental contributions
element_totals = {}
for oxide, elements in oxide_conversion.items():
    if oxide in df.columns:
        for element, factor in elements.items():
            key = f'{element}_calc'
            if key not in element_totals:
                element_totals[key] = df[oxide] * factor
            else:
                element_totals[key] += df[oxide] * factor

# Assign elemental totals back to dataframe
for element_calc, series in element_totals.items():
    df[element_calc] = series

# Determine columns to keep (excluding oxide names)
oxide_columns = list(oxide_conversion.keys())
element_columns = list(element_totals.keys())
composition_columns = [col for col in df.columns if col not in oxide_columns and col not in element_columns]

# Rebuild final dataframe
df_elements = df[composition_columns + element_columns]

# Save result
df_elements.to_csv('converted_elements.csv', index=False)
df_elements.to_excel('converted_elements.xlsx', index=False)

print("✅ Conversion complete. Files saved as 'converted_elements.csv' and 'converted_elements.xlsx'.")