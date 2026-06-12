from python_simulation.data_generator import generate_data
from python_simulation.energy_calculator import calculate_energy
from python_simulation.cost_estimator import estimate_cost
from python_simulation.alert_system import check_alert
from python_simulation.report_generator import generate_pdf_report
from python_simulation.visualizer import generate_plots

import pandas as pd

# STEP 1: Generate data
generate_data()

# STEP 2: Calculate energy
df, total_energy = calculate_energy()

# STEP 3: Cost estimation
cost = estimate_cost(total_energy)

# STEP 4: Alerts
df["Alert"] = df["Power"].apply(check_alert)

# STEP 5: Save processed data
df.to_csv("outputs/energy_report.csv", index=False)

# STEP 6: PDF Report
generate_pdf_report(df)

# STEP 7: ALL IMAGES (FIXED)
generate_plots()

print("\n✅ PROJECT COMPLETED SUCCESSFULLY 🚀")
print("📊 Check /images folder for ALL charts")