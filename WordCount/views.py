from django.http import HttpResponse
from django.shortcuts import render
import operator
import string

def home(request):
    return render(request, 'home.html')

def count2(request):
    return render(request, 'count2.html')

def count(request):
    fullText = request.GET['fullText']
    lowerFullText = fullText.lower()
    newFullText = ""

    for i in lowerFullText:
        if i not in string.punctuation:
            newFullText += i

    wordlist = newFullText.split()
    sentenceslist = fullText.split(".")

    wordDictionary = {}

    for word in wordlist:
        if word in wordDictionary:
            #Increase
            wordDictionary[word] += 1
        else:
            #Add to the dicitonary
            wordDictionary[word] = 1
    sort_wordDictionary = sorted(wordDictionary.items(), key=lambda x: (x[1], x[0]), reverse=True)
    return render(request, 'count.html', {'fullText':fullText, 'count':len(wordlist), 'wordDictionary': sort_wordDictionary, 'sentencesCount':len(sentenceslist)-1})