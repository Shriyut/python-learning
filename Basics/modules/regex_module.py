import re

pattern = re.compile("flower")
print(type(pattern))

pattern.search("candy") # will not find a match and return None object

match = pattern.search("flower power") # will return a Match object
print(type(match))

if match: # wont run when match is None
    print(match.group()) # flower
    print(match.start()) # will give the starting index
    print(match.end()) # ending index position
    print(match.span()) # gives starting and ending index

print(pattern.match("flower power")) # will search only at the beginning
# search will find the pattern anywhere in the string

sentence = "There are a lot of flowers in the flowery flower field"
print(pattern.findall(sentence)) # returns list with pattern where it occurs
print(pattern.findall("None")) # returns empty list

for match in pattern.findall(sentence):
    print(match) # prints flower 3 times


# regex module level functions
print(re.search("flower", "Picking flowers in a flower field"))
print(re.match("flower", "flower field"))
print(re.findall("flower", "Picking flowers in flower field"))

for match in re.finditer("flower", "Picking flowers in flower field"):
    print(match)


print("\t Take a look \n right here")
# create a raw string, all values will be taken as is, \t and \n will not work
print(r"\t Take a look \n right here")

pattern_1 = re.compile(r"\d") # \d denotes digits, \D denotes non digits
sentence_1 = "I bought 4 apples, 5 oranges, and 12 plums"
print(pattern_1.findall(sentence_1))

# refer regex 101 website

# \w refers to any word character including digits
# \W anything that is not alpha numeric
# \s captures any whitespace character
# \S any non whitespace character
# \bt gives word that start with t, \b is the pattern, t\b will return words that end with t
# . denotes any character
# e..o returns any word with 2 chars between e and o
# \. to find . - tells re to not identify . as metacharacter and just look for .
# [fwr] any occurence of either f w or r
# [^fwr] any character except f w and r
# [a-l] both bounds are inclusive gives all chars present from a to l
# [A-L] same as above for capital chars
# z{3} matches for 3 occurences of z together in the string
# z{3,} 3 or more occurences of 3
# z{3,5} sequence of z from 3 to 5
# \s{3} looking for 3 occurences of whitespace in a row
# \d{4} will look for 4 digit numbers
# \d{3}-\d{3}-\d{4} sample pattern to look for phone number
# \d{3}\s{1, }\d{3}\s{1, }\d{4} replaces - in above pattern with whitespace (one or more)
# \d{3}\s+\d{3}\s+\d{4} - same as above
# (\d{3}-\d{3}-\d{4}|\d{3}\s+\d{3}\s+\d{4}) (a|b) - pattern for either a or b