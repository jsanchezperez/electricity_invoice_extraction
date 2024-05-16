''''
Program for creating training data from the IDSEM database 
Converts annotated PDF invoices into text files composed of 
a list of tuples with sentences of eleven words and the label 
corresponding to the center word
'''

import pprint, re
import os, sys
from nltk import word_tokenize


def idsem_file_to_list(file):
   '''Takes an annotated invoice from IDSEM (TXT annotated) and creates a list of tuples.
      Each tuple contains a sentence of 11 words and a label corresponding to the center word'''

   labels = ["#A1", "#A2", "#A3", "#A4", "#A5", "#A6", "#B1", "#B2", "#B3", "#B4", "#B5", "#B6", "#C1", "#C2", "#C3", "#C4", "#C5", "#C6", "#C7", "#C8", "#C9", "#CA", "#CB", "#CC", "#CD", "#CE", "#D1", "#D2", "#D9", "#DC", "#DD", "#E1", "#E2", "#E3", "#E3l", "#E4", "#E5", "#E6", "#E7", "#E7l", "#E7p", "#E7s", "#E8", "#E9", "#F1", "#F2", "#F3", "#F3l", "#F3p", "#F3s", "#F4", "#F4l", "#F4p", "#F4s", "#F4u", "#F5", "#F5l", "#F5p", "#F5s", "#F5u", "#F6",  "#F7",  "#F8",  "#F8l",  "#G1",  "#G2",  "#G3",  "#G3l", "#G3p", "#G4", "#G5", "#G6", "#G7", "#G8", "#G9", "#GA", "#I1", "#I2", "#I3", "#J1", "#J2", "#J3", "#J4", "#J5", "#K2", "#K2d", "#K3", "#K4", "#K4d", "#K5", "#K6", "#K9", "#KA", "#KB", "#KC", "#KD", "#M3", "#M3d", "#M4", "#N1", "#N2", "#N3", "#N4", "#N5", "#N6", "#N7", "#N8"]

   # read and tokenize text
   text = open(file,"r", encoding="unicode_escape").read()
   text = text.replace("\n", " #eol ")
   text = word_tokenize(text) 

   # join ampersand and following string
   ampersand = False
   tmp = []
   for t in text:
      if t == "#":
         ampersand = True
      else:
         if ampersand:
            tmp.append("#" + t)
         else: 
            tmp.append(t)
         ampersand = False
        
   text = tmp   

   # search for position of labels in text and remove labels from text
   text_out = []
   tags = []
   c = 0
   next_label = ""
   for t in text:
      if t in labels:
         if next_label == t:
            p2 = c
            tags.append((next_label, p1, p2))
            next_label = ""
         else:
            next_label = t
            p1 = c
      else:
         text_out.append(t)
         if next_label == "":
            tags.append(("#OO", c, c+1))
         c = c+1

   train_data = []
   for t in tags:
      for i in range(t[2]-t[1]):
         train_data.append((' '.join(text_out[t[1]-5+i:t[1]+5+i+1]), t[0]))

   return train_data 


def idsem_to_list(directory, nbills, out_dir='train_files', ext=0):
    '''Converts IDSEM files to text files with lists of tuples''' 
    files=os.listdir(directory)

    train_data = []

    for file in files[:nbills]:
        #create the bill file
        l = idsem_file_to_list(os.path.join(directory, file))
        train_data= train_data + l
   
    #create a TXT file with Spacy structure for training
    out_str = pprint.pformat(train_data)
    open(out_dir+"/train_data_T%d.txt" % ext,"w", encoding="utf-8").write(out_str)


if __name__ == '__main__':   
   if len(sys.argv) > 1:        
      # 0: script name
      # 1: directory: with the annotated TXT files
      # 2: nbills: number of bills to include in a training file

      nbills = 100
      if len(sys.argv) > 2: nbills = int(sys.argv[2])
      directory = sys.argv[1]
      train_data = idsem_to_list(directory, nbills)

      
   else:
      print ("\nIncorrect number of parameters.\n")
      print ("     > python " + sys.argv[0] + " directory [nbills (100 default)]")
      
