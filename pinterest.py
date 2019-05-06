import sys

# Prints to standard output.
def wrapLines(lineLength, words):
  # IMPLEMENTATION GOES HERE
  #for i, word in enumerate(words):
   # if len(words[i] + words[i + 1]) <= lineLength:
   #   print (words[i] + words[i + 1])
    #elif len(words[i]) == lineLenth:
    #  print (words[i])
   # else:
    #  pass
    
    #enumerates list so we can compare index to item next to it 
    for i, word in enumerate(words):
      #print if line meets length criteria
      if len((words[i] + ' ' + words[i + 1])) <= int(lineLength):
        print (words[i] + ' ' + words[i + 1])
        words.remove(words[i])
      else:
        print (words[i])
    


      
# DO NOT MODIFY BELOW THIS LINE
def main():
  first_line = None
  words = []

  first_arg = True
  for line in sys.stdin:
    if len(line.strip()) == 0:
      continue

    line = line.rstrip()

    if first_arg:
      lineLength = line
      first_arg = False
    else:
      words.append(line)

  wrapLines(lineLength, words)

main()