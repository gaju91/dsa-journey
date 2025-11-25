"""
06. Interview Classic Algorithms
================================

The algorithms that appear in EVERY coding interview!
Master these and you're 50% ready for arrays questions.

ANALOGIES included for each to make them memorable.
"""

# ============================================
# 1. TWO SUM - The Most Famous Problem
# ============================================

def two_sum_brute_force(arr, target):
    """
    Find two numbers that add up to target

    ANALOGY: Finding two puzzle pieces that fit together

    Time: O(n²) - check all pairs
    Space: O(1)

    INTERVIEW: Never submit this! Show you know optimization.
    """
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]
    return [-1, -1]


def two_sum_hash(arr, target):
    """
    Two Sum using Hash Map (OPTIMAL)

    ANALOGY: Looking for a partner - keep a list of who you've met,
    check if their perfect match shows up

    Time: O(n) - single pass ⭐
    Space: O(n) - hash map

    INTERVIEW: LeetCode #1 - THIS IS THE ANSWER!
    """
    seen = {}  # {value: index}

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return [-1, -1]


def two_sum_sorted(arr, target):
    """
    Two Sum when array is SORTED

    ANALOGY: Two people walking from opposite ends of bridge,
    meeting in middle

    Time: O(n) - two pointers ⭐
    Space: O(1)

    INTERVIEW: LeetCode #167 - Two Sum II
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]


# ============================================
# 2. KADANE'S ALGORITHM - Maximum Subarray
# ============================================

def max_subarray_brute(arr):
    """
    Find maximum sum of contiguous subarray (Brute Force)

    Time: O(n²) or O(n³) - check all subarrays
    Space: O(1)

    NOT OPTIMAL!
    """
    n = len(arr)
    max_sum = float('-inf')

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)

    return max_sum


def max_subarray_kadane(arr):
    """
    Kadane's Algorithm for Maximum Subarray Sum

    ANALOGY: Like a gambler - keep winning streak going,
    but start fresh if you're losing too much

    Time: O(n) - single pass ⭐
    Space: O(1)

    INTERVIEW: LeetCode #53 - MUST KNOW THIS!

    KEY INSIGHT: At each position, decide:
    - Continue current subarray (add to current_sum)
    - Start new subarray (reset to current element)
    """
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        # Key decision: extend or start new
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


def max_subarray_with_indices(arr):
    """
    Kadane's with start/end indices

    Returns: (max_sum, start, end)
    """
    max_sum = arr[0]
    current_sum = arr[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, start, end


# ============================================
# 3. SLIDING WINDOW - Fixed Size
# ============================================

def max_sum_subarray_k(arr, k):
    """
    Maximum sum of subarray of size k

    ANALOGY: Moving window across a wall - slide one step,
    add new, remove old

    Time: O(n) - single pass ⭐
    Space: O(1)

    INTERVIEW: Foundation for many problems!
    """
    if len(arr) < k:
        return -1

    # Calculate first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


def avg_of_subarrays_k(arr, k):
    """
    Average of all contiguous subarrays of size k

    Time: O(n)
    """
    result = []
    window_sum = sum(arr[:k])
    result.append(window_sum / k)

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        result.append(window_sum / k)

    return result


# ============================================
# 4. SLIDING WINDOW - Variable Size
# ============================================

def smallest_subarray_sum(arr, target):
    """
    Smallest subarray with sum >= target

    ANALOGY: Expanding/contracting accordion - grow until you
    meet goal, then shrink as much as possible

    Time: O(n) - each element visited at most twice ⭐
    Space: O(1)

    INTERVIEW: LeetCode #209
    """
    min_length = float('inf')
    window_sum = 0
    left = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        # Shrink window while condition met
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0


def longest_subarray_with_k_distinct(arr, k):
    """
    Longest subarray with at most k distinct elements

    ANALOGY: Shopping cart with limit on different item types

    Time: O(n)
    Space: O(k)

    INTERVIEW: Very common pattern!
    """
    from collections import defaultdict

    char_count = defaultdict(int)
    max_length = 0
    left = 0

    for right in range(len(arr)):
        char_count[arr[right]] += 1

        # Shrink if too many distinct
        while len(char_count) > k:
            char_count[arr[left]] -= 1
            if char_count[arr[left]] == 0:
                del char_count[arr[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


# ============================================
# 5. PREFIX SUM
# ============================================

def subarray_sum_equals_k(arr, k):
    """
    Count subarrays with sum equal to k

    ANALOGY: Finding pairs of points with specific distance

    Time: O(n) ⭐
    Space: O(n)

    INTERVIEW: LeetCode #560 - Tricky!

    KEY INSIGHT: prefix_sum[j] - prefix_sum[i] = k
    So find prefix_sum[i] = prefix_sum[j] - k
    """
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # prefix_sum: frequency

    for num in arr:
        prefix_sum += num

        # Check if (prefix_sum - k) exists
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]

        # Add current prefix_sum
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

    return count


# ============================================
# 6. BEST TIME TO BUY/SELL STOCK
# ============================================

def max_profit(prices):
    """
    Maximum profit from single buy/sell transaction

    ANALOGY: Time travel - know the lowest point you've seen,
    calculate profit if you sell today

    Time: O(n) ⭐
    Space: O(1)

    INTERVIEW: LeetCode #121 - Classic!
    """
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        # Update minimum price seen
        min_price = min(min_price, price)
        # Calculate profit if sold today
        profit = price - min_price
        # Update max profit
        max_profit = max(max_profit, profit)

    return max_profit


def max_profit_multiple(prices):
    """
    Maximum profit with multiple transactions

    ANALOGY: Buy every valley, sell every peak

    Time: O(n) ⭐
    Space: O(1)

    INTERVIEW: LeetCode #122
    """
    total_profit = 0

    for i in range(1, len(prices)):
        # If price increased, we "profit"
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]

    return total_profit


# ============================================
# 7. PRODUCT OF ARRAY EXCEPT SELF
# ============================================

def product_except_self(arr):
    """
    Product of all elements except current

    ANALOGY: For each person, calculate product of everyone else

    Time: O(n) ⭐
    Space: O(1) (output array doesn't count)

    INTERVIEW: LeetCode #238 - Clever!

    KEY TRICK: Left products × Right products
    """
    n = len(arr)
    result = [1] * n

    # Left pass - product of all left elements
    left = 1
    for i in range(n):
        result[i] = left
        left *= arr[i]

    # Right pass - multiply by product of right elements
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= arr[i]

    return result


# ============================================
# 8. CONTAINS DUPLICATE
# ============================================

def contains_duplicate(arr):
    """
    Check if array has duplicates

    Time: O(n) using set ⭐
    Space: O(n)

    INTERVIEW: LeetCode #217 - Easy but common!
    """
    return len(arr) != len(set(arr))


def contains_nearby_duplicate(arr, k):
    """
    Check if duplicate exists within distance k

    ANALOGY: Sliding window of size k, check for duplicates

    Time: O(n) ⭐
    Space: O(min(n, k))

    INTERVIEW: LeetCode #219
    """
    window = set()
    for i, num in enumerate(arr):
        if num in window:
            return True

        window.add(num)

        # Maintain window size k
        if len(window) > k:
            window.remove(arr[i - k])

    return False


# ============================================
# COMPLEXITY SUMMARY TABLE
# ============================================

"""
Algorithm                  | Time    | Space | LeetCode #
---------------------------|---------|-------|------------
Two Sum (hash)             | O(n)    | O(n)  | #1
Kadane's (max subarray)    | O(n)    | O(1)  | #53
Sliding Window Fixed       | O(n)    | O(1)  | #643
Sliding Window Variable    | O(n)    | O(k)  | #209, #904
Subarray Sum = K           | O(n)    | O(n)  | #560
Buy/Sell Stock             | O(n)    | O(1)  | #121, #122
Product Except Self        | O(n)    | O(1)  | #238
Contains Duplicate         | O(n)    | O(n)  | #217, #219

ALL ARE O(n) TIME! ⭐
Learn these patterns and 50% of array problems become easy!
"""


if __name__ == "__main__":
    print("=" * 60)
    print("INTERVIEW CLASSIC ALGORITHMS DEMO")
    print("=" * 60)

    # 1. Two Sum
    arr = [2, 7, 11, 15]
    target = 9
    print(f"\n1. Two Sum: {arr}, target={target}")
    print(f"   Indices: {two_sum_hash(arr, target)}")

    # 2. Kadane's
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"\n2. Max Subarray: {arr}")
    max_sum, start, end = max_subarray_with_indices(arr)
    print(f"   Max sum: {max_sum}, subarray: {arr[start:end+1]}")

    # 3. Sliding Window
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    print(f"\n3. Max Sum of {k} elements: {arr}")
    print(f"   Max sum: {max_sum_subarray_k(arr, k)}")

    # 4. Buy/Sell Stock
    prices = [7, 1, 5, 3, 6, 4]
    print(f"\n4. Stock Prices: {prices}")
    print(f"   Max profit: {max_profit(prices)}")

    # 5. Product Except Self
    arr = [1, 2, 3, 4]
    print(f"\n5. Product Except Self: {arr}")
    print(f"   Result: {product_except_self(arr)}")

    # 6. Subarray Sum = K
    arr = [1, 1, 1]
    k = 2
    print(f"\n6. Subarray Sum = {k}: {arr}")
    print(f"   Count: {subarray_sum_equals_k(arr, k)}")

    print("\n" + "=" * 60)
    print("✅ All classic algorithms demonstrated!")
    print("\nMASTER THESE PATTERNS:")
    print("- Two Pointers (Two Sum sorted)")
    print("- Hash Map (Two Sum unsorted)")
    print("- Kadane's (Max subarray)")
    print("- Sliding Window (Fixed & Variable)")
    print("- Prefix Sum (Subarray sum)")
