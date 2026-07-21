"""R1 Drills - Part B (predict the output) and Part C (spot the bug).

Run me: python solutions_read.py
Each P-section prints the snippet's actual output right after the expected
output, so you can verify your predictions. Each B-section shows the buggy
behavior (safely) and the fixed version.
"""


def p1():
    print("P1 expected: [1] then [1, 2] - default list created ONCE, shared across calls")

    def add(item, items=[]):
        items.append(item)
        return items

    print(add(1))
    print(add(2))
    # fix: items=None, then 'if items is None: items = []'


def p2():
    print("P2 expected: [1, 2, 3, 4] - b = a copies the REFERENCE, not the list")
    a = [1, 2, 3]
    b = a
    b.append(4)
    print(a)
    # a real copy: b = a[:] or list(a)


def p3():
    print("P3 expected: 3 3.5 1 8 - // floors, / gives float, % remainder, ** power")
    print(7 // 2, 7 / 2, 7 % 2, 2 ** 3)


def p4():
    print("P4 expected: hello - strings are immutable; .upper() result was discarded")
    s = "hello"
    s.upper()
    print(s)


def p5():
    print("P5 expected: None [1, 2, 3] - .sort() is in-place and returns None")
    nums = [3, 1, 2]
    result = nums.sort()
    print(result, nums)
    # sorted(nums) is the one that RETURNS a new list


def p6():
    print("P6 expected: arv vam mavras - end-exclusive slice, negative index, reversal")
    s = "sarvam"
    print(s[1:4], s[-3:], s[::-1])


def p7():
    print("P7 expected: [4, 16, 36] - filter evens first, then square")
    nums = [1, 2, 3, 4, 5, 6]
    out = [x * x for x in nums if x % 2 == 0]
    print(out)


def p8():
    print("P8 expected: a c d - 'b' skipped by the exception, finally always runs")
    try:
        print("a")
        x = 1 / 0
        print("b")
    except ZeroDivisionError:
        print("c")
    finally:
        print("d")


def p9():
    print("P9 expected: None, 0, then KeyError - .get is safe, [] raises")
    d = {"a": 1}
    print(d.get("b"))
    print(d.get("b", 0))
    try:
        print(d["b"])
    except KeyError:
        print("KeyError (as expected)")


def p10():
    print("P10 expected: 4 - range(1, 5) ends at 4; loop variable survives the loop")
    for i in range(1, 5):
        pass
    print(i)


# ---------- Part C: spot the bug ----------

def b1():
    print("B1: inner 'and' should be 'or' - as written NO year passes the")
    print("    century check (cannot be non-div-by-100 AND div-by-400). 2000 -> False (wrong).")

    def is_leap_buggy(year):
        return year % 4 == 0 and (year % 100 != 0 and year % 400 == 0)

    def is_leap_fixed(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    print("    buggy(2000):", is_leap_buggy(2000), "| fixed(2000):", is_leap_fixed(2000))


def b2():
    print("B2: range(len(nums) - 1) skips the LAST element (off-by-one).")

    def total_buggy(nums):
        s = 0
        for i in range(len(nums) - 1):
            s += nums[i]
        return s

    def total_fixed(nums):
        s = 0
        for x in nums:  # iterate values directly - no index arithmetic to get wrong
            s += x
        return s

    print("    buggy([1,2,3]):", total_buggy([1, 2, 3]), "| fixed:", total_fixed([1, 2, 3]))


def b3():
    print("B3: mutating a list while iterating it skips elements - the iterator's")
    print("    position shifts when items are removed. Consecutive evens get missed.")
    nums = [1, 2, 2, 3, 4, 4, 5]
    for x in nums[:]:  # even iterating a COPY, remove() is the wrong tool
        if x % 2 == 0:
            nums.remove(x)
    fixed = [x for x in [1, 2, 2, 3, 4, 4, 5] if x % 2 != 0]
    print("    fix - build a new list:", fixed)


def b4():
    print("B4: the else returns False on the FIRST element, so only nums[0] is ever")
    print("    checked. [1, -2] wrongly -> False.")

    def find_negative_fixed(nums):
        for x in nums:
            if x < 0:
                return True
        return False  # only after the WHOLE loop found nothing

    print("    fixed([1, -2]):", find_negative_fixed([1, -2]))


def b5():
    print("B5: str + int raises TypeError - cannot concatenate different types.")
    count = 5
    message = f"Processed {count} files"  # f-string is the fix (or str(count))
    print("    fix:", message)


def b6():
    print("B6: naming a variable 'list' shadows the built-in; list(...) then fails")
    print("    with TypeError because it calls the list OBJECT, not the type.")
    print("    fix: never shadow built-ins (list, dict, str, sum, max, id, type).")


if __name__ == "__main__":
    for fn in (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        fn()
        print("-" * 60)
    for fn in (b1, b2, b3, b4, b5, b6):
        fn()
        print("-" * 60)
