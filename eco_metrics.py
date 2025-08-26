import time, os, json, resource

LOG_FILE = "logs/eco_log.json"

def measure(threshold_cpu=1.0, threshold_ram=256):
    start = time.process_time()
    usage = resource.getrusage(resource.RUSAGE_SELF)
    ram_mb = usage.ru_maxrss / 1024

    # Simuler un calcul
    for _ in range(10**6):
        pass

    cpu_time = time.process_time() - start
    rollback = cpu_time > threshold_cpu or ram_mb > threshold_ram

    entry = {
        "cpu_time": cpu_time,
        "ram_usage_mb": ram_mb,
        "thresholds": {"cpu": threshold_cpu, "ram": threshold_ram},
        "rollback_triggered": rollback,
        "timestamp": time.time()
    }

    log_entry(entry)
    return entry

def log_entry(entry):
    entries = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            try:
                entries = json.load(f)
            except:
                entries = []
    entries.append(entry)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2)
