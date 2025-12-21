# Why `abs()` is Critical

## The Most Common Bug

**90% of index marking failures** come from forgetting `abs()` when reading values.

Let's understand why it's absolutely necessary.

---

## The Problem

### Without `abs()` - WRONG

```python
def findDisappearedNumbers(nums):
    for i in range(len(nums)):
        idx = nums[i] - 1  # BUG: What if nums[i] is already negative?
        nums[idx] = -nums[idx]

    return [i+1 for i in range(len(nums)) if nums[i] > 0]
```

### What Goes Wrong

```
Input: [4, 3, 2, 7, 8, 2, 3, 1]

Step 1: Process 4
  idx = 4 - 1 = 3
  nums[3] = -7
  Array: [4, 3, 2, -7, 8, 2, 3, 1]
  ✓ Correct

Step 2: Process 3
  idx = 3 - 1 = 2
  nums[2] = -2
  Array: [4, 3, -2, -7, 8, 2, 3, 1]
  ✓ Correct

Step 3: Process -2 (now negative!)
  idx = -2 - 1 = -3  # DISASTER!
  nums[-3] attempts to access index from the end
  ❌ Wrong behavior!
```

---

## The Fix: Always Use `abs()`

### Correct Version

```python
def findDisappearedNumbers(nums):
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1  # ✓ Always get positive value
        nums[idx] = -abs(nums[idx])

    return [i+1 for i in range(len(nums)) if nums[i] > 0]
```

### Why It Works

```
Input: [4, 3, 2, 7, 8, 2, 3, 1]

Step 1: Process 4
  idx = abs(4) - 1 = 3
  nums[3] = -abs(7) = -7
  Array: [4, 3, 2, -7, 8, 2, 3, 1]

Step 2: Process 3
  idx = abs(3) - 1 = 2
  nums[2] = -abs(2) = -2
  Array: [4, 3, -2, -7, 8, 2, 3, 1]

Step 3: Process -2 (already marked)
  idx = abs(-2) - 1 = 1  # ✓ Correct! Gets original value
  nums[1] = -abs(3) = -3
  Array: [4, -3, -2, -7, 8, 2, 3, 1]

Continue processing...
```

---

## Two Rules for `abs()`

### Rule 1: Reading Values - ALWAYS `abs()`

```python
# When getting a value to process
value = abs(nums[i])  # ✓ ALWAYS

# When calculating index
idx = abs(nums[i]) - 1  # ✓ ALWAYS
```

**Why**: Value might already be negative from previous marking

### Rule 2: Marking Indices - Use `-abs()`

```python
# When marking an index as visited
nums[idx] = -abs(nums[idx])  # ✓ CORRECT

# NOT this:
nums[idx] = -nums[idx]  # ❌ WRONG - can toggle back to positive!
```

**Why**: Without `abs()`, double marking toggles back to positive

---

## Visual Proof: The Toggle Problem

### Using `-nums[idx]` (WRONG)

```python
nums[idx] = -nums[idx]

Initial value: 5
First mark:  -5  ✓ Looks good
Second mark: 5   ❌ Back to positive! Looks like never visited!
```

### Using `-abs(nums[idx])` (CORRECT)

```python
nums[idx] = -abs(nums[idx])

Initial value: 5
First mark:  -abs(5) = -5   ✓
Second mark: -abs(-5) = -5  ✓ Stays negative!
```

---

## Common Scenarios Where `abs()` Saves You

### Scenario 1: Finding Duplicates

```python
# Without abs() - BREAKS
for i in range(len(nums)):
    idx = nums[i] - 1  # ❌ Fails when nums[i] < 0
    if nums[idx] < 0:
        return idx + 1  # Found duplicate
    nums[idx] = -nums[idx]

# With abs() - WORKS
for i in range(len(nums)):
    idx = abs(nums[i]) - 1  # ✓ Always positive
    if nums[idx] < 0:
        return idx + 1
    nums[idx] = -nums[idx]
```

### Scenario 2: Multiple Passes

```python
# First pass: Mark evens
for i in range(len(nums)):
    if abs(nums[i]) % 2 == 0:  # ✓ Must use abs()
        idx = abs(nums[i]) - 1
        nums[idx] = -abs(nums[idx])

# Second pass: Mark odds (some already negative!)
for i in range(len(nums)):
    if abs(nums[i]) % 2 == 1:  # ✓ Must use abs()
        idx = abs(nums[i]) - 1
        nums[idx] = -abs(nums[idx])
```

---

## The Mental Model

Think of `abs()` as your "time machine":

```
abs(nums[i]) → "What was the original value before any marking?"
```

**Every time you read a value**, ask yourself:
> "Could this value have been marked by a previous iteration?"

If yes → **use `abs()`**

---

## Debugging Checklist

If your index marking code fails, check these:

```python
# ❌ Common mistakes:
idx = nums[i] - 1              # Should be: abs(nums[i]) - 1
nums[idx] = -nums[idx]         # Should be: -abs(nums[idx])
if nums[i] % 2 == 0:          # Should be: abs(nums[i]) % 2 == 0
value = nums[i]                # Should be: abs(nums[i])
```

---

## Practice: Spot the Bugs

### Example 1
```python
for i in range(len(nums)):
    idx = nums[i] - 1  # BUG 1: Missing abs()
    nums[idx] = -nums[idx]  # BUG 2: Missing abs()
```

**Fixes**:
```python
for i in range(len(nums)):
    idx = abs(nums[i]) - 1
    nums[idx] = -abs(nums[idx])
```

### Example 2
```python
for i in range(len(nums)):
    idx = abs(nums[i]) - 1
    if nums[idx] < 0:  # ✓ OK - checking sign
        print("Duplicate")
    nums[idx] = -nums[idx]  # BUG: Missing abs()
```

**Fix**:
```python
for i in range(len(nums)):
    idx = abs(nums[i]) - 1
    if nums[idx] < 0:
        print("Duplicate")
    nums[idx] = -abs(nums[idx])  # ✓ Fixed
```

### Example 3
```python
for i in range(len(nums)):
    value = nums[i]  # BUG: Missing abs()
    if value > 0:
        idx = value - 1
        nums[idx] = -abs(nums[idx])
```

**Fix**:
```python
for i in range(len(nums)):
    value = abs(nums[i])  # ✓ Fixed
    if value > 0:
        idx = value - 1
        nums[idx] = -abs(nums[idx])
```

---

## The Golden Rules

### When Reading
```python
value = abs(nums[i])      # Reading value
idx = abs(nums[i]) - 1    # Calculating index
```

### When Marking
```python
nums[idx] = -abs(nums[idx])  # Making negative
```

### When Checking Conditions
```python
if abs(nums[i]) == target:  # Comparing values
if abs(nums[i]) % 2 == 0:   # Mathematical operations
```

### When Checking Visit Status
```python
if nums[idx] < 0:  # ✓ OK - we're checking sign, not value
```

---

## Why Some Solutions Skip `abs()` and Still Work

### LeetCode may accept solutions that partially work:

```python
# This might pass some test cases
for i in range(len(nums)):
    idx = nums[i] - 1  # No abs()
    nums[idx] = -nums[idx]
```

**Why it sometimes works**:
- If you process elements left-to-right
- And values happen to be unique
- You might mark before reading

**But it's fragile**:
- Fails on duplicates
- Fails on certain orderings
- Not the intended solution

**Always use `abs()`** - it's the robust, correct approach.

---

## Summary

| Operation | Code | Why |
|-----------|------|-----|
| Read value | `abs(nums[i])` | Value might be marked negative |
| Get index | `abs(nums[i]) - 1` | Value might be marked negative |
| Mark index | `-abs(nums[idx])` | Ensure always negative, no toggle |
| Check visited | `nums[idx] < 0` | We're checking sign, not value |

**Golden rule**: When in doubt, use `abs()`

---

**Next**: Read `03_common_patterns_and_variants.md` to see all problem types
