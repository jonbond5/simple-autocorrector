# Generate the list of items we're dealing with
with open('list of fruit.txt') as f:
	list_of_people = [name[:-1] for name in f]

def simpleGuessing():
	# Get the word you'd like to correct
	name = raw_input("Input:  ")

	# Build a confidence list
	# The prof with the highest confidence is who we'll return
	confidence = {prof : 0.0 for prof in list_of_people}

	for prof in list_of_people:
		for letter in name:
			if letter in prof:
				confidence[prof] += 1

	# At this point, a small list (~2 - 50) of decently-diversed names should work
	# If you only need it for a small-list-purpose, comment out the function call below
	# else continue as planned

	for key in confidence:
		print "The name " + key + " has a confidence of...." + str(confidence[key])
	print '\n\nI believe you meant: \n' + max(confidence, key=confidence.get)


# Being built...
# Slightly better correcting
# Rather than just finding letter similarities, it looks for substring similarities
def advancedGuessing():
	name = raw_input("Name:  ")
	confidence = {prof : 0 for prof in list_of_people}

	# Find common substrings
	for prof in list_of_people:
		name_iterator = iter(name)
		last_position = 0
		on_a_roll = False
		# Iterate until the iterator has no next() value
		while 1:
			# Find any substrings in name that're in prof as well
			try:
				on_a_roll = False
				letter = next(name_iterator)
				while letter in prof:
					confidence[prof] += on_a_roll
					on_a_roll = True
					letter += next(name_iterator)
			except:
				break
		# Greater size difference, less confident
		confidence[prof] -= abs(len(name) - len(prof)) * 0.1
		


	# Initial confidence rating is done
	# Now, enhance confidence level based on size, letters given (not in substring), etc.

	for key in confidence:
		print key + " has confidence.........  " + str(confidence[key])
	print '\n\nI believe you meant:   ' + max(confidence, key=confidence.get)

advancedGuessing()