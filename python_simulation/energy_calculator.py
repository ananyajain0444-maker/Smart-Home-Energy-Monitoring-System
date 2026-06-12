import pandas as pd

def calculate_energy(file="data/energy_data.csv"):
    df = pd.read_csv(file)

    # Energy in kWh
    df["Energy_kWh"] = (df["Power"] / 1000)

    total_energy = df["Energy_kWh"].sum()

    print(f"Total Energy Consumption: {total_energy:.2f} kWh")
    return df, total_energy

if __name__ == "__main__":
    calculate_energy()