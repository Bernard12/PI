class Cache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = 10
        self.innerCache = {}

    def get(self, key: str) -> str:
        if key in self.innerCache:
            return self.innerCache[key]
        return ''

    def set(self, key: str, value: str) -> None:
        self.innerCache[key] = value

    def rem(self, key: str) -> None:
        del self.innerCache[key]