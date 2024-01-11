<div align="center">
  
#  ASON: Adaptive Structure Object Notation

<br>

[![Run Tests](https://github.com/muhammad-fiaz/ason/actions/workflows/package-tests.yaml/badge.svg)](https://github.com/muhammad-fiaz/ason/actions/workflows/package-tests.yaml)
[![PyPI Version](https://img.shields.io/pypi/v/ason)](https://pypi.org/project/ason/)
[![Python Versions](https://img.shields.io/pypi/pyversions/ason)](https://pypi.org/project/ason/)
[![Downloads](https://img.shields.io/pypi/dm/ason)](https://pypi.org/project/ason/)
[![Last Commit](https://img.shields.io/github/last-commit/muhammad-fiaz/ason)](https://github.com/muhammad-fiaz/ason)
[![GitHub Issues](https://img.shields.io/github/issues/muhammad-fiaz/ason)](https://github.com/muhammad-fiaz/ason/issues)
[![GitHub Stars](https://img.shields.io/github/stars/muhammad-fiaz/ason)](https://github.com/muhammad-fiaz/ason/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/muhammad-fiaz/ason)](https://github.com/muhammad-fiaz/ason/network)

[![Maintainer](https://img.shields.io/badge/Maintainer-muhammad--fiaz-blue)](https://github.com/muhammad-fiaz)
[![Sponsor on GitHub](https://img.shields.io/badge/Sponsor%20on%20GitHub-Become%20a%20Sponsor-blue)](https://github.com/sponsors/muhammad-fiaz)
[![License](https://img.shields.io/github/license/muhammad-fiaz/ason)](https://github.com/muhammad-fiaz/ason/blob/main/LICENSE)
[![Stability](https://img.shields.io/badge/Stability-Stable-green)](https://github.com/muhammad-fiaz/ason)

ASON is a Python library designed for adaptive data serialization. It seamlessly handles various data structures, offering flexibility and simplicity inspired by JSON.


</div>



## Installation

```bash
pip install ason
```

## Usage

```python3
# Usage example for Ason class

from ason import ason

# Create an Ason object
data = '{"name": "${name}", "age": ${age}, "city": "${city}", "hobbies": ["${hobby1}", "${hobby2}"]}'
ason_data = ason.loads(data)

# Set values for variables
ason_data.set("name", "John")
ason_data.set("age", 30)
ason_data.set("city", "New York")
ason_data.set("hobby1", "Reading")
ason_data.set("hobby2", "Coding")

# Print the result after setting variables
result_after_set = ason_data.dumps()
print("Result after setting variables:")
print(result_after_set)
print()

# Replace a key dynamically
ason_data.replace("age", "new_age", 25)

# Append a value to the 'hobbies' list
ason_data.append("hobbies", "Gardening")

# Print the result after replacing and appending
result_after_modify = ason_data.dumps()
print("Result after replacing and appending:")
print(result_after_modify)
print()

# Get the value associated with a key
city_value = ason_data.get("city")
print("Value for key 'city':", city_value)
print()

# Accessing values using square bracket notation
name_value = ason_data["name"]
print("Value for key 'name' using square bracket notation:", name_value)
print()

# Set a value using square bracket notation
ason_data["new_key"] = "new_value"
print("Result after setting a value using square bracket notation:")
print(ason_data.dumps())


```
This example demonstrates how to create an Ason object, load data, set values for variables, and then dump the result. The output will be a dictionary with the replaced values:

Result after setting variables:
```json

{"name": "John", "age": "30", "city": "New York", "hobbies": ["${hobby1}", "${hobby2}"]}
```
Result after replacing and appending:
```json

{"name": "John", "new_age": 25, "city": "New York", "hobbies": ["${hobby1}", "${hobby2}", "Gardening"]}
```
Value for key 'city': New York

Value for key 'name' using square bracket notation: John

Result after setting a value using square bracket notation:
```json

{"name": "John", "new_age": 25, "city": "New York", "hobbies": ["${hobby1}", "${hobby2}", "Gardening"], "new_key": "new_value"}
```

## Contributing
Contributions are welcome! Before contributing, please read our [Contributing Guidelines](CONTRIBUTING.md) to ensure a smooth and collaborative development process.

## Code of Conduct

Please review our [Code of Conduct](CODE_OF_CONDUCT.md) to understand the standards of behavior we expect from contributors and users of this project.

## License
This project is licensed under the [Apache 2.0 License](). See [LICENSE](LICENSE) for more details.

## Support the Project
<br>
<div align="center">

<h5> <strong> 💰 You can help me improve more by offering a little support on any platform❤️</strong></h5>

[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/muhammadfiaz) [![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://patreon.com/muhammadfiaz) [![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/muhammadfiaz)
[![Sponsor muhammad-fiaz](https://img.shields.io/badge/Sponsor-%231EAEDB.svg?&style=for-the-badge&logo=GitHub-Sponsors&logoColor=white)](https://github.com/sponsors/muhammad-fiaz)
[![Open Collective Backer](https://img.shields.io/badge/Open%20Collective-Backer-%238CC84B?style=for-the-badge&logo=open-collective&logoColor=white)](https://opencollective.com/muhammadfiaz)
</div>



## Happy Coding ❤️
