# gather the int store as string
int_string = input("Please enter an integer : ")

# test is the int negative
negative = int_string.startswith('-')

# reverse the int
int_string = "".join(int_string.replace("-", "")[::-1])

# create the integer this also remove all leading 0
integer = int("-" + int_string) if negative else int(int_string)

# print the result
print(integer)
