class StockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price):
        self.prices.append(price)
        span = 1
        for i in range(len(self.prices) - 2, -1, -1):
            if self.prices[i] <= price:
                span += 1
            else:
                break
        return span

# Test case
spanner = StockSpanner()
result = [None]
queries = [[100], [80], [60], [70], [60], [75], [85]]
for i in queries:
    result.append(spanner.next(i[0]))

print(result)
