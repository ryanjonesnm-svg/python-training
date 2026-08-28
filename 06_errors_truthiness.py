"""
TASK 6 — Errors and truthiness

Part A: exceptions
------------------
    try { ... } catch (e) { ... } finally { ... }
    try:      ... except ValueError as e: ... finally: ...

    throw new Error("bad")   ->   raise ValueError("bad")

Catch a SPECIFIC exception type. A bare `except:` swallows everything —
including Ctrl-C and genuine bugs — and is the Python equivalent of an empty
catch block that hides your stack trace.

Part B: truthiness — READ THIS TWICE
------------------------------------
    JavaScript:  []  is TRUTHY      {}  is TRUTHY
    Python:      []  is FALSY       {}  is FALSY

Also falsy in Python: 0, 0.0, "", None, set()
Truthy: "0", "false", [0], anything non-empty

This is the single most likely thing to silently break a function you port
from JS. `if (arr)` in JS means "arr exists". `if arr:` in Python means
"arr exists AND has something in it".
"""


def safe_int(text):
    """
    Convert text to an int. If it isn't a valid number, return None.
    int("abc") raises ValueError — catch that specific type.
    """
    # YOUR CODE HERE
    pass


def divide(a, b):
    """
    Return a / b. If b is 0, raise ValueError("Cannot divide by zero").
    Note: Python's own error here is ZeroDivisionError — you're deliberately
    replacing it with a friendlier one.
    """
    # YOUR CODE HERE
    pass


def parse_scores(raw):
    """
    Given a list of strings like ["80", "abc", "92", ""], return only the
    ones that parse as ints: [80, 92].
    Reuse safe_int. A comprehension with an `if` is a clean fit here.
    """
    # YOUR CODE HERE
    pass


def first_or_default(items, default="empty"):
    """
    Return the first item, or `default` if the list is empty.
    Write it using `if not items:` — lean on Python truthiness rather than
    checking len(items) == 0.
    """
    # YOUR CODE HERE
    pass


def truthiness_report():
    """
    Return a dict mapping each value's label to whether Python considers it
    truthy. Predict each answer BEFORE you run the checks.

    Expected keys: "0", "empty string", "empty list", "empty dict",
                   "None", "string zero"
    """
    # YOUR CODE HERE
    pass


# ---------------------------------------------------------------------------
# Self-checks — don't edit below this line.
# ---------------------------------------------------------------------------

def check(label, got, want):
    status = "PASS" if got == want else "FAIL"
    print(f"[{status}] {label}: got {got!r}, want {want!r}")


def check_raises(label, fn, exc_type):
    try:
        fn()
    except exc_type:
        print(f"[PASS] {label}: raised {exc_type.__name__}")
    except Exception as e:
        print(f"[FAIL] {label}: raised {type(e).__name__}, want {exc_type.__name__}")
    else:
        print(f"[FAIL] {label}: nothing raised, want {exc_type.__name__}")


if __name__ == "__main__":
    print("--- Task 6: errors and truthiness ---")
    check("safe_int('42')", safe_int("42"), 42)
    check("safe_int('abc')", safe_int("abc"), None)
    check("safe_int('')", safe_int(""), None)

    check("divide(10, 2)", divide(10, 2), 5.0)
    check_raises("divide(1, 0)", lambda: divide(1, 0), ValueError)

    check(
        "parse_scores(['80', 'abc', '92', ''])",
        parse_scores(["80", "abc", "92", ""]),
        [80, 92],
    )

    check("first_or_default([5, 6])", first_or_default([5, 6]), 5)
    check("first_or_default([])", first_or_default([]), "empty")

    check(
        "truthiness_report()",
        truthiness_report(),
        {
            "0": False,
            "empty string": False,
            "empty list": False,   # <- TRUTHY in JavaScript!
            "empty dict": False,   # <- TRUTHY in JavaScript!
            "None": False,
            "string zero": True,
        },
    )
