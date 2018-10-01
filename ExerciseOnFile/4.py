"""
4. A sentence splitter is a program capable of splitting a text into sentences.
The standard set of heuristics for sentence splitting includes (but isn't limited to) the following rules:
Sentence boundaries occur at one of "." (periods), "?" or "!", except that  .
Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
a.	Periods followed by a digit with no intervening whitespace are not sentence boundaries.
b.	Periods followed by whitespace and then an upper case letter,
    but preceded by any of a short list of titles are not sentence boundaries.
    Sample titles include Mr., Mrs., Dr., and so on.
c.	Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries
    (for example, www.aptex.com, or e.g).
d.	Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.

Your task here is to write a program that given the name of a text file can write its
content with each sentence on a separate line. Test your program with the following short text:
Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true...
Well, with a probability of .9 it isn't. The result should be:
Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
Did he mind?
Adam Jones Jr. thinks he didn't.
In any case, this isn't true...
Well, with a probability of .9 it isn't.

"""

import os

def convertToSentence(filename):
    readFile = open(os.getcwd() + "\\" + filename, 'r')
    stringValue = readFile.read()

    titles = ["Mr.", "Mrs.", "Dr."]
    data = stringValue.split()

    result = ""
    n = 0
    for i in data:
        temp = i + " "
        if(i.endswith(".") or i.endswith("?") or i.endswith("!")):
            if(n != len(data) -1):
                if(i not in titles and str(data[n + 1][0]).isupper()):
                    temp = temp + "\n"

        n =  n + 1

        result = result + temp

    return result

print(convertToSentence("shortText.txt"))
