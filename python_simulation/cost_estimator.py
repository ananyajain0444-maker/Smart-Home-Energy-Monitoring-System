def estimate_cost(energy_kwh, rate_per_kwh=8):
    cost = energy_kwh * rate_per_kwh

    print(f"Estimated Cost: ₹{cost:.2f}")
    return cost