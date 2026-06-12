import pandas as pd
import random
from datetime import datetime, timedelta

def generate_data(days=7):
    data = []
    start_time = datetime.now()

    for i in range(days * 24):
        timestamp = start_time + timedelta(hours=i)
        voltage = 230
        current = round(random.uniform(0.5, 8.0), 2)
        power = round(voltage * current, 2)

        data.append([timestamp, voltage, current, power])

    df = pd.DataFrame(data, columns=["Timestamp", "Voltage", "Current", "Power"])
    df.to_csv("data/energy_data.csv", index=False)
    print("Data generated successfully!")

if __name__ == "__main__":
    generate_data()