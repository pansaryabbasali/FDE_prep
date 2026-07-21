"""R1 Drills - solutions for Part A (write-from-scratch W1-W24).

Run me: python solutions_write.py
Every solution is verified by the asserts at the bottom.
"""


# ---------- Tier 1: warm-ups ----------

def is_leap(year):
    # divisible by 4, EXCEPT centuries, UNLESS divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def fizzbuzz():
    # check 15 first - order of conditions is the classic trap
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def is_prime(n):
    if n < 2:
        return False
    # checking up to sqrt(n) is enough: a factor above sqrt(n)
    # implies a matching factor below it
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fact_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fact_rec(n):
    return 1 if n <= 1 else n * fact_rec(n - 1)


def reverse(s):
    out = ""
    for ch in s:
        out = ch + out  # prepend each char
    return out
    # one-liner alternative: s[::-1]


def is_pal(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


def fib(n):
    """Return (rather than print) the first n Fibonacci numbers."""
    out = []
    a, b = 0, 1
    for _ in range(n):
        out.append(a)
        a, b = b, a + b  # tuple unpacking avoids a temp variable
    return out


def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))


def digit_sum_math(n):
    n, total = abs(n), 0
    while n:
        total += n % 10  # last digit
        n //= 10         # drop last digit
    return total


def largest(nums):
    # initialize from the list itself, NOT 0 - all-negative lists
    # would break a zero-initialized version
    biggest = nums[0]
    for x in nums[1:]:
        if x > biggest:
            biggest = x
    return biggest


def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")


def swap(a, b):
    a, b = b, a
    return a, b


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# ---------- Tier 2: strings & collections ----------

def word_freq(sentence):
    counts = {}
    for word in sentence.lower().split():
        counts[word] = counts.get(word, 0) + 1  # .get(key, default) idiom
    return counts


def first_unique(s):
    # O(n^2) but fine at this level; two-pass dict-count version is O(n)
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None


def is_anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())


def dedupe(items):
    seen, out = set(), []
    for x in items:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def second_largest(nums):
    first = second = float("-inf")
    for x in nums:
        if x > first:
            first, second = x, first
        elif x > second:
            second = x
    return second
    # simpler alternative: sorted(nums)[-2]


def merge(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])  # one of these two is already empty
    out.extend(b[j:])
    return out


def flatten(lists):
    out = []
    for sub in lists:
        out.extend(sub)
    return out
    # comprehension form: [x for sub in lists for x in sub]


def invert(d):
    return {v: k for k, v in d.items()}


def chunk(items, k):
    # slicing past the end is safe in Python - the last chunk just comes
    # out shorter
    return [items[i:i + k] for i in range(0, len(items), k)]


# ---------- Tier 3: applied ----------

def parse(s):
    out = {}
    for pair in s.split(";"):
        key, value = pair.split("=", 1)  # maxsplit=1: values may contain '='
        out[key] = value
    return out


def error_summary(lines):
    errors = [ln for ln in lines if "ERROR" in ln]
    return len(errors), errors[:3]


def top2(scores):
    ranked = sorted(scores, key=lambda pair: pair[1], reverse=True)
    return [name for name, _ in ranked[:2]]


# ---------- self-tests ----------

if __name__ == "__main__":
    assert is_leap(2024) and is_leap(2000) and not is_leap(1900) and not is_leap(2023)
    assert is_prime(2) and is_prime(17) and not is_prime(9) and not is_prime(1)
    assert fact_loop(5) == fact_rec(5) == 120 and fact_loop(0) == 1
    assert reverse("sarvam") == "mavras"
    assert is_pal("Nurses Run") and not is_pal("hello")
    assert fib(6) == [0, 1, 1, 2, 3, 5]
    assert digit_sum(123) == digit_sum_math(123) == 6
    assert digit_sum(-45) == 9
    assert largest([-5, -2, -9]) == -2
    assert count_vowels("Sarvam AI") == 4
    assert swap(5, 9) == (9, 5)
    assert gcd(48, 18) == 6 and gcd(7, 13) == 1
    assert word_freq("the cat and the dog")["the"] == 2
    assert first_unique("swiss") == "w" and first_unique("aabb") is None
    assert is_anagram("listen", "silent") and not is_anagram("hello", "world")
    assert dedupe([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert second_largest([10, 4, 7, 9]) == 9
    assert merge([1, 4, 6], [2, 3, 7]) == [1, 2, 3, 4, 6, 7]
    assert flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert chunk([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]]
    assert parse("name=Asha;age=30;city=Pune") == {"name": "Asha", "age": "30", "city": "Pune"}
    assert error_summary(["ok", "ERROR x", "ERROR y"]) == (2, ["ERROR x", "ERROR y"])
    assert top2([("asha", 91), ("ravi", 78), ("meena", 95)]) == ["meena", "asha"]
    print("All W1-W24 solutions pass.")
