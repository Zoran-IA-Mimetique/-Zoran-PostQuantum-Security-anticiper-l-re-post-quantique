from eco_metrics import measure

if __name__ == "__main__":
    print("--- Scenario 1: Normal load ---")
    print(measure(threshold_cpu=1.0, threshold_ram=512))

    print("--- Scenario 2: Tight thresholds ---")
    print(measure(threshold_cpu=0.0001, threshold_ram=1))
