from string_utilis import string_operations as ops
from string_utilis import string_validations as vals

s = input("Enter a string: ")

print("Reversed:", ops.reverse_string(s))
print("Uppercase:", ops.to_uppercase(s))
print("Length:", ops.string_length(s))
print("Is Palindrome:", vals.is_palindrome(s))
print("Contains only alphabets:", vals.is_alpha(s))
