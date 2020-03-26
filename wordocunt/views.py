from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddic = {}
    for word in wordlist:
        if word not in worddic.keys():
            worddic[word] = 1
        else:
            worddic[word] += 1
    sortedwords = sorted(worddic.items(), key = operator.itemgetter(1), reverse = True)



    return render(request, 'count.html', {'completetext':fulltext, 'count': len(wordlist), 'sort_w': sortedwords})
    # items() method is used to return the list with all the dictionalry keys with values
    '''
    https://www.geeksforgeeks.org/python-dictionary-items-method/
    '''
def about(request):
    return render(request, 'about.html')
