from dataclasses import dataclass


@dataclass
class Item:
    value: float
    weight: float

    @property
    def ratio(self) -> float:
        return self.value / self.weight


class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        if len(val) != len(wt):
            raise ValueError("values and weights must have the same length")

        current_wt = 0
        final_value = 0.0

        items = [Item(value, weight) for value, weight in zip(val, wt) if weight > 0]

        items.sort(key=lambda item: item.ratio, reverse=True)
        for item in items:
            if current_wt + item.weight <= capacity:
                current_wt += item.weight
                final_value += item.value
            else:
                remaining = capacity - current_wt
                final_value += (item.value / item.weight) * remaining
                break

        return final_value


s = Solution()
print(s.fractionalKnapsack(val=[100, 60, 100, 200], wt=[20, 10, 50, 50], capacity=50))
