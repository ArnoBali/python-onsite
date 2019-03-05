'''
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be
replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message,
and exit.
Solution: http://thinkpython2.com/code/sed.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''


def sed(filename1,filename2):
    string = 'hello'
    replacement_string = 'hello world'

    with open(filename1, 'r') as fin:
        file1 = fin.readlines()

    with open(filename2, 'a') as fout:
        for i in file1:
            file2 = fout.write(i.replace(string, replacement_string))


sed('words.txt', 'replacement_words.txt')

