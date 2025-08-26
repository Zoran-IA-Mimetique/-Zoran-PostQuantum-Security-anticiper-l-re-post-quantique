# Zoran-Eco-Metrics — Sobriété énergétique exécutable

## 🌍 Contexte
Les IA sont souvent critiquées pour leur **coût énergétique**.  
Zoran aSiM intègre la sobriété comme **garde-fou technique**, auditable et reproductible.  

## ⚙️ Fonctionnement
- Mesure CPU via `time.process_time()`.  
- Mesure RAM via `resource` (RSS en Mo).  
- Définition de seuils (`cpu`, `ram`).  
- Déclenchement rollback Eco-ΔM11.3 si un seuil est franchi.  
- Audit log JSON (`logs/eco_log.json`).  

## 📜 Exemple
```json
{
  "cpu_time": 2.01,
  "ram_usage_mb": 520,
  "thresholds": {"cpu": 1.0, "ram": 512},
  "rollback_triggered": true
}
```

## 🧪 Démonstration
`demo.py` illustre :  
- un calcul simple (CPU < seuil),  
- un calcul intensif simulé → rollback Eco-ΔM11.3.  

## 📊 Objectifs
- Intégrer **l’écologie dans la gouvernance de l’IA**.  
- Fournir aux régulateurs une preuve exécutable.  
- Faire de Zoran une IA responsable, auditable et durable.
