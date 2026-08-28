"""
TASK 1 — Syntax reflex

Goal: get IndentationError and "missing colon" out of your system.
No new logic. Translate the JavaScript below, line for line.

--- ORIGINAL JAVASCRIPT ---------------------------------------------------

    function grade(score) {
      if (score >= 80) { return "Excellence"; }
      else if (score >= 65) { return "Merit"; }
      else if (score >= 50) { return "Achieved"; }
      return "Not Achieved";
    }

    const total = (prices) => prices.reduce((a, b) => a + b, 0);

    function greet(name = "world") { return `Hello, ${name}!`; }

---------------------------------------------------------------------------

Reminders:
  * `else if` is spelled `elif`
  * every `if` / `def` line ends with a colon
  * the body is indented 4 spaces — that IS the block, there are no braces
  * for `total`, do NOT reach for reduce. Python has a builtin: sum()
  * `f"..."` is the template literal
"""


def grade(score):
    # YOUR CODE HERE
    pass


def total(prices):
    # YOUR CODE HERE
    pass


def greet(name="world"):
    # YOUR CODE HERE
    pass


# ---------------------------------------------------------------------------
# Self-checks — don't edit below this line.
# ---------------------------------------------------------------------------

def check(label, got, want):
    status = "PASS" if got == want else "FAIL"
    print(f"[{status}] {label}: got {got!r}, want {want!r}")


if __name__ == "__main__":
    print("--- Task 1: syntax reflex ---")
    check("grade(95)", grade(95), "Excellence")
    check("grade(70)", grade(70), "Merit")
    check("grade(50)", grade(50), "Achieved")
    check("grade(12)", grade(12), "Not Achieved")
    check("total([1, 2, 3])", total([1, 2, 3]), 6)
    check("total([])", total([]), 0)
    check("greet('Ana')", greet("Ana"), "Hello, Ana!")
    check("greet()", greet(), "Hello, world!")
