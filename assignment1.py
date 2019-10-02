import sys, os, time, string

def countUsingConditions():
	start = time.time()

	#Open files and normalize words
	with open("neuromancer.txt", "r") as txtFile:
		words = txtFile.read().split()

	with open("stop_words.txt", "r") as txtFile:
		stop_words = txtFile.read().split(",")

	normalizedWords = []
	for word in words:
		word = word.lower().replace(".", "")
		word = word.replace(",", "")
		word = word.replace('?', "")
		word = word.replace('"', "")
		if word == "":
			continue
		normalizedWords.append(word)

	normalizedStopWords = []
	for word in stop_words:
		word = word.lower()
		normalizedStopWords.append(word)

	#Container for words and their occurence
	occurence = {}
	#Loop through words, skip if they're a stop word, add to dictionary if they're not
	for word in normalizedWords:
		if word in normalizedStopWords:
			continue
		#Counts occurences
		try:
			occurence[word] += 1
		#Catches key error if key word is not in dictionary yet
		except:
			occurence[word] = 1

	end = time.time()
	return end-start, occurence

if __name__ == "__main__":
	time, occurences = countUsingConditions()
	sortedValues = sorted(occurences.iteritems(), key = lambda x : x[1], reverse=True)
	currentValue = 0
	counter = 0

	for name,frequency in sortedValues:
		if frequency == currentValue:
			continue
		currentValue = frequency
		if counter > 24:
			break
		counter +=1
		print name, "--", frequency

	print "Counted in:", time, "seconds"

