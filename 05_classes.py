"""
TASK 5 — Classes and `self`

--- ORIGINAL JAVASCRIPT ---------------------------------------------------

    class BankAccount {
      constructor(owner, balance = 0) {
        this.owner = owner;
        this.balance = balance;
      }
      deposit(amount) {
        if (amount <= 0) throw new Error("Must be positive");
        this.balance += amount;
        return this.balance;
      }
      withdraw(amount) {
        if (amount > this.balance) throw new Error("Insufficient funds");
        this.balance -= amount;
        return this.balance;
      }
      toString() { return `${this.owner}: $${this.balance}`; }
    }

    const acct = new BankAccount("Ana", 100);

---------------------------------------------------------------------------

The mapping:

    constructor(...)        ->  def __init__(self, ...)
    this.owner              ->  self.owner
    toString()              ->  def __str__(self)
    new BankAccount("Ana")  ->  BankAccount("Ana")      no `new` keyword
    throw new Error(msg)    ->  raise ValueError(msg)

THE #1 BEGINNER ERROR: `self` is not implicit like `this`. You must type it as
the first parameter of every method. Forget it and you get

    TypeError: deposit() takes 1 positional argument but 2 were given

...which never mentions `self`. Now you know what it means.
"""


class BankAccount:
    def __init__(self, owner, balance=0):
        # YOUR CODE HERE — set self.owner and self.balance
        pass

    def deposit(self, amount):
        """Raise ValueError('Must be positive') if amount <= 0.
        Otherwise add it and return the new balance."""
        # YOUR CODE HERE
        pass

    def withdraw(self, amount):
        """Raise ValueError('Insufficient funds') if amount > balance.
        Otherwise subtract it and return the new balance."""
        # YOUR CODE HERE
        pass

    def __str__(self):
        """Return e.g. 'Ana: $100'. This is what print(acct) shows."""
        # YOUR CODE HERE
        pass


class SavingsAccount(BankAccount):
    """
    Inheritance. `extends BankAccount` -> `(BankAccount)` in the class line.

    Takes an extra `rate` (e.g. 0.05 for 5%). In __init__ you must call the
    parent constructor first:

        super().__init__(owner, balance)      # JS: super(owner, balance)

    Then add one new method, add_interest(), which deposits balance * rate
    and returns the new balance.
    """

    def __init__(self, owner, balance=0, rate=0.05):
        # YOUR CODE HERE
        pass

    def add_interest(self):
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
    print("--- Task 5: classes ---")
    acct = BankAccount("Ana", 100)
    check("acct.owner", acct.owner, "Ana")
    check("acct.balance", acct.balance, 100)
    check("acct.deposit(50)", acct.deposit(50), 150)
    check("acct.withdraw(30)", acct.withdraw(30), 120)
    check("str(acct)", str(acct), "Ana: $120")
    check("default balance", BankAccount("Bo").balance, 0)

    check_raises("deposit(-5)", lambda: acct.deposit(-5), ValueError)
    check_raises("withdraw(9999)", lambda: acct.withdraw(9999), ValueError)

    print("--- inheritance ---")
    sav = SavingsAccount("Cy", 200, 0.10)
    check("sav.owner", sav.owner, "Cy")
    check("sav inherits deposit", sav.deposit(100), 300)
    check("sav.add_interest()", sav.add_interest(), 330.0)
    check("isinstance check", isinstance(sav, BankAccount), True)
