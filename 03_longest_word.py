# QUESTION
"""
Longest Word

Have the function LongestWord(sen) take the sen parameter
being passed and return the longest word in the string.
If there are two or more words that are the same length,
return the first word from the string with that length.
Ignore punctuation and assume sen will not be empty.
Words may also contain numbers, for example "Hello world123 567"

Use the Parameter Testing feature in the box below to test your code with different arguments.
"""

# ANSWER

import re

pattern = re.compile(r'\W+')

def LongestWord(sen):
    x = pattern.split(sen)
    return max(x, key=len)
print(LongestWord(input()))

"""
Purpose of Regular Expressions:
-> Extracting the needed information from the dense data stack,
-> Controlling the input entered by the user,
-> Putting the data into a format suitable for its intended use.
"""

# Thanks to special characters, events such as 'search' or 'replacement' occur quickly and effectively.
