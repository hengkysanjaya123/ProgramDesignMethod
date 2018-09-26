"""
1. The third person singular verb form in English is distinguished by the suffix -s,
which is added to the stem of the infinitive form: run -> runs. A simple set of rules can be given as follows:
a.	If the verb ends in y, remove it and add ies
b.	If the verb ends in o, ch, s, sh, x or z, add es
c.	By default just add s
Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form
returns its third person singular form. Test your function with words like try, brush, run and fix.
Note however that the rules must be regarded as heuristic, in the sense that you must not expect them to work for all cases.
Tip: Check out the string method endswith().

"""

#solution1
def make_3sg_form(verb):
    data = "o ch s sh x z"
    data = data.split(" ")

    #check first constraint
    if(verb.endswith("y")):
        return (verb[0:len(verb)-1] + "ies")
    #check for the second constraint
    else:
        for i in data:
            if(verb.endswith(i)):
                return verb + "es"

    #just plus "s" by default
    return verb + "s"


#solution2
def make_3sg_form2(verb):
    #check first constraint
    if(verb.endswith("y")):
        return (verb[0:len(verb)-1] + "ies")
    #check for the second constraint
    elif(verb.endswith(("o","ch","s","sh","x","z"))):
        return verb + "es"

    #just plus "s" by default
    return verb + "s"


print("Input . (dot) to exit")
while True:
    #ask for input
    verb = input("Please input verb : ")
    #check if user type dot the program will terminate
    if(verb == "."):
        break

    #call the function and print the result
    print("From solution 1's result : "+make_3sg_form(verb))
    print("From solution 2's result : "+make_3sg_form2(verb))





