# HonorsContract

The file mchain.py is a library to create markov chains and use them to generate sentences.

The functions included in this file are: (1) portText, (2) getMat, (3) genSent

(1) "Import text file" returns a <list> of the words in the text file in order.
  portText(filename)
  filename - <string> stating the name of the file containing the reference text

(2) "Get probability matrix" returns a <list> of the vocabulary & <numpy.array> of probability weights based on the relationships of the words in the refrence text
  getMat(ref)
  ref - <list> of words reference text
 
(3) "Generate sentence" returns a <string> randomly generated sentence
  genSent(voc,mat,N = 1)
  voc - <list> of vocabulary words
  mat - <numpy.array> describing the probabilities of each word to follow a previous word
  N - (optional) <int> number of sentences to generate
