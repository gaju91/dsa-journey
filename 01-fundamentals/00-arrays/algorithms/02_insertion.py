"""
02. Array Insertion
===================

ANALOGY: Like adding people to a queue or inserting pages in a book.
Depending on WHERE you insert, the effort varies!

KEY INSIGHT:
- Insert at END → O(1) - just append
- Insert at BEGINNING → O(n) - shift everything right
- Insert at MIDDLE → O(n) - shift half elements

INTERVIEW TIP: Always ask "Where are we inserting?" The position matters!
"""

# ============================================
# APPROACH 1: INSERT AT END
# ============================================
# Time: O(1) amortized, Space: O(1)

def insert_at_end(arr, element):
    """
    Add element to end

    ANALOGY: Adding someone to the back of a line - no one else moves!

    Time: O(1) amortized*
    Space: O(1)

    *Amortized because occasionally Python list needs to resize
    """
    arr.append(element)
    return arr


# ============================================
# APPROACH 2: INSERT AT BEGINNING
# ============================================
# Time: O(n), Space: O(1)

def insert_at_beginning(arr, element):
    """
    Add element to front

    ANALOGY: Cutting in line - everyone behind you shifts back!

    Time: O(n) - must shift all elements
    Space: O(1)

    INTERVIEW NOTE: This is SLOW for large arrays.
    Consider using deque if inserting at front frequently.
    """
    arr.insert(0, element)
    return arr


# ============================================
# APPROACH 3: INSERT AT POSITION
# ============================================
# Time: O(n), Space: O(1)

def insert_at_position(arr, index, element):
    """
    Insert at specific index

    ANALOGY: Inserting a page in a book - all pages after it shift

    Time: O(n) worst case (insert at beginning)
          O(1) best case (insert at end)
    Space: O(1)
    """
    # Validate index
    if index < 0 or index > len(arr):
        raise IndexError("Index out of bounds")

    arr.insert(index, element)
    return arr


# ============================================
# APPROACH 4: INSERT IN SORTED ARRAY
# ============================================
# Time: O(n), Space: O(1)

def insert_sorted(arr, element):
    """
    Insert element maintaining sorted order

    ANALOGY: Putting a book on an alphabetically sorted shelf

    Time: O(n) - O(log n) to find position, O(n) to shift
    Space: O(1)

    This is KEY for many interview problems!
    """
    # Find insertion position
    pos = 0
    while pos < len(arr) and arr[pos] < element:
        pos += 1

    arr.insert(pos, element)
    return arr


def insert_sorted_binary(arr, element):
    """
    Insert in sorted array using binary search

    ANALOGY: Like finding where to insert a card in a sorted hand

    Time: O(n) - O(log n) search + O(n) insertion
    Space: O(1)

    Note: Binary search helps FIND position faster,
    but insertion itself is still O(n)
    """
    import bisect
    bisect.insort(arr, element)
    return arr


# ============================================
# APPROACH 5: INSERT MULTIPLE ELEMENTS
# ============================================
# Time: O(n+m), Space: O(1)

def insert_multiple(arr, index, elements):
    """
    Insert multiple elements at once

    ANALOGY: Inserting multiple pages in a book together

    Time: O(n+m) where m = len(elements)
    Space: O(1)
    """
    # Method 1: Using slice assignment
    arr[index:index] = elements

    # Method 2: Using extend at end
    # arr.extend(elements)

    return arr


# ============================================
# MANUAL IMPLEMENTATION (Understanding How It Works)
# ============================================

def insert_manual(arr, index, element):
    """
    Manual insertion to understand the mechanics

    ANALOGY: Like manually moving books on a shelf to make space

    This shows what happens under the hood!
    """
    # Append placeholder
    arr.append(None)

    # Shift elements right
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]

    # Insert element
    arr[index] = element

    return arr


# ============================================
# INTERVIEW PATTERNS
# ============================================

def insert_with_duplicates_check(arr, element):
    """
    Insert only if not duplicate

    Time: O(n)
    Space: O(1)

    INTERVIEW: Common in "unique elements" problems
    """
    if element not in arr:
        arr.append(element)
    return arr


def insert_with_capacity_limit(arr, element, max_size):
    """
    Insert with size limit (circular buffer concept)

    ANALOGY: A parking lot with limited spaces

    Time: O(1)
    Space: O(1)

    INTERVIEW: Seen in LRU cache, sliding window problems
    """
    if len(arr) >= max_size:
        arr.pop(0)  # Remove oldest
    arr.append(element)
    return arr


def insert_at_intervals(arr, element, interval):
    """
    Insert element at every k positions

    ANALOGY: Adding bookmarks every 50 pages

    Time: O(n)
    Space: O(n/k)
    """
    result = []
    for i, val in enumerate(arr):
        result.append(val)
        if (i + 1) % interval == 0:
            result.append(element)
    return result


# ============================================
# PERFORMANCE COMPARISON
# ============================================

def compare_insertion_methods():
    """
    Demonstrate performance differences

    LESSON: Position matters more than method!
    """
    import time

    n = 10000

    # Test 1: Insert at end (FAST)
    arr = []
    start = time.time()
    for i in range(n):
        arr.append(i)
    print(f"Insert at end: {time.time() - start:.4f}s")

    # Test 2: Insert at beginning (SLOW)
    arr = []
    start = time.time()
    for i in range(min(n, 1000)):  # Reduced n to avoid slowness
        arr.insert(0, i)
    print(f"Insert at beginning: {time.time() - start:.4f}s")

    # Test 3: Using deque for beginning (FAST)
    from collections import deque
    dq = deque()
    start = time.time()
    for i in range(n):
        dq.appendleft(i)
    print(f"Insert at beginning (deque): {time.time() - start:.4f}s")


# ============================================
# COMMON MISTAKES
# ============================================

def demonstrate_mistakes():
    """Interview gotchas"""

    arr = [1, 2, 3, 4, 5]

    # MISTAKE 1: Index out of bounds
    # arr.insert(10, 99)  # Silently adds at end!
    # LESSON: Python is forgiving, but be careful

    # MISTAKE 2: Insert in loop (quadratic time!)
    # for i in range(100):
    #     arr.insert(0, i)  # O(n²) total!
    # LESSON: Use deque or build new list

    # MISTAKE 3: Forgetting insert modifies in-place
    arr.insert(2, 99)
    # arr is now [1, 2, 99, 3, 4, 5]
    # LESSON: insert() returns None, modifies original


# ============================================
# COMPLEXITY SUMMARY
# ============================================

"""
POSITION           | Time    | Analogy
-------------------|---------|---------------------------
At end (append)    | O(1)*   | Join end of line
At beginning       | O(n)    | Cut in line (everyone shifts)
At middle (index)  | O(n)    | Insert in middle of line
In sorted order    | O(n)    | Organized insertion

*Amortized O(1) due to occasional list resizing

SPACE: O(1) - insertion doesn't need extra space
       (the list itself grows, but that's inherent)

KEY TAKEAWAY:
Insert at END → O(1) ✅ Good
Insert elsewhere → O(n) ❌ Slow

For frequent front insertions, use collections.deque!
"""


if __name__ == "__main__":
    print("=" * 60)
    print("ARRAY INSERTION DEMO")
    print("=" * 60)

    # Demo 1: Insert at end
    arr = [1, 2, 3]
    print(f"\n1. Original: {arr}")
    insert_at_end(arr, 4)
    print(f"   After insert at end (4): {arr}")

    # Demo 2: Insert at beginning
    arr = [1, 2, 3]
    print(f"\n2. Original: {arr}")
    insert_at_beginning(arr, 0)
    print(f"   After insert at beginning (0): {arr}")

    # Demo 3: Insert at position
    arr = [1, 2, 4, 5]
    print(f"\n3. Original: {arr}")
    insert_at_position(arr, 2, 3)
    print(f"   After insert 3 at index 2: {arr}")

    # Demo 4: Insert in sorted array
    arr = [1, 3, 5, 7, 9]
    print(f"\n4. Sorted: {arr}")
    insert_sorted(arr, 6)
    print(f"   After inserting 6 (sorted): {arr}")

    # Demo 5: Insert multiple
    arr = [1, 2, 5, 6]
    print(f"\n5. Original: {arr}")
    insert_multiple(arr, 2, [3, 4])
    print(f"   After inserting [3,4] at index 2: {arr}")

    # Demo 6: Manual insertion (educational)
    arr = [1, 2, 4, 5]
    print(f"\n6. Original: {arr}")
    insert_manual(arr, 2, 3)
    print(f"   After manual insert 3 at index 2: {arr}")

    print("\n" + "=" * 60)
    print("✅ All insertion methods demonstrated!")
    print("\nPERFORMANCE TIPS:")
    print("- Insert at end: O(1) - FAST ✅")
    print("- Insert at front/middle: O(n) - SLOW ⚠️")
    print("- For frequent front inserts: use deque")
