# Fundamentals Exercise 1: CLI

Perform the following tasks using the CLI and copy and paste
the commands and results below.

- Navigate to your home directory
cd ~
- Create a new directory called CodingNomads. We will use this folder
to house materials for the course.
Already there.
- Move into the CodingNomads folder
cd Documents/_CodingNomads
- Create new folder cli_testing
mkdir cli_testing
- Inside of folder cli_testing,
    a. print the directory path
    pwd
    b. create 3 new .txt files all with different names (file1.txt,
    file2.txt, file3.txt)
    touch file1.txt file2.txt file3.txt
    c. list the contents of the folder
    ls
    d. rename one of the files
    mv file3.txt file4.txt
- Inside of folder cli_testing, create a new folder
mkdir new_folder
- Copy a file from cli_testing to the new folder
mv file4.txt new_folder
- Move a different file from cli_testing to the new folder
mv file2.txt new_folder
- Demonstrate removing:
    a. A file
    rm file1.txt
    b. A folder
    cli_testing: rm -rf new_folder 

## vim

- Use `$ vim` to write some text inside a file
vim
i
"hallo"
:w filename
:wq
- Use `$ cat` print contents of file
cat filename
- Use `$ grep` to search for a word inside file
vim filename
:grep hallo


## explore advanced CLI

- What is the difference between the two commands > and >>?

- Create a file hello.txt with the text "how?!", then append the text
    to another file called my_file.txt
- Overwrite the content of my_file.txt with "tell me"
