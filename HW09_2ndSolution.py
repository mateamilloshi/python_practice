#Ptoblem 1
def file_copy(in_file, out_file):
  inF = open(in_file, 'r')
  outF= open(out_file, 'w')
  for line in inF:
    outF.write(line)

  inF.close()
  outF.close()

#Problem 2
def file_stats(in_file):
  inF = open(in_file,'r')

  text = inF.read()
  numChars = len(text)
  numWords = len(text.split())
  numLines = text(text.split('\n'))
  print('lines ',numLines)
  print('words ',numWords)
  print('chars ',numChars)

  inF.close()

#Problem 3
import string
def repeat_words(in_file,out_file):
  inF = open(in_file, 'r')
  outF= open(out_file, 'w')
  for line in inF:
    words = line.split()
    seenOnce=[]
    seenAgain=[]

    for word in words:
      cleanWord = word.lower()
      cleanWord = cleanWord.strip(string.punctuation)
      if cleanWord not in seenOnce:
        seenOnce.append(cleanWord)
      elif cleanWord not in seenAgain: 
        seenAgain.append(cleanWord)
        
    for word in seenAgain:
      outF.write(word + ' ')
    outF.write('\n')

  inF.close()
  outF.close()
