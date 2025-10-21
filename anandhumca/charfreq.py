input_string=input("Enter a string:")
char_frequency={}
for char in input_string:
    char_frequency[char]=char_frequency.get(char,0)+1
print(f"Character frequencies in '{input_string}':")
for char,count in char_frequency.items():
    print(f"{char} occurs {count} times.")
