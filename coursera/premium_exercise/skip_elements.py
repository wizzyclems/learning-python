
#The skip_elements function returns a list containing every other element from an input list, 
# starting with the first element. Complete this function to do that, 
# using the for loop to iterate through the input list.
def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for e in elements:
		# Does this element belong in the resulting list?
		if i%2 == 0 :
			# Add this element to the resulting list
			new_list.append(e)
		# Increment i
		i += 1

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']


#def skip_elements(elements):
	# Initialize variables
#	new_list = []
#	i = 0

	# Iterate through the list
#	for ---- 
		# Does this element belong in the resulting list?
#		if ---- 
			# Add this element to the resulting list
#			----
		# Increment i
#		----

#	return new_list

#print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']