"""
11. Collections Module for Arrays
==================================
Specialized container datatypes from collections module.
"""

from collections import deque, Counter, defaultdict, OrderedDict, namedtuple

# ============================================
# 1. DEQUE - DOUBLE-ENDED QUEUE
# ============================================

# Create deque
dq = deque([1, 2, 3, 4, 5])
dq = deque()              # Empty
dq = deque(range(5))      # From iterable
dq = deque(maxlen=5)      # Fixed size (drops oldest)

# Operations at both ends - O(1)!
dq = deque([2, 3, 4])

dq.append(5)       # Add right: [2, 3, 4, 5]
dq.appendleft(1)   # Add left:  [1, 2, 3, 4, 5]

dq.pop()           # Remove right: returns 5, [1, 2, 3, 4]
dq.popleft()       # Remove left:  returns 1, [2, 3, 4]

# Extend at both ends
dq.extend([5, 6])        # [2, 3, 4, 5, 6]
dq.extendleft([1, 0])    # [0, 1, 2, 3, 4, 5, 6] - Note: reversed!

# Rotation
dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)       # [4, 5, 1, 2, 3] - Right rotation
dq.rotate(-2)      # [1, 2, 3, 4, 5] - Left rotation

# Reverse
dq.reverse()

# Count and index
dq.count(3)
dq.index(3)

# Maxlen behavior (sliding window)
window = deque(maxlen=3)
for i in range(5):
    window.append(i)
    print(list(window))
# [0]
# [0, 1]
# [0, 1, 2]
# [1, 2, 3]  <- 0 dropped
# [2, 3, 4]  <- 1 dropped

# ============================================
# 2. DEQUE VS LIST PERFORMANCE
# ============================================

"""
| Operation          | list    | deque   |
|-------------------|---------|---------|
| append()          | O(1)*   | O(1)    |
| pop()             | O(1)    | O(1)    |
| insert(0, x)      | O(n)    | O(1)    |
| pop(0)            | O(n)    | O(1)    |
| access by index   | O(1)    | O(n)    |

* amortized
"""

# ============================================
# 3. COUNTER
# ============================================

# Count elements
arr = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4]
counter = Counter(arr)
print(counter)  # Counter({4: 4, 3: 3, 1: 2, 2: 1})

# From string
Counter("mississippi")  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Access counts
counter[3]   # 3
counter[99]  # 0 (not KeyError!)

# Most common
counter.most_common(2)  # [(4, 4), (3, 3)]

# Operations
c1 = Counter([1, 2, 2, 3])
c2 = Counter([2, 3, 3, 4])

c1 + c2      # Add counts
c1 - c2      # Subtract (keeps positive)
c1 & c2      # Intersection (min counts)
c1 | c2      # Union (max counts)

# Get elements
list(counter.elements())  # [1, 1, 2, 3, 3, 3, 4, 4, 4, 4]

# Update counts
counter.update([5, 5, 5])
counter.subtract([4, 4])

# ============================================
# 4. DEFAULTDICT
# ============================================

# Regular dict raises KeyError
# d = {}
# d['missing']  # KeyError!

# defaultdict provides default value
dd = defaultdict(int)  # Default: 0
dd['missing']  # 0

dd = defaultdict(list)  # Default: []
dd['key'].append(1)     # No need to check if key exists

dd = defaultdict(lambda: 'N/A')
dd['missing']  # 'N/A'

# Grouping example
words = ['apple', 'banana', 'apricot', 'blueberry', 'avocado']
by_first_letter = defaultdict(list)
for word in words:
    by_first_letter[word[0]].append(word)
# {'a': ['apple', 'apricot', 'avocado'], 'b': ['banana', 'blueberry']}

# Count frequency (like Counter)
freq = defaultdict(int)
for item in [1, 2, 2, 3, 3, 3]:
    freq[item] += 1

# ============================================
# 5. NAMEDTUPLE
# ============================================

# Create a class-like tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

# Access by name or index
print(p.x)     # 10
print(p[0])    # 10

# Immutable
# p.x = 30  # AttributeError!

# Convert to dict
p._asdict()  # {'x': 10, 'y': 20}

# Replace (creates new tuple)
p2 = p._replace(x=30)  # Point(x=30, y=20)

# Useful for DSA
Edge = namedtuple('Edge', ['src', 'dest', 'weight'])
edges = [
    Edge(0, 1, 10),
    Edge(0, 2, 6),
    Edge(1, 2, 4)
]

for edge in edges:
    print(f"{edge.src} -> {edge.dest}: {edge.weight}")

# ============================================
# 6. ORDEREDDICT (Python 3.7+ regular dict is ordered)
# ============================================

from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

# Move to end
od.move_to_end('a')      # {'b': 2, 'c': 3, 'a': 1}
od.move_to_end('c', last=False)  # Move to beginning

# Pop from ends
od.popitem()             # Pop last
od.popitem(last=False)   # Pop first

# LRU Cache implementation
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# ============================================
# 7. COMMON DSA PATTERNS WITH COLLECTIONS
# ============================================

# Sliding window maximum with deque
def max_sliding_window(nums, k):
    dq = deque()  # Store indices
    result = []

    for i, num in enumerate(nums):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Find k most frequent elements
def top_k_frequent(nums, k):
    return [item for item, count in Counter(nums).most_common(k)]

# Group anagrams
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())

# ============================================
# 8. CHAINMAP (BONUS)
# ============================================

from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

chain = ChainMap(dict1, dict2)
print(chain['a'])  # 1 (from dict1)
print(chain['b'])  # 2 (from dict1, first match)
print(chain['c'])  # 4 (from dict2)

if __name__ == "__main__":
    # Deque demo
    print("=== Deque ===")
    dq = deque([1, 2, 3])
    dq.appendleft(0)
    dq.append(4)
    print(f"Deque: {dq}")

    # Counter demo
    print("\n=== Counter ===")
    arr = [1, 1, 2, 3, 3, 3]
    c = Counter(arr)
    print(f"Counter: {c}")
    print(f"Most common: {c.most_common(2)}")

    # defaultdict demo
    print("\n=== defaultdict ===")
    dd = defaultdict(list)
    dd['a'].append(1)
    dd['a'].append(2)
    dd['b'].append(3)
    print(f"defaultdict: {dict(dd)}")
