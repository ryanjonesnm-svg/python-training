"""
TASK 3 — Comprehensions (the big one)

This is where Python stops looking like JavaScript. There is no idiomatic
.map() or .filter(). There is one form that does both:

    [ expression  for item in iterable  if condition ]
      ^ the map     ^ the loop            ^ the filter

Read it left to right as: "give me EXPRESSION, for each ITEM, where CONDITION".

--- ORIGINAL JAVASCRIPT ---------------------------------------------------

    const nums = [1,2,3,4,5,6,7,8,9,10];

    const evens       = nums.filter(n => n % 2 === 0);
    const doubled     = nums.map(n => n * 2);
    const evenSquares = nums.filter(n => n % 2 === 0).map(n => n ** 2);
    const words       = ["apple","fig","banana"]
                          .filter(w => w.length > 3)
                          .map(w => w.toUpperCase());

---------------------------------------------------------------------------

Note the chained case: in JS that is two passes. In Python it is ONE
comprehension — the filter and the map live in the same set of brackets.

CHECKPOINT: if you're still writing `result = []` then `result.append(...)`
for a simple transform after this task, you haven't landed it yet.
"""

NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def evens(nums):
    """[2, 4, 6, 8, 10] — filter only."""
    # YOUR CODE HERE
    pass


def doubled(nums):
    """[2, 4, 6, ..., 20] — map only."""
    # YOUR CODE HERE
    pass


def even_squares(nums):
    """[4, 16, 36, 64, 100] — filter AND map in one comprehension."""
    # YOUR CODE HERE
    pass


def long_words_upper(words):
    """['APPLE', 'BANANA'] — words longer than 3 chars, uppercased."""
    # YOUR CODE HERE
    pass


def name_lengths(names):
    """
    DICT comprehension. Given ["ana", "bo", "cy"] return
    {"ana": 3, "bo": 2, "cy": 2}.

    Same shape, curly braces, and a key:value expression:
        { key_expr: value_expr for item in iterable }
    """
    # YOUR CODE HERE
    pass


def flatten(rows):
    """
    NESTED comprehension. Given [[1, 2], [3, 4]] return [1, 2, 3, 4].

    The two `for` clauses read in the SAME order you'd write nested loops:
        [x for row in rows for x in row]
    """
    # YOUR CODE HERE
    pass


# ---------------------------------------------------------------------------
# Self-checks — don't edit below this line.
# ---------------------------------------------------------------------------

def check(label, got, want):
    status = "PASS" if got == want else "FAIL"
    print(f"[{status}] {label}: got {got!r}, want {want!r}")


if __name__ == "__main__":
    print("--- Task 3: comprehensions ---")
    check("evens(NUMS)", evens(NUMS), [2, 4, 6, 8, 10])
    check("doubled(NUMS)", doubled(NUMS), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
    check("even_squares(NUMS)", even_squares(NUMS), [4, 16, 36, 64, 100])
    check(
        "long_words_upper(['apple', 'fig', 'banana'])",
        long_words_upper(["apple", "fig", "banana"]),
        ["APPLE", "BANANA"],
    )
    check(
        "name_lengths(['ana', 'bo', 'cy'])",
        name_lengths(["ana", "bo", "cy"]),
        {"ana": 3, "bo": 2, "cy": 2},
    )
    check("flatten([[1, 2], [3, 4]])", flatten([[1, 2], [3, 4]]), [1, 2, 3, 4])
