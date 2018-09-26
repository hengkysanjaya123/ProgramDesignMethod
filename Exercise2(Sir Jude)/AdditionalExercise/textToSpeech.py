#import time and os to support the text to speech
import time, os

"""
define a function takes 3 parameters
txt = text to be spoken
#icao_pause = to set the delay time between each icao word
#word_pause = to set the delay time between each word
"""
def tellMe(txt, icao_pause = 1, word_pause = 2):
	#set it to lower case
	words = txt.lower()
	#split the word into list
	words = words.split()

	# declare a dictionary to store ICAO data
	d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 'z':'zulu'}

	#loop each element in words
	for word in words:
		#loop each character in word
		for j in word:
			# speak the word in ICAO alphabet
			os.system('say ' + d[j])
		#set the delay time between icao alphabet
		time.sleep(icao_pause)
	#set the delay time between word
	time.sleep(word_pause)


#calling method
tellMe("I am test")