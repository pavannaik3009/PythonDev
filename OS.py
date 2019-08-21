#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)

  # Check for item existence and type
  print("Item exists:" + str(path.exists("OS.py")))
  print("Is file:" + str(path.isfile("OS.py")))
  print("Is a directory: " + str(path.isdir("OS.py")))
  # Work with file paths
  print("Item path:" +str(path.realpath("OS.py")))
  print("Item path and name:" + str(path.split(path.realpath("OS.py"))))
  
  # Get the modification time
  t = time.ctime(path.getmtime("OS.py"))
  print(t)
  print(datetime.datetime.fromtimestamp(path.getmtime("OS.py")))
  # Calculate how long ago the item was modified
  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("OS.py"))
  print("It has been:" + str(td) + " since the file was modified.")
  print("Or, " + str(td.total_seconds()) + "seconds")
  
if __name__ == "__main__":
  main()
