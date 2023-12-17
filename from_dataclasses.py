from dataclasses import dataclass

@dataclass
class Counter:
    value: int = 0

    def getVal(self):
        self.value += 1
        return self.value

# Usage
counter = Counter()
print(counter.getVal())  # This will print 1
print(counter.getVal())  # This will print 2

c2 = Counter()
print(counter.getVal())
print(c2.getVal())

