class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.frequency = {}
        self.min_frequency = 0

    def get(self, key):
        if key not in self.cache:
            return -1

        value, freq = self.cache[key]
        self.frequency[key] += 1

        # Update the minimum frequency if necessary
        if freq == self.min_frequency and not self.frequency[key]:
            self.min_frequency += 1

        return value

    def put(self, key, value):
        if self.capacity <= 0:
            return

        if key in self.cache:
            # Update the value and frequency of the existing key
            self.cache[key] = (value, self.cache[key][1])
            self.get(key)  # Increase frequency
            return

        if len(self.cache) >= self.capacity:
            # Evict the least frequently used key
            key_to_evict = min(self.frequency, key=self.frequency.get)
            del self.cache[key_to_evict]
            del self.frequency[key_to_evict]

        # Add the new key with a frequency of 1
        self.cache[key] = (value, 1)
        self.frequency[key] = 1
        self.min_frequency = 1
operations = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

lfu_cache = None
output = []

for op, val in zip(operations, values):
    if op == "LFUCache":
        lfu_cache = LFUCache(val[0])
        output.append(None)
    elif op == "put":
        lfu_cache.put(val[0], val[1])
        output.append(None)
    elif op == "get":
        output.append(lfu_cache.get(val[0]))

print(output)
