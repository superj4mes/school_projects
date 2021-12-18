import json
import sys


def read_dict(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except ValueError:
        print("Corrupted JSON data")
    except OSError:
        print("Error opening or reading file")


def write_dict(dict, file):
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(dict, f, indent=4)
            return True

    except OSError:
        print("Error writing file")
        return False
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return False


DB_LOCATION = "dictdb.json"
dict = read_dict(DB_LOCATION)

if dict:
    print("Dictionary loaded succesfully!")
else:
    dict = {"dog": "koira", "cat": "kissa", "ape": "apina"}
    print("No dictionary file found!\nUtilizing pre-installed dictionary!")

while True:
    print("")
    print("Dictionary Program!")
    print("1 - Fetch a word\n2 - Quit and save\n3 - Quit")
    choice = input("Option: ")
    if choice == "1":
        while True:
            word = input("Give me a word? or just hit ENTER ").lower()
            if not word:
                break
            if word in dict:
                print(word, "=", dict[word])
            else:
                definition = input(
                    "Give definition for word %s?\n" % word).lower()
                if definition:
                    dict[word] = definition
    if choice == "2":
        if write_dict(dict, DB_LOCATION):
            print("Dictionary saved successful with", len(dict), "words")
            break
    if choice == "3":
        break
