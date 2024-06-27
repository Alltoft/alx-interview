# UTF-8 Validation

This repository contains the implementation of a UTF-8 validation algorithm.

## Algorithm

The UTF-8 validation algorithm checks whether a given byte array represents a valid UTF-8 encoded string. It follows the UTF-8 encoding rules specified by the Unicode Consortium.

The algorithm works as follows:

1. Start with the first byte in the array.
2. Determine the number of bytes in the current UTF-8 character based on the first byte.
3. Check that the next `n-1` bytes in the array are valid continuation bytes.
4. Repeat steps 2 and 3 for the remaining bytes in the array.
5. If all bytes are valid and properly encoded, the array represents a valid UTF-8 string.

## Usage

To use the UTF-8 validation algorithm, follow these steps:

1. Include the `utf8_validation.py` file in your project.
2. Call the `validate_utf8(bytes_array)` function, passing in the byte array to be validated.
3. The function will return `True` if the byte array is a valid UTF-8 string, and `False` otherwise.

## Example

Here is an example usage of the UTF-8 validation algorithm:

```python
