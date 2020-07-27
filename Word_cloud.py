# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:13:35 2020

@author: chiku
"""
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import io
import sys

my_file = open("finalproject.txt")
file_contents = my_file.read()
print(file_contents)


def calculate_frequencies(file_contents):
  
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    frequencies = {}
    words = file_contents.split()
    for word in words:
        if not word.lower() in uninteresting_words:
            for punctuation in punctuations:
                if punctuation in word:
                    word = word.replace(punctuation,"")
            if not word.lower() in frequencies:
                frequencies[word.lower()]=0
            frequencies[word.lower()] += 1
    
    
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()

my_file.close()