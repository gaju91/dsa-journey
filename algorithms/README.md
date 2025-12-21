# Algorithm Patterns Collection

> **Purpose**: Document reusable algorithm patterns with comprehensive explanations, not just memorized solutions.

This folder contains algorithm patterns that appear repeatedly in coding interviews and competitive programming. Each pattern is documented with theory, implementation, and practice problems.

---

## Philosophy

**We don't memorize solutions. We understand patterns.**

Each algorithm pattern here is:
- **Explained from first principles** - understand the "why"
- **Documented with multiple variants** - see all use cases
- **Accompanied by practice problems** - master through application
- **Written for reusability** - pattern over specific problem

---

## Available Patterns

### 1. Index Marking
**Folder**: `00-index-marking/`

**Core Idea**: Use array elements' signs to encode presence/absence information without extra space.

**When to Use**:
- Array values in bounded range `[1..n]`
- Need to find missing/duplicate numbers
- O(1) space required

**Key Problems**: LC #448, LC #442, LC #645, LC #41

**Difficulty**: Medium (technique) | Hard (LC #41)

[📖 Read Full Documentation](./00-index-marking/README.md)

---

### 2. Two Pointers ⭐
**Folder**: `01-two-pointers/`

**Core Idea**: Use two indices to traverse arrays, eliminating nested loops through intelligent pointer movement.

**When to Use**:
- Sorted arrays (or can be sorted)
- Finding pairs/triplets with conditions
- In-place array modifications
- Subarray/substring problems
- Palindrome checking

**Key Problems**: LC #167, LC #15, LC #11, LC #26, LC #125

**Difficulty**: Easy to Medium

**Interview Frequency**: ⭐⭐⭐⭐⭐ (Top 3 most important!)

[📖 Read Full Documentation](./01-two-pointers/README.md)

---

## Pattern Categories

### Space Optimization Patterns
- ✅ **Index Marking** - Use sign bit for storage
- ✅ **Two Pointers** - Eliminate nested loops
- 🚧 XOR Tricks - Coming soon

### Mathematical Patterns
- 🚧 Sum Formulas - Coming soon
- 🚧 GCD/LCM - Coming soon
- 🚧 Prime Sieve - Coming soon

### Graph Patterns
- 🚧 DFS Templates - Coming soon
- 🚧 BFS Templates - Coming soon
- 🚧 Union Find - Coming soon

### Dynamic Programming Patterns
- 🚧 Knapsack Variants - Coming soon
- 🚧 Subsequence Problems - Coming soon
- 🚧 State Machine DP - Coming soon

---

## How to Use This Collection

### For Learning
1. **Read the README** of the pattern first
2. **Study concepts/** for deep understanding
3. **Work through problems/** with solutions
4. **Practice on LeetCode** to reinforce

### For Interview Prep
1. **Identify pattern** from problem constraints
2. **Recall template** from README
3. **Apply pattern** with modifications
4. **Explain reasoning** to interviewer

### For Reference
- Each pattern has a **quick reference template**
- Check **mental checklist** before applying
- Review **common mistakes** to avoid

---

## Pattern Recognition Guide

| Problem Says... | Think Pattern... |
|----------------|------------------|
| "Numbers in range [1..n]" + "Find missing/duplicate" | **Index Marking** |
| "Constant space" + "In-place modification OK" | **Index Marking** or **Two Pointers** |
| "Find two numbers that sum to X" | **Two Pointers** or **Hash Map** |
| "All elements except one appear twice" | **XOR** |
| "Shortest path in grid" | **BFS** |
| "All possible paths" | **DFS** or **Backtracking** |
| "Optimize subsequence/subset" | **DP** |

---

## Folder Structure

Each pattern folder contains:

```
pattern-name/
├── README.md              # Main documentation
├── concepts/              # Theory and explanations
│   ├── 01_core_principle.md
│   ├── 02_why_technique_works.md
│   └── ...
└── problems/              # LeetCode solutions
    ├── 01_problem_name.py
    ├── 02_problem_name.py
    └── ...
```

---

## Contribution Guidelines

When adding a new pattern:

1. **Create comprehensive README**
   - What is this pattern?
   - When to use it?
   - Base template
   - Common variants
   - Mental checklist

2. **Add concept files**
   - Explain from first principles
   - Use analogies
   - Show visual examples
   - Cover edge cases

3. **Include practice problems**
   - Multiple approaches
   - Detailed comments
   - Test cases
   - Dry run examples

---

## Learning Path

### Beginner (Start Here)
1. ✅ **Two Pointers** - Master array manipulation (COMPLETE: 8/12 problems)
2. ✅ **Index Marking** - Learn in-place techniques (COMPLETE!)
3. 🚧 **Sliding Window** - Understand subarray patterns

### Intermediate
1. Binary Search Variants
2. DFS/BFS Templates
3. Basic DP Patterns

### Advanced
1. Advanced DP (State Machine, Bitmask)
2. Segment Trees
3. Advanced Graph Algorithms

---

## Quick Reference

### Most Important Patterns for Interviews

1. **Two Pointers** (LC: 50+ problems)
2. **Sliding Window** (LC: 40+ problems)
3. **Binary Search** (LC: 60+ problems)
4. **DFS/BFS** (LC: 100+ problems)
5. **DP** (LC: 150+ problems)
6. **Index Marking** (LC: 10 problems, but impressive!)

---

## Resources

### External References
- [LeetCode Patterns](https://seanprashad.com/leetcode-patterns/)
- [14 Patterns to Ace Any Coding Interview](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)

### Books
- "Grokking Algorithms" - Visual explanations
- "Elements of Programming Interviews" - Pattern-based approach
- "Cracking the Coding Interview" - Interview prep

---

## Statistics

| Pattern | Problems | Avg Difficulty | Interview % |
|---------|----------|----------------|-------------|
| Index Marking | 10 | Medium | 15% |
| Two Pointers | 50+ | Easy-Medium | 40% |
| Sliding Window | 40+ | Medium | 35% |
| Binary Search | 60+ | Medium-Hard | 30% |

---

**Last Updated**: 2025-12-20
**Total Patterns**: 2 (Index Marking ✅, Two Pointers ✅)
**Total Problems**: 12+ (4 Index Marking + 8 Two Pointers variants)
