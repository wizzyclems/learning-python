#Fill in the blanks to make the is_power_of function return whether the 
# number is a power of the given base. Note: base is assumed to be a positive number. 
# Tip: for functions that return a boolean value, you can return the result of a comparison.

#def is_power_of(number, base):
  ## Base case: when number is smaller than base.
 # if number < base:
    ## If number is equal to 1, it's a power (base**0).
 #   return __

  ## Recursive case: keep dividing number by base.
 # return is_power_of(__, ___)

#print(is_power_of(8,2)) # Should be True
#print(is_power_of(64,4)) # Should be True
#print(is_power_of(70,10)) # Should be False


def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1
    
  number = number/base
  print(number)
  # Recursive case: keep dividing number by base.
  return is_power_of(number, base)

#print(is_power_of(8,2)) # Should be True
#print(is_power_of(64,4)) # Should be True
#print(is_power_of(70,10)) # Should be False
print(is_power_of(16,10)) # Should be False
