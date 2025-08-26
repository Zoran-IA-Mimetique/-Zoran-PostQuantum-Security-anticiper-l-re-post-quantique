# Zoran-Eco-Metrics

**Eco-Metrics** est la brique de Zoran aSiM dédiée à la **sobriété énergétique**.  
Elle mesure l’empreinte CPU, RAM et durée d’exécution, et déclenche un **rollback Eco-ΔM11.3** si un seuil est dépassé.  

## 🚀 Fonctionnalités
- Mesure CPU (temps utilisateur/système).  
- Mesure RAM (RSS, mémoire en Mo).  
- TTL énergétique configurable.  
- Audit log (`eco_log.json`).  
- Démonstration reproductible (`demo.py`).  

## 📖 Démonstration
```bash
python demo.py
```

## 📜 Exemple de log
```json
{
  "cpu_time": 0.123,
  "ram_usage_mb": 42,
  "thresholds": {"cpu": 1.0, "ram": 256},
  "rollback_triggered": false
}
```

## 🔗 Liens associés
- White Paper : *“Eco-ΔM11.3: Toward Sustainable Mimetic AI”* (à paraître).  
- Contact : tabary01@gmail.com  

## 📄 Licence
MIT — usage libre.  
© 2025, Frédéric Tabary — Projet Zoran aSiM
