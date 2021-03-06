# Concordance
Given a file with text create a concordance of all the text

This is a project manifest with instructions on how to setup and 
run the Concordance project. 

I. Contents
   1) concordance.py - The main classes of this project.  
   2) concordance_cli.py - A script for running the project at the command line. 
   3) concordance_tests.py - The class that has all of the unit tests. 
   4) empty.file.lines.txt - used to prove the files with empty lines are bypassed.
   5) empty.file.txt - used to prove that empty files are bypassed.
   6) test.file.txt - a valid file for testing. 

II. Instructions
  You can import this project into an ide or you can run it from the command line. 

III. Caveats
  I do not have an exhaustive list of abbreviations.  I'm only accounting for '.e.g' 
  and '.i.e'.  In a production scenario I would have a file system of abbreviations
  that were loaded at runtime. 

  My regex that is used to split the file has a few issues.  One it raises a PEP8 error 
  about a redundant escape character.  The problem with removing it is that the tests
  throw an error once I do that.  I will admit to not being a regex expert and I did 
  not have the time to play with this.  Also, the regex produces a blank item as the
  last item in the list.  I've handled this with code.  Ideally, I would like to have
  a regex that doesn't do this.  
