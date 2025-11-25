"""
03. Array Deletion
==================

ANALOGY: Like removing people from a queue or tearing pages from a book.
Similar to insertion - WHERE you delete matters!

KEY INSIGHT:
- Delete from END → O(1) - just pop
- Delete from BEGINNING → O(n) - shift everything left
- Delete from MIDDLE → O(n) - shift half elements

INTERVIEW TIP: Deletion often requires shifting. Consider if you can avoid
actual deletion (use markers, swap with end, etc.)
"""

# ============================================
# APPROACH 1: DELETE FROM END
# ============================================
# Time: O(1), Space: O(1)

def delete_from_end(arr):
    """
    Remove last element

    ANALOGY: Person leaving from back of line - no one else affected!

    Time: O(1)
    Space: O(1)

    Returns: removed element
    """
    if not arr:
        raise IndexError("Cannot pop from empty array")

    return arr.pop()  # or arr.pop(-1)


# ============================================
# APPROACH 2: DELETE FROM BEGINNING
# ============================================
# Time: O(n), Space: O(1)

def delete_from_beginning(arr):
    """
    Remove first element

    ANALOGY: First person leaves line - everyone else moves forward!

    Time: O(n) - must shift all elements left
    Space: O(1)

    INTERVIEW WARNING: This is SLOW! O(n) for each deletion.
    """
    if not arr:
        raise IndexError("Cannot pop from empty array")

    return arr.pop(0)


# ============================================
# APPROACH 3: DELETE AT POSITION
# ============================================
# Time: O(n), Space: O(1)

def delete_at_position(arr, index):
    """
    Delete element at specific index

    ANALOGY: Removing a page - all later pages shift forward

    Time: O(n) worst case (delete from beginning)
          O(1) best case (delete from end)
    Space: O(1)
    """
    if index < 0 or index >= len(arr):
        raise IndexError(f"Index {index} out of bounds")

    return arr.pop(index)


# ============================================
# APPROACH 4: DELETE BY VALUE
# ============================================
# Time: O(n), Space: O(1)

def delete_by_value(arr, value):
    """
    Remove FIRST occurrence of value

    ANALOGY: Finding and removing a specific book from shelf

    Time: O(n) - search O(n) + delete O(n) = O(n)
    Space: O(1)

    INTERVIEW: This removes only FIRST occurrence!
    """
    try:
        arr.remove(value)
        return True
    except ValueError:
        return False  # Value not found


def delete_all_occurrences(arr, value):
    """
    Remove ALL occurrences of value

    ANALOGY: Removing all copies of same book

    Time: O(n²) - wrong way
    Time: O(n) - right way (shown below)
    Space: O(1)
    """
    # WRONG WAY - O(n²)
    # while value in arr:
    #     arr.remove(value)

    # RIGHT WAY - O(n)
    i = 0
    while i < len(arr):
        if arr[i] == value:
            arr.pop(i)
        else:
            i += 1

    # BEST WAY - O(n) with list comprehension
    # return [x for x in arr if x != value]


# ============================================
# APPROACH 5: DELETE WITH CONDITION
# ============================================
# Time: O(n), Space: O(1)

def delete_if(arr, condition):
    """
    Remove all elements satisfying condition

    ANALOGY: Security removing all prohibited items

    Time: O(n)
    Space: O(1) if in-place, O(n) if new list
    """
    i = 0
    while i < len(arr):
        if condition(arr[i]):
            arr.pop(i)
        else:
            i += 1

    return arr


# Example: Delete all even numbers
def delete_evens(arr):
    return delete_if(arr, lambda x: x % 2 == 0)


# ============================================
# APPROACH 6: DELETE DUPLICATES
# ============================================

def delete_duplicates_sorted(arr):
    """
    Remove duplicates from SORTED array (IN-PLACE)

    ANALOGY: Removing repeated words in sorted list

    Time: O(n)
    Space: O(1)

    INTERVIEW CLASSIC: LeetCode #26
    """
    if not arr:
        return 0

    write_index = 1  # Position to write next unique element

    for read_index in range(1, len(arr)):
        if arr[read_index] != arr[read_index - 1]:
            arr[write_index] = arr[read_index]
            write_index += 1

    # Trim array to new length
    del arr[write_index:]

    return write_index  # New length


def delete_duplicates_unsorted(arr):
    """
    Remove duplicates from UNSORTED array

    ANALOGY: Keeping only first occurrence of each item

    Time: O(n)
    Space: O(n) for hash set

    Two approaches:
    1. Preserve order - use seen set (shown)
    2. Don't care about order - convert to set
    """
    seen = set()
    unique = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            unique.append(num)

    arr.clear()
    arr.extend(unique)
    return arr


# ============================================
# APPROACH 7: EFFICIENT DELETION (SWAP WITH END)
# ============================================
# Time: O(1), Space: O(1)

def delete_by_swap_with_end(arr, index):
    """
    Delete by swapping with last element

    ANALOGY: Like removing someone from middle of line by swapping
    with last person, then removing last

    Time: O(1) - no shifting needed!
    Space: O(1)

    TRADEOFF: Order is NOT preserved

    INTERVIEW: Use when order doesn't matter!
    Common in graph adjacency lists, hash tables
    """
    if index < 0 or index >= len(arr):
        raise IndexError("Index out of bounds")

    # Swap with last
    arr[index] = arr[-1]

    # Remove last
    arr.pop()

    return arr


# ============================================
# APPROACH 8: LAZY DELETION (MARKING)
# ============================================

def lazy_delete(arr, indices_to_delete):
    """
    Mark for deletion, compact later

    ANALOGY: Putting "DO NOT USE" stickers instead of actually removing

    Time: O(n) for marking + O(n) for compaction = O(n)
    Space: O(n) for markers

    INTERVIEW: Used in databases, garbage collection
    """
    # Mark deleted indices
    markers = [False] * len(arr)
    for idx in indices_to_delete:
        markers[idx] = True

    # Compact (remove marked)
    result = [arr[i] for i in range(len(arr)) if not markers[i]]

    arr.clear()
    arr.extend(result)
    return arr


# ============================================
# INTERVIEW PATTERNS
# ============================================

def remove_element(arr, val):
    """
    LeetCode #27 - Remove Element

    Remove all occurrences of val IN-PLACE

    Time: O(n)
    Space: O(1)

    TWO POINTERS technique!
    """
    write_idx = 0

    for read_idx in range(len(arr)):
        if arr[read_idx] != val:
            arr[write_idx] = arr[read_idx]
            write_idx += 1

    # Trim array
    del arr[write_idx:]
    return write_idx


def move_zeros(arr):
    """
    LeetCode #283 - Move Zeros

    Move all zeros to end while maintaining order

    ANALOGY: Pushing all empty boxes to back of truck

    Time: O(n)
    Space: O(1)

    KEY PATTERN: Two pointers - write position for non-zeros
    """
    write_idx = 0

    # Move all non-zeros to front
    for read_idx in range(len(arr)):
        if arr[read_idx] != 0:
            arr[write_idx] = arr[read_idx]
            write_idx += 1

    # Fill rest with zeros
    while write_idx < len(arr):
        arr[write_idx] = 0
        write_idx += 1

    return arr


# ============================================
# COMMON MISTAKES
# ============================================

def demonstrate_mistakes():
    """Interview gotchas"""

    # MISTAKE 1: Modifying while iterating
    arr = [1, 2, 3, 4, 5]
    # WRONG:
    # for i in range(len(arr)):
    #     if arr[i] % 2 == 0:
    #         arr.pop(i)  # Indices shift, causes bugs!

    # RIGHT: Iterate backwards
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] % 2 == 0:
            arr.pop(i)

    # MISTAKE 2: Deleting in loop with while (forgetting i++)
    arr = [1, 2, 2, 3]
    # WRONG:
    # i = 0
    # while i < len(arr):
    #     if arr[i] == 2:
    #         arr.pop(i)
    #     i += 1  # This increments even after pop!

    # RIGHT: Only increment if not deleted
    i = 0
    while i < len(arr):
        if arr[i] == 2:
            arr.pop(i)
        else:
            i += 1


# ============================================
# COMPLEXITY SUMMARY
# ============================================

"""
OPERATION              | Time    | Space | Analogy
-----------------------|---------|-------|----------------------
Delete from end        | O(1)    | O(1)  | Person leaves back
Delete from beginning  | O(n)    | O(1)  | Everyone shifts forward
Delete at index        | O(n)    | O(1)  | People after shift
Delete by value        | O(n)    | O(1)  | Search + delete
Delete duplicates      | O(n)    | O(1)* | Two pointers
Swap with end delete   | O(1)    | O(1)  | Swap + pop (order lost)

*In-place for sorted, O(n) space for unsorted

KEY PATTERNS:
1. Two Pointers (read/write) - for in-place deletion
2. Swap with End - O(1) delete when order doesn't matter
3. Backwards Iteration - safe deletion while looping
"""


if __name__ == "__main__":
    print("=" * 60)
    print("ARRAY DELETION DEMO")
    print("=" * 60)

    # Demo 1: Delete from end
    arr = [1, 2, 3, 4, 5]
    print(f"\n1. Original: {arr}")
    removed = delete_from_end(arr)
    print(f"   Deleted from end: {removed}, remaining: {arr}")

    # Demo 2: Delete from beginning
    arr = [1, 2, 3, 4, 5]
    print(f"\n2. Original: {arr}")
    removed = delete_from_beginning(arr)
    print(f"   Deleted from beginning: {removed}, remaining: {arr}")

    # Demo 3: Delete at position
    arr = [1, 2, 3, 4, 5]
    print(f"\n3. Original: {arr}")
    removed = delete_at_position(arr, 2)
    print(f"   Deleted at index 2: {removed}, remaining: {arr}")

    # Demo 4: Delete by value
    arr = [1, 2, 3, 2, 4]
    print(f"\n4. Original: {arr}")
    delete_by_value(arr, 2)
    print(f"   After removing first '2': {arr}")

    # Demo 5: Delete all occurrences
    arr = [1, 2, 3, 2, 4, 2]
    print(f"\n5. Original: {arr}")
    delete_all_occurrences(arr, 2)
    print(f"   After removing all '2's: {arr}")

    # Demo 6: Delete duplicates (sorted)
    arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
    print(f"\n6. Sorted with duplicates: {arr}")
    new_len = delete_duplicates_sorted(arr)
    print(f"   After removing duplicates: {arr}")

    # Demo 7: Move zeros
    arr = [0, 1, 0, 3, 12]
    print(f"\n7. Original: {arr}")
    move_zeros(arr)
    print(f"   After moving zeros to end: {arr}")

    # Demo 8: Swap with end (O(1) delete)
    arr = [1, 2, 3, 4, 5]
    print(f"\n8. Original: {arr}")
    delete_by_swap_with_end(arr, 2)
    print(f"   After O(1) delete at index 2: {arr} (order changed!)")

    print("\n" + "=" * 60)
    print("✅ All deletion methods demonstrated!")
    print("\nKEY TAKEAWAYS:")
    print("- Delete from end: O(1) - FAST ✅")
    print("- Delete elsewhere: O(n) - requires shifting ⚠️")
    print("- Two pointers: Best for in-place deletion")
    print("- Swap with end: O(1) but loses order")
