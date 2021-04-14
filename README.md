# EE458, excuse me?

Adapted from Java code because I don't have JVM installed locally.

Intended to serve as demo code for 1-N object design model.

## Definition

The definition of objects can be found at [definition.py](definition.py).

An `Advertiser` can hold multiple `Account`s,

An `Account` may only exist in a single `Advertiser`.

`Account.set_owner` may change its owner.

`Advertiser.add_account` may add an `Account` to its accounts, and vice versa.

## Tests

Test code can be found at [tests.py](tests.py). Run test by executing [main.py](main.py)

``` shell
$ python3 main.py
test_owner (tests.TestAddToDifferentAdvertiser) ... FAIL
test_contains (tests.TestAddToDifferentAdvertiser) ... FAIL
test_owner (tests.TestResetOwner) ... FAIL
test_contains (tests.TestResetOwner) ... FAIL

======================================================================
FAIL: test_owner (tests.TestAddToDifferentAdvertiser)
----------------------------------------------------------------------
AssertionError: unexpectedly None : Who's my owner?

======================================================================
FAIL: test_contains (tests.TestAddToDifferentAdvertiser)
----------------------------------------------------------------------
AssertionError: <Account "alice" owner=None> not found in <Advertiser "daniel" accounts=set()> : I should be one of daniel.

======================================================================
FAIL: test_owner (tests.TestResetOwner)
----------------------------------------------------------------------
AssertionError: unexpectedly None : Who's my owner?

======================================================================
FAIL: test_contains (tests.TestResetOwner)
----------------------------------------------------------------------
AssertionError: <Account "alice" owner=None> not found in <Advertiser "daniel" accounts=set()> : I should be one of daniel.

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=4)
```

So how may I change the owner of an `Account` without setting its owner to `None`(`null`) first?