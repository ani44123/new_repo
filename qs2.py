sample_str = input("Enter a sample string: ")

if sample_str[0].isdigit():
    numeric_values = ""
    for char in sample_str:
        if char.isdigit():
            numeric_values += char
    print("Numeric values:", numeric_values)
else:
    alphabets = ""
    for char in sample_str:
        if char.isalpha():
            alphabets += char
    print("Alphabets:", alphabets)
