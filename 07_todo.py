"""
TASK 7 — Build a real thing

A command-line to-do manager. Everything from tasks 1-6, in one file.

Requirements
------------
  * A `Task` class with: title, done (default False), and a __str__
  * Load from and save to todos.json in this folder
  * A menu loop: add / list / complete / delete / quit
  * Bad input never crashes the program — wrap parsing in try/except
  * The entry-point guard at the bottom (already written for you)

The json module
---------------
    JS: JSON.stringify(data)      Python: json.dumps(data)      -> string
    JS: JSON.parse(text)          Python: json.loads(text)      -> object

    ...and the file versions, which JS has no direct equivalent for:
        json.dump(data, file)   writes straight to an open file
        json.load(file)         reads straight from an open file

    (dumpS / loadS = "to/from String". The ones without the S take a file.)

Reading and writing files
-------------------------
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

`with` auto-closes the file even if something raises — it is the closest
thing Python has to a try/finally you don't have to write.

`if __name__ == "__main__":`
---------------------------
This block runs only when the file is executed directly, NOT when another
file imports it. It is the guard that lets a file be both a runnable script
and an importable module. There's no exact JS equivalent — the nearest
cousin is checking `require.main === module` in CommonJS.

Stretch goals, once it works
----------------------------
  * add a due date and sort by it
  * add priorities and filter the list view
  * split Task into its own file and import it — you'll need the guard then
  * write test_todo.py and run `pytest`
"""

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "todos.json")


class Task:
    def __init__(self, title, done=False):
        # YOUR CODE HERE
        pass

    def __str__(self):
        """e.g. '[x] Buy milk' when done, '[ ] Buy milk' when not."""
        # YOUR CODE HERE
        pass

    def to_dict(self):
        """Return {"title": ..., "done": ...} so json can serialise it.
        json.dump cannot serialise your custom class directly."""
        # YOUR CODE HERE
        pass

    @staticmethod
    def from_dict(d):
        """Rebuild a Task from a plain dict loaded out of JSON.

        @staticmethod means 'no self' — it's a function that lives on the
        class. Closest JS equivalent: a `static` class method."""
        # YOUR CODE HERE
        pass


def load_tasks():
    """
    Return a list of Task objects from DATA_FILE.
    If the file doesn't exist yet, return an empty list — don't crash.
    Check with os.path.exists(DATA_FILE).
    """
    # YOUR CODE HERE
    pass


def save_tasks(tasks):
    """Write the list of Tasks to DATA_FILE as JSON."""
    # YOUR CODE HERE
    pass


def show_menu():
    print("\n1. Add   2. List   3. Complete   4. Delete   5. Quit")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("> ").strip()

        # YOUR CODE HERE
        #
        # Handle each choice. Sketch:
        #   "1" -> input a title, append Task(title), save
        #   "2" -> print each task with its number (enumerate, start=1)
        #   "3" -> input a number, mark that task done, save
        #   "4" -> input a number, remove that task, save
        #   "5" -> print goodbye, break
        #   anything else -> "Unknown option"
        #
        # For "3" and "4": the user types "2" but the list index is 1.
        # An out-of-range index raises IndexError, and a non-number raises
        # ValueError. Catch both and print a friendly message rather than
        # letting the program die.
        #
        # Once the if/elif chain works, try rewriting it as a `match`
        # statement — Python 3.10+, and much closer to a JS switch:
        #
        #     match choice:
        #         case "1": ...
        #         case "5": break
        #         case _:   print("Unknown option")

        break  # DELETE THIS once your loop handles choices


if __name__ == "__main__":
    main()
