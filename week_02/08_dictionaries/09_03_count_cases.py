'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.
Note: ignore all spaces.

Example input:
    I love to work with dictionaries!
Example output:
    Upper case: 1
    Lower case: 26
    Punctuation: 1

'''

input_ = input('Can you please enter whatever: ')


def upper_lower_punc(l):
    count_upper = 0
    count_lower = 0
    count_punctuation = 0
    punctuation = [",", ".", ":", ";", "(", ")","!", "?"]
    dict_ = {}

    for i in l:
        if i in punctuation:
            count_punctuation += 1
        elif i == i.lower():
            count_lower += 1
        elif i == i.upper():
            count_upper += 1

    dict_['Upper case'] = count_upper
    dict_['Lower case'] = count_lower
    dict_['Punctuation'] = count_punctuation
    dict_['Total characters'] = len(l)

    return dict_

l = list(input_)
print(upper_lower_punc(l))


