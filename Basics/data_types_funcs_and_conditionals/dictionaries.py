# an unordered data structure for declaring relationships between objects - mutable
# keys are unique, values can be duplicate, keys must be of immutable types


empty_dictionary = {}
ice_cream_prefs = {
    # key: value
    "Ben": "Vanilla",
    "Jerry": "Chocolate",
    "Tom": "Strawberry"
}
print(len(ice_cream_prefs))  # prints total number of key value pairs

# accessing values
print(ice_cream_prefs["Ben"])  # keys are case-sensitive
# print(ice_cream_prefs["ben"])  # KeyError
print(ice_cream_prefs.get("Ben"))  # returns value if key exists else None
print(ice_cream_prefs.get("ben", "No such key"))  # returns default value (can be of any data type) if key not found


pokemon = {
    "Fire": ["Charmander", "Charmeleon", "Charizard"],
    "Water": ["Squirtle", "Wartortle", "Blastoise"],
    "Grass": ["Bulbasaur", "Ivysaur", "Venusaur"]
}

print('Fire' in pokemon)  # checks for key
print('Fire' in pokemon.keys())  # same as above
print('Charmander' not in pokemon)  # checks for key
print('Charmander' in pokemon.values())  # checks for value
print('Charmander' in pokemon["Fire"])  # checks for value in a list

# adding new key value pairs
ice_cream_prefs["Tim"] = "Mint"
print(ice_cream_prefs)
# overwriting values
ice_cream_prefs["Ben"] = "Mint"
print(ice_cream_prefs)

sports_team_rosters = {
    "Cubs": ["Rizzo", "Bryant", "Baez"],
    "Red Sox": ["Betts", "Sale", "Devers"]
}

video_game_options = dict()  # empty dictionary
print(video_game_options)
video_game_options["difficulty"] = "Medium"
video_game_options["volume"] = 7
video_game_options["subtitles"] = True
print(video_game_options)

# key can be a dynamic value
words = ["danger", "beware", "danger" ]
def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

print(count_words(words))

# removing key value pairs

del video_game_options["volume"]
print(video_game_options)

film_directors = {
    "Martin Scorsese": "The Irishman",
    "Steven Spielberg": "Jaws",  # trailing comma is allowed
}
print(film_directors.get("Martin Scorsese", "No such key"))
print(film_directors.get("Quentin Tarantino", "No such key"))
film_directors.setdefault("Quentin Tarantino", "Pulp Fiction")  # only sets the value if the key doesn't exist
print(film_directors)

# iterating over dictionaries
for key in film_directors:
    print(key, film_directors[key])

for key, value in film_directors.items():  # items method returns a tuple of key value pairs which can be unpacked
    print(key, value)

for value in film_directors.values():
    print(value)

for key in film_directors.keys():
    print(key)

# dictionary comprehension
numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)

# conditional dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = {num: num ** 2 for num in numbers if num % 2 == 0}
print(squared_numbers)


word = "asdfdfhiuqwgfhbr gahdsklgvbfaudfasdgihasdighoasdgiofdasg;"
letter_count = {letter: word.count(letter) for letter in word}
print(letter_count)


capitals = {
    "USA": "Washington DC",
    "France": "Paris",
    "Italy": "Rome"
}

# flipping key value pairs in dictionary
flipped_capitals = {capital: country for country, capital in capitals.items()}
print(flipped_capitals)

# pop method
ice_cream_prefs.pop("Tim")  # removes key value pair, returns value, checks if key exists
print(ice_cream_prefs)


# clear method
ice_cream_prefs.clear()  # removes all key value pairs
print(ice_cream_prefs)
del ice_cream_prefs  # deletes the dictionary from memory
# print(ice_cream_prefs)  # NameError


employee_salaries = {
    "John": 50000,
    "Sally": 60000,
    "Jane": 70000
}

extra_salaries = {
    "Jake": 80000,
    "Jill": 90000
}

employee_salaries.update(extra_salaries)  # adds key value pairs from extra_salaries to employee_salaries
print(employee_salaries)


# copying dictionaries
employee_salaries_copy = employee_salaries.copy()  # creates a shallow copy
print(employee_salaries_copy)
employee_salaries_copy["John"] = 60000
print(employee_salaries_copy)
print(employee_salaries)

# nested dictionaries
nested_dict = {
    "first": {
        "a": 1,
        "b": 2
    },
    "second": {
        "c": 3,
        "d": 4
    }
}
print(nested_dict["first"]["a"])
print(nested_dict["second"]["d"])


# sorted function
print(sorted(employee_salaries))  # sorts the keys and returns a list of keys
print(sorted(employee_salaries.values()))  # sorts the values and returns a list of values
print(sorted(employee_salaries.items()))  # sorts the key value pairs and returns a list of tuples


# min and max functions
print(min(employee_salaries))  # returns the minimum key
print(max(employee_salaries))  # returns the maximum key
print(min(employee_salaries.values()))  # returns the minimum value
print(max(employee_salaries.values()))  # returns the maximum value


# unpacking argument dictionaries
def height_to_meters(feet, inches):
    return feet * 0.3048 + inches * 0.0254

print(height_to_meters(**{"feet": 5, "inches": 11}))  # unpacks the dictionary and passes the key value pairs as arguments
print(height_to_meters(**{"feet": 6, "inches": 0}))  # unpacks the dictionary and passes the key value pairs as arguments

stats = {
    # if more keys are passed than required by the function, it will throw an error
    "feet": 5,
    "inches": 11
}
print(height_to_meters(**stats))  # unpacks the dictionary and passes the key value pairs as arguments
