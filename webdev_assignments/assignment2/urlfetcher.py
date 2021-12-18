from urllib.request import urlopen
import re
import sys

dangerous_words = ["bomb", "kill", "murder",
                   "terror", "terrorism", "terrorist", "terrorists"]


def check_dangerous_words(html):
    total = 0
    for word in dangerous_words:
        pattern = re.compile(r"\b" + word + r"\b")
        list_danger_words = re.findall(pattern, html)
        total += len(list_danger_words)
    print(f"In total {total} dangerous words found")


def save_file(html, path):
    try:
        with open(path, "wb") as f:
            f.write(html)
    except OSError:
        print("Error writing file")


def main():
    user_input = input("Give me a valid URL to download: ")
    try:
        html = urlopen(user_input).read()
        check_dangerous_words(html.decode("utf-8"))

        save_file(html, input("Give me filename?"))

    except UnicodeDecodeError:

        print("Doesn't appear to be and HTML file with utf-8 encoding.")
        save_file(html, input("Give me filename?"))

    except ValueError:
        print("Loading page failed. Try valid URL.")

    except:
        print("Unexpected error:", sys.exc_info()[0])


if __name__ == "__main__":
    main()
