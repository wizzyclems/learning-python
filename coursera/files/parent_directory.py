import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  parent = os.path.join(os.getcwd(),"..")
  os.chdir(parent)
  relative_parent = os.getcwd()

  # Return the absolute path of the parent directory
  return relative_parent

print(parent_directory())