"""
You've been hired as a content moderator for a social media platform, and your task is to identify and flag inappropriate language used by users. Your team has received a tip that some users are using coded language to bypass the platform's filters and post inappropriate content.

After analyzing the data, you've discovered a text file, "drunkard_words.txt", which contains a list of words that are likely being used to disguise inappropriate language. You can access and download this text file via link (https://gist.githubusercontent.com/lzblack/cd9d6187dfdc4fbd363e0fbc538275a5/raw/43dbeda41c0c7ef1223e1ac2e64ef87aad4c054d/drunkard_words.txt). 

Your job is to create a function, `identify_inappropriate_words`, that identifies the inappropriate words and return the complete list of these words.

A word is considered as "inappropriate" if it meets all the following three conditions:
- The word contains at least three letters from "covid".
- The word contains at least one letter (any letter) that occurs twice in a row.
- The word starts and ends with the same letter (any letter).

Requirements:
- You can create helper function(s) to be used in the major function, `identify_inappropriate_words`.
- You should write docstring(s) to the function(s) you create, describing its purpose, input parameters, and output.
- To test your function(s), you should add test code that calls the function(s) you create.
- You can write comments and pseudo-code appropriately in order to improve the readability and understandability of your code.
- Use meaningful function and variable names.
"""
f = open ('data/drunkard_words.txt')
inappropriate_letter = ["c","o","v","i","d"]
for line in f:
        word = line.strip()


def identify_inappropriate_words():
    """
    Characteristic of a bad word:
    a. contains three letters of letter "c", "o", "v", "i", "d"
    b. two letter in the same row, like oo
    c. word start with the same letter: amanda 
    """
    count = 0 #initial as 0
    for i in range(word):
            if word[i] in inappropriate_letter:
                count += 1
                if count>=3:
                    return (True)
def check ():
    for i in range(len(word) - 1):
        if identify_inappropriate_words == True:
            if word[i] == word[i + 1]: # it satifisfies condition b
                return (True)
            else:
                 return (False)

def check_2():
      for i in range(len(word) - 1):
        if check == True:
            if word[0]==word[-1]: # it satifisfies condition b
                print (word)
            else:
                 return (False)

           

identify_inappropriate_words()
