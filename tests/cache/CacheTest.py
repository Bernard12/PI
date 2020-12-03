import unittest
from src.cache.cache import Cache


class CacheTestCase(unittest.TestCase):
    def test_homework1(self):
        cache = Cache(100)
        cache.set('Jesse', 'Pinkman')
        cache.set('Walter', 'White')
        cache.set('Jesse', 'James')
        self.assertEqual(cache.get('Jesse'), 'James')  # вернёт 'James'
        cache.rem('Walter')
        self.assertEqual(cache.get('Walter'), '')


if __name__ == '__main__':
    unittest.main()
