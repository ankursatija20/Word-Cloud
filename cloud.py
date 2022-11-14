#!/usr/bin/env python3
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys




file_contents = "hello cloud ffrr waed yth the in a resw qasd frty huij kfmv nsad cbaq wes frt ' dfer .\
llook cdsa we you in it Whew! That was a lot. All of the and  ssss kkk the arwfeg sityo ldkej \
ssscccff for your and uploader widget To uplo file, run the following cell that contains all the code for "


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "in","for","s", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    
    result ={}
    a = file_contents.split()
    for word in a:
        if word in uninteresting_words:
            pass
        else:
            for letter in word:
                if letter in punctuations:
                    letter.replace(punctuations,"")
            if word not in result.keys():
                result[word]= 1
                
            else:
                result[word] += 1
                
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(result)
    return cloud.to_array()
    
    # Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()

