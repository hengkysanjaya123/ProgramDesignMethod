"""
12.	In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going.
    A simple set of heuristic rules can be given as follows:
        a)	If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
        b)	If the verb ends in ie, change ie to y and add ing
        c)	For words consisting of consonant-vowel-consonant, double the final letter before adding ing
        d)	By default just add ing

        Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form
    returns its present participle form. Test your function with words such as lie, see, move and hug.
    However, you must not expect such simple rules to work for all cases.
"""

# declare function
def isVowel(x):
    vowel = ['a', 'i', 'u', 'e','o']
    return x.lower() in vowel

# declare function
def make_ing_form(verb):
    # get length of verb
    length = len(verb)

    #get last two characters
    lastTwo = verb[length - 2 : length]
    if(lastTwo == "ie"):
        verb = verb[0:length - 2] + "y"

    # get last character
    last = verb[length - 1 : length]
    if(last == "e"):
        verb = verb[0: length - 1] + ""

    # get one last two character
    lastSecondChar = verb[length - 2 : length - 1]
    if(isVowel(lastSecondChar)):
        verb = verb + last + ""

    return verb + "ing"

#calling
print(make_ing_form("move"))
