# Generate the list of items we're dealing with
with open('list of names.txt') as f:
	list_of_people = [name[:-1] for name in f]

def simpleGuessing():
	# Get the word you'd like to correct
	guess = raw_input("Input:  ")

	# Build a confidence list
	# The prof with the highest confidence is who we'll return
	confidence = {prof : 0 for prof in list_of_people}

	for prof in list_of_people:
		for letter in guess:
			if letter in prof:
				confidence[prof] += 1

	# At this point, a small list (~2 - 50) of decently-diversed names should work
	# If you only need it for a small-list-purpose, comment out the function call below
	# else continue as planned
	advancedConfidence()

	for key in confidence:
		print "The name " + key + " has a confidence of...." + str(confidence[key])
	print '\n\nI believe you meant: \n' + max(confidence, key=confidence.get)


# Being built...
def advancedConfidence():
	pass

simpleGuessing()