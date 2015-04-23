## Facotrial
print (reduce(lambda x, y: x * y, range(1, 10)))

## Remove character

start_string = "hello how this is a long string"
char_to_find = "l"
print(filter(lambda x: x != char_to_find, start_string))

## print nubmer of occurances of a character

print(len(filter(lambda x: x == char_to_find, start_string)))

## Take a string of words and say how many start with a speific character

print(len(filter(lambda x: x[0] == "h", start_string.split())))

