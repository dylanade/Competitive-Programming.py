def swap_case(s):
    swapped_s = ""
    for char in s:
        if (char.islower()):
            swapped_s += char.upper()
        elif (char.isupper()):
            swapped_s += char.lower()
        else:
            swapped_s += char
            
    return swapped_s
        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
