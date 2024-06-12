'''take a sample string as input from the user, then find its length.

if the length is greater than 4 then capitalize the entire string. else capitalize the last element of the string.'''

sample_str = input("Enter a sample string: ")
length = len(sample_str)
if length > 4:
    result = sample_str.upper()
else:
    result = sample_str[:-1] + sample_str[-1].upper()
print("Result:", result)