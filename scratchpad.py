from urllib.parse import quote, unquote

# String to encode
original_string = "What is the unicode u+ code for the ⋃ symbol? big cup or union..md"

# Encode the string to URL-encoded format
encoded_string = quote(original_string)
print(original_string)
# Now you can send the encoded_string to the server...
print(encoded_string)

decoded_string = unquote(encoded_string)

# Now you have the original string back
print(decoded_string)

if original_string == decoded_string:
    print("Success!")
else:
    print("Fail!")