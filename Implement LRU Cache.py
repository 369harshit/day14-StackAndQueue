from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

# Input
operations = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

# Output
output = []
cache = None

for op, val in zip(operations, values):
    if op == "LRUCache":
        cache = LRUCache(*val)
        output.append(None)
    elif op == "put":
        cache.put(*val)
        output.append(None)
    elif op == "get":
        output.append(cache.get(*val))

print(output)
