# 🧪 Oxide-to-Element Composition Converter

This Python script automates the conversion of **oxide-based chemical compositions** (e.g., `SiO2`, `Fe2O3`, etc.) into their corresponding **elemental compositions** (e.g., `Si`, `Fe`, `O`), using molecular weight ratios.

It is especially useful for **materials science**, **glass science**, and **geochemistry** workflows that require tracking of elemental contributions in complex mixtures.

---

## 📥 Input

The script reads a `.csv` file containing oxide percentages (by weight), such as:

| Sample | SIO2 | AL2O3 | FE2O3 | NA2O | ... |
|--------|------|--------|--------|-------|
| A      | 45.0 | 15.0   | 5.0    | 2.0   |

📍 **Note:** You can set your own input file by modifying the `input_file` path in the script.

---

## ⚙️ What It Does

- Maps oxide formulas to elemental ratios using molecular weights
- Converts each oxide into its elemental contributions (e.g., `SiO2` → `Si`, `O`)
- Adds new columns with calculated elemental contributions
- Exports two output files:
  - `converted_elements.csv`
  - `converted_elements.xlsx`

---

## 🧠 Supported Oxides

The script currently supports:

