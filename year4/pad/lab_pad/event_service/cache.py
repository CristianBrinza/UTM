import threading

class LRUCache:
    def __init__(self, capacity=100):
        self.cache = {}
        self.order = []
        self.capacity = capacity
        self.lock = threading.Lock()

    def get(self, key):
        with self.lock:
            if key in self.cache:
                self.order.remove(key)
                self.order.insert(0, key)
                return self.cache[key]
            return None

    def put(self, key, value):
        with self.lock:
            if key in self.cache:
                self.order.remove(key)
            elif len(self.cache) >= self.capacity:
                old_key = self.order.pop()
                del self.cache[old_key]
            self.cache[key] = value
            self.order.insert(0, key)
