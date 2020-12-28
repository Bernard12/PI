from collections import OrderedDict

class Cache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.innerCache = OrderedDict({})

    def get(self, key: str) -> str:
        if key in self.innerCache:
            self._move_key_to_front(key)
            return self.innerCache[key]
        return ''

    def _move_key_to_front(self, key):
        if not key in self.innerCache:
            return
        val = self.innerCache[key]
        del self.innerCache[key]
        self.innerCache[key] = val

    def set(self, key: str, value: str) -> None:
        keys = list(self.innerCache.keys())

        if len(keys) == self.capacity:
            last_key = keys[0]
            del self.innerCache[last_key]

        self.innerCache[key] = value

    def rem(self, key: str) -> None:
        del self.innerCache[key]
