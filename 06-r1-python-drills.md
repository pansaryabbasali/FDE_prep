# R1 Python Drills — Questions Only (printable / Word-doc practice)

Answers with explanations are on the dashboard → **R1 Drills** tab
(https://pansaryabbasali.github.io/FDE_prep/). Protocol: write in a blank doc, no running,
5 min/question max; only then paste into Python, run, and log every slip in `notes.md`.

## Part A — Write from scratch

**Tier 1: warm-ups**
1. W1 — `is_leap(year)`: True if leap year. (The confirmed example question.)
2. W2 — FizzBuzz 1–100 (3→Fizz, 5→Buzz, both→FizzBuzz).
3. W3 — `is_prime(n)`.
4. W4 — Factorial: once with a loop, once with recursion.
5. W5 — Reverse a string without slicing; then the one-liner.
6. W6 — Palindrome check ignoring case and spaces.
7. W7 — Print the first n Fibonacci numbers.
8. W8 — Sum of digits of an integer (string way and math way).
9. W9 — Largest number in a list without max().
10. W10 — Count vowels in a string.
11. W11 — Swap two variables without a temp.
12. W12 — GCD of two numbers (Euclid).

**Tier 2: strings & collections**
13. W13 — Sentence → dict of word counts.
14. W14 — First non-repeating character ("swiss" → "w").
15. W15 — Are two strings anagrams?
16. W16 — Remove duplicates from a list, preserving order.
17. W17 — Second largest number in a list.
18. W18 — Merge two sorted lists into one sorted list, no sort().
19. W19 — Flatten a list of lists, one level.
20. W20 — Invert a dict (unique values).
21. W21 — Chunk a list into batches of size k.

**Tier 3: applied**
22. W22 — Parse "name=Asha;age=30;city=Pune" into a dict.
23. W23 — From a list of log lines: count lines containing "ERROR", return the first 3.
24. W24 — From [(name, score), ...]: names of the top 2 scorers.

## Part B — Predict the output (commit to an answer before checking)

P1 — mutable default argument (`def add(item, items=[])`, called twice)
P2 — `b = a; b.append(4); print(a)`
P3 — `7 // 2, 7 / 2, 7 % 2, 2 ** 3`
P4 — `s.upper()` without reassignment, then `print(s)`
P5 — `result = nums.sort(); print(result, nums)`
P6 — `s[1:4], s[-3:], s[::-1]` for s = "sarvam"
P7 — `[x*x for x in nums if x % 2 == 0]` for [1..6]
P8 — try / ZeroDivisionError / except / finally print order
P9 — `d.get("b")`, `d.get("b", 0)`, `d["b"]` on {"a": 1}
P10 — value of loop variable `i` after `for i in range(1, 5)`

## Part C — Spot the bug (name the fix)

B1 — leap year with `and (… != 0 and … % 400 == 0)`
B2 — `for i in range(len(nums) - 1)` in a sum
B3 — `nums.remove(x)` while iterating `nums`
B4 — `return False` inside the loop's else on first iteration
B5 — `"Processed " + count + " files"` with count = 5
B6 — variable named `list`, then calling `list(...)`

## Session plan

1. Session 1 (40 min): W1–W12 → run → log slips
2. Session 2 (40 min): W13–W24 → run → log slips
3. Session 3 (30 min): P1–P10 + B1–B6, answers out loud first
4. Retry pass (20 min): re-write only the misses

**Passing bar:** Tier 1 flawless and fast (≤3 min each) · Tier 2 correct with minor slips ·
every P/B trap recognized.
