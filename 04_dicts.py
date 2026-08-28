"""
TASK 4 — Dicts are not objects

JavaScript lets you blur objects and maps. Python does not.

    JS:      student.name        student["name"]      both work
    Python:  student["name"]     only this works

    student.name          -> AttributeError
    student["email"]      -> KeyError   (NOT undefined!)
    student.get("email")  -> None       (the safe version)

That second one is the real trap. In JS a missing property quietly gives you
`undefined` and your code limps on. In Python it raises immediately.

Use square brackets when the key MUST be there (a bug if it isn't).
Use .get() when absence is legitimate.
"""

STUDENTS = [
    {"name": "Ana", "scores": [80, 92, 75]},
    {"name": "Bo", "scores": [55, 61, 70]},
    {"name": "Cy", "scores": [90, 88, 94]},
]


def average(student):
    """
    Return the mean of a student's scores, rounded to 1 decimal place.
    Builtins you want: sum(), len(), round(x, 1)
    """
    # YOUR CODE HERE
    pass


def top_student(students):
    """
    Return the name of the student with the highest average.

    Two ways — try the second once the first works:
      1. a loop tracking the best so far
      2. max(students, key=average)   <- `key` is like JS sort's comparator,
                                         but it returns a value, not -1/0/1
    """
    # YOUR CODE HERE
    pass


def get_email(student):
    """
    Return the student's email, or "no email on file" if the key is absent.
    Use .get() with a default — do NOT use try/except here.
    """
    # YOUR CODE HERE
    pass


def add_grade(students):
    """
    Return a NEW list of dicts, each with an extra "grade" key based on
    the student's average:  >=80 Excellence, >=65 Merit, >=50 Achieved,
    otherwise Not Achieved.

    Do not mutate the input. To copy a dict and add a key:
        {**student, "grade": g}        <- yes, spread works, same as JS
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
    print("--- Task 4: dicts ---")
    check("average(STUDENTS[0])", average(STUDENTS[0]), 82.3)
    check("average(STUDENTS[1])", average(STUDENTS[1]), 62.0)
    check("top_student(STUDENTS)", top_student(STUDENTS), "Cy")
    check(
        "get_email(STUDENTS[0])",
        get_email(STUDENTS[0]),
        "no email on file",
    )
    check(
        "get_email({'name': 'Di', 'email': 'di@x.nz'})",
        get_email({"name": "Di", "email": "di@x.nz"}),
        "di@x.nz",
    )

    graded = add_grade(STUDENTS)
    check(
        "add_grade -> grades",
        [s["grade"] for s in graded] if graded else None,
        ["Excellence", "Achieved", "Excellence"],
    )
    check(
        "add_grade did not mutate input",
        "grade" in STUDENTS[0],
        False,
    )
