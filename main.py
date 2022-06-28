import os
import getpass
import filetype

# get all extensions in directory
current_dir = os.getcwd()

# get current user
current_user = getpass.getuser()


def navigate_to(dir: str):
  os.chdir(f"/Users/{current_user}/{dir}")
  print("Current working directory: {0}".format(os.getcwd()))

def check_extensions():
  print("Checking file extensions in: {0}".format(os.getcwd()))
  pass

navigate_to("Desktop")
check_extensions()

def main():
  pass

if __name__ == '__main__':
    main()
# go to a location
# instead of checking extensions first, 
# Iterate through all the files in the location, if there is an extension we know of
  #  create the folder and put the file in there


