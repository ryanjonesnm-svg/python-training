"""
TASK 2 — Loops and iteration

Python has no `for (let i = 0; i < n; i++)`. It has four tools instead.

    range(1, 11)        ->  1, 2, 3 ... 10        (stop value is EXCLUSIVE)
    enumerate(items)    ->  (0, "ana"), (1, "bo")  ... index + value
    d.items()           ->  ("a", 1), ("b", 2)     ... key + value
    zip(a, b)           ->  (a[0], b[0]), ...      ... two lists side by side

--- ORIGINAL JAVASCRIPT ---------------------------------------------------

    const names = ["ana", "bo", "cy"];
    names.forEach((n, i) => console.log(`${i + 1}. ${n.toUpperCase()}`));

---------------------------------------------------------------------------

GOTCHA — the same keyword behaves differently by type:

    for x in my_list:   ->  x is a VALUE   (like JS `for...of`)
    for x in my_dict:   ->  x is a KEY     (like JS `for...in`)

Each function below returns a list so the checks can verify it. Build the list
with .append() inside the loop — comprehensions are task 3, resist for now.
"""


def count_to_ten():
    """Return [1, 2, 3, ..., 10]. Use range()."""
    # YOUR CODE HERE
    pass


def numbered_names(names):
    """
    Given ["ana", "bo"], return ["1. ANA", "2. BO"].
    Use enumerate(). Uppercase in Python is .upper() (no camelCase).
    """
    # YOUR CODE HERE
    pass


def describe_scores(scores):
    """
    Given {"ana": 80, "bo": 55}, return ["ana scored 80", "bo scored 55"].
    Use .items().
    """
    # YOUR CODE HERE
    pass


def pair_up(names, scores):
    """
    Given ["ana", "bo"] and [80, 55], return ["ana: 80", "bo: 55"].
    Use zip().
    """
    # YOUR CODE HERE
    pass


def keys_only(d):
    """
    Given {"ana": 80, "bo": 55}, return ["ana", "bo"].
    Loop the dict directly — prove to yourself you get keys, not values.
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
    print("--- Task 2: loops ---")
    check("count_to_ten()", count_to_ten(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    check(
        "numbered_names(['ana', 'bo', 'cy'])",
        numbered_names(["ana", "bo", "cy"]),
        ["1. ANA", "2. BO", "3. CY"],
    )
    check(
        "describe_scores({'ana': 80, 'bo': 55})",
        describe_scores({"ana": 80, "bo": 55}),
        ["ana scored 80", "bo scored 55"],
    )
    check(
        "pair_up(['ana', 'bo'], [80, 55])",
        pair_up(["ana", "bo"], [80, 55]),
        ["ana: 80", "bo: 55"],
    )
    check(
        "keys_only({'ana': 80, 'bo': 55})",
        keys_only({"ana": 80, "bo": 55}),
        ["ana", "bo"],
    )
