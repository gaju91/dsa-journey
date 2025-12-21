# Core Principle of Index Marking

## The Fundamental Insight

**Question**: How can we store information about which numbers appeared in an array without using extra space?

**Answer**: Use the sign of the array elements themselves!

---

## The Storage Problem

### Naive Approach (Extra Space)

```python
# Find missing numbers in [1..n]
def find_missing_naive(nums):
    seen = set()  # O(n) extra space
    for num in nums:
        seen.add(num)

    missing = []
    for i in range(1, len(nums) + 1):
        if i not in seen:
            missing.append(i)
    return missing
```

**Cost**: O(n) space for the hash set

---

## The Breakthrough: Exploiting Constraints

### Key Observations

1. **Array length = n**
2. **Values are in [1..n]**
3. **Each value x can map to index x-1**
4. **We need only 1 bit of information**: "did this number appear?"

### The Mapping

```
Value x → Index (x - 1)

Examples:
  Value 1 → Index 0
  Value 5 → Index 4
  Value n → Index n-1
```

---

## Using Sign as Storage

### The Trick

Since all values are positive (in range [1..n]):
- **Negative sign** = extra bit of information
- **Original value** = `abs(number)`

### State Encoding

```python
# At index i:
if nums[i] > 0:
    # Number (i+1) has NOT appeared yet
else:  # nums[i] < 0
    # Number (i+1) HAS appeared
```

---

## Visual Example

**Input**: `nums = [4, 3, 2, 7, 8, 2, 3, 1]`
**Goal**: Find which numbers in [1..8] are present

### Step-by-Step Marking

```
Initial:  [4,  3,  2,  7,  8,  2,  3,  1]
           ↓
Process 4 (mark index 3):
          [4,  3,  2, -7,  8,  2,  3,  1]
                          ↑ marked

Process 3 (mark index 2):
          [4,  3, -2, -7,  8,  2,  3,  1]
                  ↑ marked

Process 2 (mark index 1):
          [4, -3, -2, -7,  8,  2,  3,  1]
              ↑ marked

Process 7 (mark index 6):
          [4, -3, -2, -7,  8,  2, -3,  1]
                                  ↑ marked

Process 8 (mark index 7):
          [4, -3, -2, -7,  8,  2, -3, -1]
                                       ↑ marked

Process 2 (mark index 1):
          Already negative! → 2 is a duplicate
          [4, -3, -2, -7,  8,  2, -3, -1]
              ↑ already marked

Process 3 (mark index 2):
          Already negative! → 3 is a duplicate
          [4, -3, -2, -7,  8,  2, -3, -1]
                  ↑ already marked

Process 1 (mark index 0):
          [-4, -3, -2, -7,  8,  2, -3, -1]
           ↑ marked
```

### Reading the Result

```
Final:    [-4, -3, -2, -7,  8,  2, -3, -1]
Index:      0   1   2   3   4   5   6   7

Index 4 is positive → Number (4+1) = 5 is missing
Index 5 is positive → Number (5+1) = 6 is missing

Missing numbers: [5, 6]
```

---

## Why It Works

### Mathematical Invariant

**After processing all numbers:**

```
∀ i ∈ [0, n-1]:
  nums[i] < 0  ⟺  (i+1) appeared in original array
```

### Preservation of Information

Even though we modify the signs:
- **Original value** = `abs(nums[i])` (always recoverable)
- **Visited status** = `sign(nums[i])` (newly encoded)

We've **doubled our information capacity** without extra space!

---

## The Template Formula

```python
# Phase 1: Encoding (Marking)
for i in range(n):
    value = abs(nums[i])      # Get original value
    index = value - 1         # Map to index
    nums[index] = -abs(nums[index])  # Mark as seen

# Phase 2: Decoding (Reading)
for i in range(n):
    if nums[i] > 0:
        # index i is positive → number (i+1) never appeared
        result.append(i + 1)
```

---

## Space Complexity Proof

**Claim**: This uses O(1) extra space

**Proof**:
- Input array: O(n) (given, doesn't count as "extra")
- Variables used: `i`, `value`, `index` → O(1)
- Output array: O(k) where k = result size (doesn't count as "extra" in LeetCode)

**Auxiliary space** = O(1) ✓

---

## Time Complexity Analysis

```python
# Pass 1: Mark all elements
for i in range(n):          # O(n)
    idx = abs(nums[i]) - 1  # O(1)
    nums[idx] = -abs(nums[idx])  # O(1)

# Pass 2: Collect results
for i in range(n):          # O(n)
    if nums[i] > 0:         # O(1)
        result.append(i + 1)  # O(1)
```

**Total**: O(n) + O(n) = O(n) ✓

---

## Key Insights

1. **Value-to-Index Mapping**
   - We have a perfect hash function: `h(x) = x - 1`
   - No collisions when values are unique and in [1..n]

2. **Sign as Storage**
   - Since values are positive, sign is "unused space"
   - We repurpose it to store "visited" flag

3. **In-Place Modification**
   - We're allowed to modify because we can always recover original value
   - `abs(nums[i])` gives back the original

4. **Reversibility** (Optional)
   ```python
   # Can restore original array if needed
   for i in range(n):
       nums[i] = abs(nums[i])
   ```

---

## When This Breaks

### ❌ Case 1: Values Outside Range

```python
nums = [1, 100, 3]  # 100 > n=3
idx = 100 - 1 = 99  # Index out of bounds!
```

**Solution**: Pre-process to handle out-of-range values (LC #41)

### ❌ Case 2: Negative Values

```python
nums = [1, -2, 3]
idx = abs(-2) - 1 = 1  # Works but...
# Can't distinguish between originally negative and marked negative
```

**Solution**: Clean array first (replace negatives)

### ❌ Case 3: Zero in Array

```python
nums = [0, 1, 2]
idx = 0 - 1 = -1  # Invalid index
```

**Solution**: Handle 0 as special case or adjust range

---

## Analogies

### 1. Roll Call Analogy
- **Original problem**: Track who attended class
- **Naive solution**: Keep a separate attendance sheet
- **Index marking**: Cross out names on the roster as people arrive

### 2. Library Checkout Analogy
- **Original problem**: Track which books are checked out
- **Naive solution**: Maintain a separate database
- **Index marking**: Flip the card in each book when checked out

### 3. Parking Lot Analogy
- **Original problem**: Know which spots are occupied
- **Naive solution**: Maintain a list of occupied spots
- **Index marking**: Mark each spot as occupied/empty directly

---

## Philosophical Perspective

Index marking is an example of:

1. **Constraint Exploitation**
   - Problem constraints aren't limitations—they're tools
   - `[1..n]` range isn't restrictive—it enables the solution

2. **Information Theory**
   - We need 1 bit per position
   - Sign gives us exactly 1 bit
   - Perfect match!

3. **In-Place Algorithms**
   - Don't think "I need extra space"
   - Think "What unused dimensions exist in my input?"

---

## Summary

**Core Principle**: When values are in `[1..n]` and array length is `n`:
- Map each value `x` to index `x-1`
- Use sign of `nums[x-1]` to store "seen" flag
- Read with `abs()`, write with `-abs()`

**Result**: O(1) space, O(n) time, powerful technique

---

**Next**: Read `02_why_abs_is_critical.md` to understand the most common mistake
