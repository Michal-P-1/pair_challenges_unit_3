# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def extract_uppercase(mixed_words):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a list of strings, each one a word (e.g. ["WORLD"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.


def allow_access(date_of_birth):
    example_date_list = date_of_birth.split("-")
    date_year = int(example_date_list[0])
    date_month = int(example_date_list[1])
    date_day = int(example_date_list[2])
    current_date = datetime.date.today()

    user_date_of_birth = datetime.date(date_year, date_month, date_day)
    age = relativedelta.relativedelta(current_date , user_date_of_birth)

    if age < 16:
        return f"No access. Your current age is {age} and the required age is 16"
    else:
        return "Access allowed"

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Test if the entered format is correct
"""
def test_correct_format_entered():
    assert allow_access(1999) == "Entered year has to be string"

"""
Test access denied if under 16
"""
def test_access_denied():
    assert allow_access("2010-12-12") == "No access"

"""
Test access granted
"""
def test_access_granted():
    assert allow_access("2006-12-12") == "Access allowed"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
