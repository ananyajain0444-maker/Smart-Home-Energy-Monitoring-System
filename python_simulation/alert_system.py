def check_alert(power):
    if power > 1500:
        return "⚠ HIGH POWER USAGE DETECTED"
    elif power > 800:
        return "⚡ Medium usage"
    else:
        return "✅ Normal usage"