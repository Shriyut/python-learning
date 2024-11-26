"sushi"

'sushi'

'you\'re right'
'shakespeare once said "To be or not to be"'

mutli_line_string = ('sample mutli line string'
       'next line'
       'another line')

another_multi_line_string = """
Hey, this is another 
mutli-line string"""

third_multi_line_string = "multiline string" \
       + another_multi_line_string \
       + mutli_line_string

print(type(mutli_line_string), type(another_multi_line_string))

sample_string = "pg_conftools"
sample = ".conf"

print(len(sample_string))
print(len(str(4)))

file_name = sample_string + sample

#string index positions start from 0
print(file_name[1]) # returns as a string

# index -1 gives the last character of the string

print(file_name[-3]) # returns third last character

#slicing strings
print(file_name[0:3]) # left value is inclusive and right value is exclusive
print(file_name[3:-5]) # returns substring from the 3rd character till the 5th last character excluding it
print(file_name[3:])  # 3rd character till the end
print(file_name[-10:])
print(file_name[:12]) # starts from beginning till the 10 th character

print(file_name[0:10])   #pg_conftoo
print(file_name[0:10:2]) #p_ofo
# third index is used to represent how should the control take the value i,e in this case takes every second character in b/w 0 to 10

print(file_name[::])   # returns the string
print(file_name[::-1]) #fnoc.slootfnoc_gp - reverses the string

# both shown below return true
print("tools" in file_name)
print("tools " not in file_name)

print(file_name.find("conf")) # returns first occurrence of the substring, -1 if doesn't exist
print(file_name.find("conf", 7)) # starts looking from 7th position
#index function works in the same way as find but returns value error if the value doesn't exist
#string functions are case-sensitive
print(file_name.startswith("pg"))
print(file_name.endswith("conf"))
print(file_name.count("conf"))
print(file_name.upper())
print(file_name.islower()) # returns true even if _ and . are present in string
print(file_name.rstrip()) #lstrip, strip - these functions remove trailing spaces
print(file_name.lstrip("f")) #removes all trailing f from the beginning of the string
print(file_name.replace("conf", "exec"))

one = "one"
two = "two"
three = "three"

combination = "{} and {} and {}"
print(combination.format(one, two, three))
combination = "{2} and {1} and {0}"
print(combination.format(one, two, three))
combination = "{one} and {two} and {three}"
print(combination.format(one=one,two=two,three=three))

print(f"{one} and {two} and {three}")

dinner = "chicken and wine"

for char in dinner:
       print(char)