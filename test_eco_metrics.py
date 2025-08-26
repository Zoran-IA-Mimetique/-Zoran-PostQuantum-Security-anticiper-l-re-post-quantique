import unittest
from eco_metrics import measure

class TestEcoMetrics(unittest.TestCase):
    def test_normal_load(self):
        entry = measure(threshold_cpu=1.0, threshold_ram=512)
        self.assertIn("cpu_time", entry)
        self.assertFalse(entry["rollback_triggered"])

    def test_trigger_rollback(self):
        entry = measure(threshold_cpu=0.0, threshold_ram=1)
        self.assertTrue(entry["rollback_triggered"])

if __name__ == "__main__":
    unittest.main()
