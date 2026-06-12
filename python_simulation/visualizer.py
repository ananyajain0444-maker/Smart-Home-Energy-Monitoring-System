import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_plots(file="data/energy_data.csv"):
    df = pd.read_csv(file)

    os.makedirs("images", exist_ok=True)

    # -----------------------------------
    # 1. Dashboard Preview (Power trend)
    # -----------------------------------
    plt.figure(figsize=(6,4))
    plt.plot(df["Power"], color="blue")
    plt.title("Dashboard Preview - Power Trend")
    plt.xlabel("Time Steps")
    plt.ylabel("Power (W)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("images/dashboard_preview.png")
    plt.close()

    # -----------------------------------
    # 2. Energy Usage Chart
    # -----------------------------------
    plt.figure(figsize=(6,4))
    plt.plot(df["Power"], marker='o', color="green")
    plt.title("Energy Usage Chart")
    plt.xlabel("Time Steps")
    plt.ylabel("Power (W)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("images/energy_usage_chart.png")
    plt.close()

    # -----------------------------------
    # 3. Monthly Cost Chart (FIXED)
    # -----------------------------------
    total_energy_kwh = df["Power"].sum() / 1000
    rate = 8  # ₹ per kWh
    monthly_cost = total_energy_kwh * rate

    plt.figure(figsize=(4,4))
    plt.bar(["Energy Cost"], [monthly_cost], color="orange")
    plt.title("Monthly Cost Estimation")
    plt.ylabel("Cost (₹)")
    plt.tight_layout()
    plt.savefig("images/monthly_cost_chart.png")
    plt.close()

    # -----------------------------------
    # 4. Alert Notification Chart
    # -----------------------------------
    alerts = df["Power"].apply(lambda x: "High" if x > 1500 else "Normal").value_counts()

    plt.figure(figsize=(4,4))
    plt.bar(alerts.index, alerts.values, color="red")
    plt.title("Alert Notifications")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("images/alert_notification.png")
    plt.close()

    # -----------------------------------
    # 5. PDF Report Preview (FIXED VISUAL)
    # -----------------------------------
    plt.figure(figsize=(6,3))
    plt.axis("off")

    text = f"""SMART HOME ENERGY REPORT

Total Power Entries: {len(df)}
Total Energy (kWh): {total_energy_kwh:.2f}
Estimated Monthly Cost: ₹{monthly_cost:.2f}

Status: Report Generated Successfully
"""

    plt.text(0.05, 0.5, text, fontsize=10, family="monospace")
    plt.savefig("images/pdf_report_preview.png")
    plt.close()

    print("✅ ALL 5 IMAGES GENERATED SUCCESSFULLY")