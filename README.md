# Python Practice — JS → Python translation

Seven tasks. Each file has the original JavaScript in a comment block, a stub to
fill in, and self-checks at the bottom so you get instant pass/fail feedback.

## How to run

From this folder:

    python 01_syntax_reflex.py

Every file prints a checklist. Fill in the stubs until everything is `PASS`.

## Order

| File | Focus | Time |
|---|---|---|
| `01_syntax_reflex.py` | indentation, `:`, `return`, f-strings | 30 min |
| `02_loops.py` | `range`, `enumerate`, `.items()`, `zip` | 45 min |
| `03_comprehensions.py` | replacing `.map()` / `.filter()` | 1 hr |
| `04_dicts.py` | dicts are not objects | 45 min |
| `05_classes.py` | `self`, `__init__`, `__str__` | 1 hr |
| `06_errors_truthiness.py` | `except`, `raise`, falsy `[]` and `{}` | 30 min |
| `07_todo.py` | full CLI app, JSON persistence | 2–3 hrs |

## Swap table

| JavaScript | Python |
|---|---|
| `{ }` blocks, `;` | indentation + `:` |
| `let` / `const` | just `x = 5` |
| `null` / `undefined` | `None` |
| `===` / `==` | `==` (value), `is` (identity — only for `None`/`True`/`False`) |
| `` `Hi ${name}` `` | `f"Hi {name}"` |
| `arr.map(f)` | `[f(x) for x in arr]` |
| `arr.filter(f)` | `[x for x in arr if cond]` |
| `{a: 1}` object | `{"a": 1}` dict — access `d["a"]`, never `d.a` |
| `this` | `self` (first parameter of every method) |
| `new Thing()` | `Thing()` |
| `arr.length` | `len(arr)` |
| `try/catch` | `try/except` |
| `throw new Error(x)` | `raise ValueError(x)` |
| `console.log` | `print` |
| `//` | `#` |
| `&&` `\|\|` `!` | `and` `or` `not` |

## After task 3

    pip install pytest black

`pytest` is your Jest (files named `test_*.py`, functions named `test_*`, plain
`assert`). `black` is your Prettier — run `black .` and stop thinking about it.
