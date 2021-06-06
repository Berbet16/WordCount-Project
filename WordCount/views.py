from django.http import HttpResponse
from django.shortcuts import render
import operator
import string

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext'].lower()

    newFulltext = ""

    for i in fulltext:
        if i not in string.punctuation:
            newFulltext += i

    wordlist = newFulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})