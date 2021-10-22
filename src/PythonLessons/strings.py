# Working with strings


p_string = "Hello there"

# Print only 'there' in string
print(p_string[6:])

# Print string in reverse
print(p_string[::-1])

# Print string skipping every other word
print(p_string[::2])


name = "Dominic"
print("How are you doing %s" % name)

age = 15
print("The number is %d" % age)

number = 10.5532
# print("The other number is %d" % number)
print("The other number is %f" % number)
print("The other number is %.1f" % number)
print("The other number is {:.2f}".format(number))

p_string = "           Dominc"
# Print string with all spaces stripped
print(p_string.strip())

p_string = "Josh Gates"
print(p_string.startswith('Josh'))
print(p_string.replace('Gates', 'Paris'))


p_string = "Bill/Josh/Jack/Sam/David"
print(p_string.split('/'))
print(''.join(p_string))


some_list = ['Joe'] * 60
p_string = ''.join(some_list)
print(p_string)