# ason.py
import re
from collections import OrderedDict
from ason.exception import *
class ason:
    """
     Ason: Adaptive Structure Object Notation

     A Python class for adaptive data serialization, handling various data structures with flexibility
     and simplicity inspired by JSON.

     Attributes:
         data (OrderedDict): The data structure used to store key-value pairs.

     Methods:
         __init__(self, data=None):
             Initializes an Ason object.

         set(self, variable, value):
             Sets the value of a variable within the Ason data.

         get(self, key):
             Retrieves the value associated with a given key from the Ason data.

         _process_placeholder(self, match):
             Processes a placeholder match during the 'set' operation.

         _handle_nested_type(self, variable, value, item):
             Handles nested types (dict, OrderedDict, list) during the 'set' operation.

         replace(self, old_key, new_key, new_value):
             Replaces a key with a new key and value dynamically.

         append(self, key, value):
             Appends a value to a list within the Ason data.

         dumps(self):
             Converts the Ason data to a dictionary.

         loads(cls, data_str):
             Loads Ason data from a string representation.

         __getitem__(self, key):
             Gets the value associated with a given key using the square bracket notation.

         __setitem__(self, key, value):
             Sets the value of a key using the square bracket notation.
     """
    def __init__(self, data=None):
        """
              Initializes an Ason object.

              Args:
                  data (OrderedDict): The initial data structure. Defaults to an empty OrderedDict.
              """
        self.data = data or OrderedDict()

    def set(self, variable, value):
        """
              Sets the value of a variable within the Ason data.

              Args:
                  variable (str): The variable to set.
                  value: The value to assign to the variable.
              """
        updated_data = OrderedDict()
        try:
            for key, data_value in self.data.items():
                if isinstance(data_value, str):
                    # Replace variables inside the key
                    key_with_value = re.sub(r'(?<!\\)\${(\w+)}', self._process_placeholder, key)
                    if key_with_value != key:
                        updated_data[key_with_value] = data_value
                    else:
                        key_with_value = re.sub(fr'\${{{variable}}}', str(value), key_with_value)
                        updated_data[key_with_value] = re.sub(fr'\${{{variable}}}', str(value), data_value)
                elif isinstance(data_value, (dict, OrderedDict)):
                    nested_as = ason(data_value)
                    nested_as.set(variable, value)
                    updated_data[key] = nested_as.dumps()
                elif isinstance(data_value, list):
                    updated_data[key] = [self._handle_nested_type(variable, value, item) for item in data_value]
                else:
                    updated_data[key] = data_value
            self.data = updated_data
        except Exception as e:
            raise SetOperationException(f"An error occurred during 'set' operation: {e}")

    def get(self, key):
        """
               Retrieves the value associated with a given key from the Ason data.

               Args:
                   key: The key to retrieve the value for.

               Returns:
                   The value associated with the key.
               """
        try:
            return self.data.get(key)
        except Exception as e:
            raise GetOperationException(f"An error occurred during 'get' operation: {e}")

    def _process_placeholder(self, match):
        """
               Processes a placeholder match during the 'set' operation.

               Args:
                   match: The regex match object.

               Returns:
                   The processed value for the placeholder.
               """
        try:
            key = match.group(1)
            value = self.get(key)
            if value is None:
                return match.group(0)
            return value
        except Exception as e:
            raise ProcessPlaceholderOperationException(f"An error occurred during '_process_placeholder' operation: {e}")

    def _handle_nested_type(self, variable, value, item):
        """
              Handles nested types (dict, OrderedDict, list) during the 'set' operation.

              Args:
                  variable (str): The variable to set.
                  value: The value to assign to the variable.
                  item: The nested item to handle.

              Returns:
                  The processed value for the nested item.
              """
        if isinstance(item, (dict, OrderedDict)):
            nested_as = ason(item)
            nested_as.set(variable, value)
            return nested_as.dumps()
        elif isinstance(item, list):
            return [self._handle_nested_type(variable, value, subitem) for subitem in item]
        else:
            return item

    def replace(self, old_key, new_key, new_value):
        """
              Replaces a key with a new key and value dynamically.

              Args:
                  old_key: The key to be replaced.
                  new_key: The new key to use.
                  new_value: The new value to associate with the new key.
              """
        try:
            updated_data = OrderedDict()
            for key, value in self.data.items():
                if key == old_key:
                    updated_data[new_key] = new_value
                elif isinstance(value, (dict, OrderedDict)):
                    nested_as = ason(value)
                    nested_as.replace(old_key, new_key, new_value)
                    updated_data[key] = nested_as.dumps()
                elif isinstance(value, list):
                    updated_data[key] = [self._handle_nested_type(old_key, new_key, item) for item in value]
                else:
                    updated_data[key] = value
            self.data = updated_data
        except Exception as e:
            raise ReplaceOperationException(f"An error occurred during 'replace' operation: {e}")

    def append(self, key, value):
        """
             Appends a value to a list within the Ason data.

             Args:
                 key: The key associated with the list.
                 value: The value to append to the list.
             """
        try:
            if key in self.data and isinstance(self.data[key], list):
                self.data[key].append(value)
            elif key in self.data and isinstance(self.data[key], (dict, OrderedDict)):
                nested_as = ason(self.data[key])
                nested_as.append(key, value)
                self.data[key] = nested_as.dumps()
            else:
                print(f"Warning: '{key}' is not a list or nested type. Cannot append value.")
        except Exception as e:
            raise AppendOperationException(f"An error occurred during 'append' operation: {e}")

    def dumps(self):
        """
             Converts the Ason data to a dictionary.

             Returns:
                 The Ason data as a dictionary.
             """
        try:
            return dict(self.data)
        except Exception as e:
            raise DumpsOperationException(f"An error occurred during 'dumps' operation: {e}")

    @classmethod
    def loads(cls, data_str):
        """
             Loads Ason data from a string representation.

             Args:
                 data_str (str): The string representation of Ason data.

             Returns:
                 An Ason object initialized with the loaded data.
             """
        try:
            return cls(data=eval(data_str, {}, {'OrderedDict': OrderedDict}))
        except Exception as e:
            raise LoadsOperationException(f"An error occurred during 'loads' operation: {e}")

    def __getitem__(self, key):
        """
               Gets the value associated with a given key using the square bracket notation.

               Args:
                   key: The key to retrieve the value for.

               Returns:
                   The value associated with the key.
               """
        try:
            return self.data[key]
        except Exception as e:
            raise GetItemOperationException(f"An error occurred during '__getitem__' operation: {e}")

    def __setitem__(self, key, value):
        """
               Sets the value of a key using the square bracket notation.

               Args:
                   key: The key to set the value for.
                   value: The value to assign to the key.
               """
        try:
            self.data[key] = value
        except Exception as e:
            raise SetItemOperationException(f"An error occurred during '__setitem__' operation: {e}")



