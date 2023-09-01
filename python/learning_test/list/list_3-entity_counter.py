
from collections import Counter

my_list = [10, 10, 5, 2, 9, 9, 9]
counter = Counter(my_list)

print(counter)
print(counter[10])
print(counter.most_common(1))