import pytest
from ason import ason
def test_given_usage_example():
    x = '{ "${key1}":"John", "age":30, "city":"${city}", "hobbies": [], "nested": { "inner_key": "${inner_value}" } }'

    y = ason.loads(x)

    # Set values for variables
    y.set("city", "New York")
    y.set("key1", "name")

    # Replace key dynamically
    y.replace("age", "new_age", 25)

    # Append a value to the 'hobbies' list
    y.append("hobbies", "Reading")
    y.append("hobbies", "Reading")
    y.append("hobbies", "Reading")

    # Set nested variable
    y.set("inner_value", "NestedValue")

    # Display age, name, and nested value
    assert y["new_age"] == 25
    assert y["name"] == "John"  # Adjusted based on the previous code
    assert y["nested"] == {'inner_key': 'NestedValue'}

    # Print the result
    b = y.dumps()
    assert isinstance(b, dict)  # Ensure it's a dictionary
    assert b["city"] == "New York"
   # assert b["key1"] == "name"
    assert b["new_age"] == 25
    assert b["hobbies"] == ["Reading", "Reading", "Reading"]
    assert b["nested"] == {'inner_key': 'NestedValue'}
