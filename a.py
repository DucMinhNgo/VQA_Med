import re

# Given string
original_string = "{'train': [tensor(0.3919, device='cuda:0')], 'valid': [tensor(0.4560, device='cuda:0')]}"

# Regular expression pattern to match floating-point numbers
pattern = r'\d+\.\d+'

# Find all floating-point numbers in the string
numbers = re.findall(pattern, original_string)

# Extracted numbers
extracted_numbers = [float(number) for number in numbers]

# Print the extracted numbers
print(extracted_numbers[0])
print(extracted_numbers[1])