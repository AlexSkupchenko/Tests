from unittest import TestCase
from main import canal_max, stats, canal, new_geo_logs, geo_logs, new_logs, unique_ids, ids, new_ids


class TestSomething(TestCase):
    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def test_canal_max(self):
        self.assertEqual(canal_max(stats), canal)

    def test_new_geo_logs(self):
        self.assertEqual(new_geo_logs(geo_logs), new_logs)

    def test_unique_ids(self):
        self.assertEqual(unique_ids(ids), new_ids)
