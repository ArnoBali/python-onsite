'''
We've learned about strings earlier. Looking at string methods from the
perspective of "everything is an object in python" explains the syntax
that we encountered there.

Now take a second look at the documentation of the string methods at:
http://docs.python.org/3/library/stdtypes.html#string-methods.

Demonstrate 3 interesting string methods of your choice and explain why
they are invoked like this: str.method()

'''
a = "HellOoOoO in this crazy LITTLE wOrlD! "


# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found within the slice s[start:end].
# Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

# str.title()
# Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.

# str.swapcase()
# Return a copy of the string with uppercase characters converted to lowercase and vice versa. Note that it is not necessarily true that s.swapcase().swapcase() == s.

print(type(a))

print(a.title())
print(a.swapcase())

print(a.find('i'))