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

    def test_capacity(self):
        cache = Cache(2)

        cache.set('1', 'a')
        cache.set('2', 'b')

        self.assertEqual(cache.get('1'), 'a')
        cache.set('3', 'c')
        self.assertEqual(cache.get('1'), '')
        self.assertEqual(cache.get('3'), 'c')


if __name__ == '__main__':
    unittest.main()
