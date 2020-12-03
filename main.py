from src.cache.cache import Cache


if __name__ == '__main__':
    cache = Cache(100)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    cache.get('Jesse')  # вернёт 'James'
    cache.rem('Walter')
    cache.get('Walter')  # вернёт ''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
