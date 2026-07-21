# R1 Drills — Full Problem Statements

Practice conditions: blank Word doc, no interpreter, 5 min/question. Solutions are in
`solutions_write.py` and `solutions_read.py` in this folder — both runnable
(`python solutions_write.py` executes self-tests).

---

## Part A — Write from scratch

### Tier 1 — Warm-ups

**W1 — Leap year.**
Write a function `is_leap(year)` that returns `True` if `year` is a leap year, else `False`.
A year is a leap year if it is divisible by 4 — except century years (divisible by 100),
which are leap years only if also divisible by 400.
Examples: `2024 → True`, `1900 → False`, `2000 → True`, `2023 → False`.

**W2 — FizzBuzz.**
Print the numbers 1 to 100, one per line — but for multiples of 3 print `Fizz`, for
multiples of 5 print `Buzz`, and for multiples of both print `FizzBuzz`.
First 5 lines: `1, 2, Fizz, 4, Buzz`.

**W3 — Prime check.**
Write `is_prime(n)` returning `True` if `n` is a prime number (divisible only by 1 and
itself; primes start at 2).
Examples: `2 → True`, `9 → False`, `17 → True`, `1 → False`, `0 → False`.

**W4 — Factorial, two ways.**
Write `fact_loop(n)` using a loop and `fact_rec(n)` using recursion, both returning n!
(`fact(5) = 120`, `fact(0) = 1`).

**W5 — Reverse a string.**
Write `reverse(s)` that returns the string reversed, WITHOUT using slicing. Then state the
slicing one-liner. Example: `"sarvam" → "mavras"`.

**W6 — Palindrome.**
Write `is_pal(s)` returning `True` if `s` reads the same forwards and backwards, ignoring
case and spaces. Examples: `"Nurses Run" → True`, `"hello" → False`, `"madam" → True`.

**W7 — Fibonacci.**
Write `fib(n)` that prints the first `n` Fibonacci numbers (sequence starts 0, 1; each next
number is the sum of the previous two). `fib(6)` prints: 0 1 1 2 3 5.

**W8 — Sum of digits, two ways.**
Write `digit_sum(n)` returning the sum of the digits of integer `n` — once by converting to
a string, once with pure arithmetic (% and //). Examples: `123 → 6`, `999 → 27`, `-45 → 9`
(treat negatives by absolute value).

**W9 — Largest without max().**
Write `largest(nums)` returning the biggest number in a non-empty list, without using
`max()` or `sorted()`. Must work for all-negative lists: `[-5, -2, -9] → -2`.

**W10 — Count vowels.**
Write `count_vowels(s)` returning how many vowels (a e i o u, either case) appear in `s`.
Example: `"Sarvam AI" → 4`.

**W11 — Swap without temp.**
Two variables `a = 5`, `b = 9`. Swap their values without using a third variable.

**W12 — GCD.**
Write `gcd(a, b)` returning the greatest common divisor using Euclid's algorithm
(repeatedly replace the pair (a, b) with (b, a % b) until b is 0).
Examples: `gcd(48, 18) → 6`, `gcd(7, 13) → 1`.

### Tier 2 — Strings & collections

**W13 — Word frequency.**
Write `word_freq(sentence)` returning a dict mapping each word (lowercased) to how many
times it appears. Example: `"the cat and the dog" → {"the": 2, "cat": 1, "and": 1, "dog": 1}`.

**W14 — First non-repeating character.**
Write `first_unique(s)` returning the first character that appears exactly once in `s`, or
`None` if there is none. Examples: `"swiss" → "w"`, `"aabb" → None`.

**W15 — Anagrams.**
Write `is_anagram(a, b)` returning `True` if the two strings contain exactly the same
letters in any order (ignore case). Examples: `("listen", "silent") → True`,
`("hello", "world") → False`.

**W16 — Dedupe preserving order.**
Write `dedupe(items)` that removes duplicates from a list while keeping the first
occurrence order. Example: `[3, 1, 3, 2, 1] → [3, 1, 2]`. (Note: `set()` alone loses order.)

**W17 — Second largest.**
Write `second_largest(nums)` returning the second-biggest value in a list of distinct
numbers. Example: `[10, 4, 7, 9] → 9`.

**W18 — Merge two sorted lists.**
Write `merge(a, b)` that merges two already-sorted lists into one sorted list WITHOUT using
`sort()`/`sorted()` — walk both lists with two indexes.
Example: `([1, 4, 6], [2, 3, 7]) → [1, 2, 3, 4, 6, 7]`.

**W19 — Flatten one level.**
Write `flatten(lists)` turning a list of lists into a single list (one level deep only).
Example: `[[1, 2], [3], [4, 5]] → [1, 2, 3, 4, 5]`.

**W20 — Invert a dict.**
Write `invert(d)` swapping keys and values (assume values are unique and hashable).
Example: `{"a": 1, "b": 2} → {1: "a", 2: "b"}`.

**W21 — Chunk a list.**
Write `chunk(items, k)` splitting a list into consecutive batches of size `k` (last batch
may be smaller). Example: `([1,2,3,4,5,6,7], 3) → [[1,2,3], [4,5,6], [7]]`.

### Tier 3 — Applied

**W22 — Parse a config string.**
Write `parse(s)` turning `"name=Asha;age=30;city=Pune"` into
`{"name": "Asha", "age": "30", "city": "Pune"}`. Pairs are separated by `;`, keys from
values by the FIRST `=` (values may contain `=`).

**W23 — Error log summary.**
Write `error_summary(lines)` that, given a list of log-line strings, returns a tuple:
(count of lines containing `"ERROR"`, list of the first 3 such lines).

**W24 — Top 2 scorers.**
Given a list of `(name, score)` tuples like `[("asha", 91), ("ravi", 78), ("meena", 95)]`,
write `top2(scores)` returning the names of the two highest scorers in order:
`["meena", "asha"]`.

---

## Part B — Predict the output

Commit to an answer (say it out loud / write it down) before checking. Snippets are in
`solutions_read.py` with expected outputs — run it to verify.

**P1**
```python
def add(item, items=[]):
    items.append(item)
    return items

print(add(1))
print(add(2))
```

**P2**
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

**P3**
```python
print(7 // 2, 7 / 2, 7 % 2, 2 ** 3)
```

**P4**
```python
s = "hello"
s.upper()
print(s)
```

**P5**
```python
nums = [3, 1, 2]
result = nums.sort()
print(result, nums)
```

**P6**
```python
s = "sarvam"
print(s[1:4], s[-3:], s[::-1])
```

**P7**
```python
nums = [1, 2, 3, 4, 5, 6]
out = [x * x for x in nums if x % 2 == 0]
print(out)
```

**P8**
```python
try:
    print("a")
    x = 1 / 0
    print("b")
except ZeroDivisionError:
    print("c")
finally:
    print("d")
```

**P9**
```python
d = {"a": 1}
print(d.get("b"))
print(d.get("b", 0))
print(d["b"])
```

**P10**
```python
for i in range(1, 5):
    pass
print(i)
```

---

## Part C — Spot the bug

For each: what's wrong, what misbehaves, and the fix. Buggy + fixed versions are in
`solutions_read.py`.

**B1** — leap year:
```python
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 and year % 400 == 0)
```

**B2** — sum of a list:
```python
def total(nums):
    s = 0
    for i in range(len(nums) - 1):
        s += nums[i]
    return s
```

**B3** — remove even numbers:
```python
nums = [1, 2, 3, 4, 5, 6]
for x in nums:
    if x % 2 == 0:
        nums.remove(x)
```

**B4** — does the list contain a negative?
```python
def find_negative(nums):
    for x in nums:
        if x < 0:
            return True
        else:
            return False
```

**B5** — build a message:
```python
count = 5
message = "Processed " + count + " files"
```

**B6** — pair up elements:
```python
list = [1, 2, 3]
pairs = list(zip(list, list))
```
