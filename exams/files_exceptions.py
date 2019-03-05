'''
You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) open war_and_peace.txt, read the whole file content and store it in a variable

2) open crime_and_punishment.txt and overwrite the whole content with an empty string

3) loop over all three files and print out the first 100 characters. the program
    should NEVER terminate with a Traceback.

    a) which Exception can you expect to encounter? why?

    b) how do you catch it to avoid the program from terminating with a Traceback?

4) EXTRA: write a custom Exception that inherits from Exception and raise it if the
    first 100 characters of any of the files contain the string "attention".

'''

class AttentionException(Exception):
    pass

with open("war_and_peace.txt", "r") as fin:
    content = fin.read()

with open("crime_and_punishment.txt", "w") as fout:
    fout.write("")

books = ["war_and_peace.txt","crime_and_punishment.txt","pride_and_prejudice.txt"]

for book in books:
    try:
        with open(book,"r") as fin:
            content = fin.read()
    except FileNotFoundError as fnf:
        print(fnf)
    except PermissionError as err:
        print(err)
    else:
        try:
            first_char = content[:100]
        except IndexError as err:
            print(err)
        else:
            if "attention" in (first_char):
                raise AttentionException
            print(first_char)



