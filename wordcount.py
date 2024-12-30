#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def make_dict(filename):
  f = open(filename, encoding ='utf-8')
  #f = open(filename) #testing importance of utf-8
  garbage = [ '\n' , '.' , '!' , '?' , ',' , '(' , ')' ,'\'' ,'[',']',':',';','\"','`','_']
  dict = {}
  for line in f:
    #print(line)
    line = line.replace('--', ' ')
    line = line.replace('\'',' ')
    words = line.split()
    for word in words:
      word = word.lower()
      
      for ii in garbage:
        word = word.replace(ii,"")
      
      if (not word in dict):
        dict[word] = 1
      else:
        dict[word] = dict[word] + 1
  #print(dict)
  f.close()
  return dict

def word_count_dict(filename):
  """Returns a word/count dict for this filename."""
  # Utility used by count() and Topcount().
  word_count = {}  # Map each word to its count
  input_file = open(filename, encoding='utf-8')
  for line in input_file:
    words = line.split()
    for word in words:
      word = word.lower()
      # Special case if we're seeing this word for the first time.
      if not word in word_count:
        word_count[word] = 1
      else:
        word_count[word] = word_count[word] + 1
  input_file.close()  # Not strictly required, but good form.
  return word_count


def print_words(filename):
  dict_words = make_dict(filename)
  lines = []
  for word in dict_words:
    line = word + ' ' + str(dict_words.get(word))
    lines.append(line)
    lines = sorted(lines)
  f = open("DictionaryWordCount "+ filename,'w') #create new txt file
  for line in lines:
    print(line)
    f.write(line + '\n')
  
  

def count_key(tuple):
  return(tuple[1])


def print_top(filename):
  #print top 20 most common words
  dict_words = make_dict(filename)
  tuples = []
  for word in dict_words:
    count = dict_words.get(word)
    tuple = (word, count)
    tuples.append(tuple)
  tuples = sorted(tuples,key=count_key,reverse=True)
  #print(tuples)
  
  ii = 0
  while ii < 20:
    print(tuples[ii][0] + ' ' + str(tuples[ii][1]))
    ii += 1


###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
