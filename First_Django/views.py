
from django.http import HttpResponse
from django.shortcuts import render
import operator
from . import counter
def home(request):
    return render(request,'index.html',{'key1':'I am from python code'})
#
def results(request):
    # age = request.GET['user_age']
    # name = request.GET['user_name']
    # message = f'Hi {name}, you are {age} years old'
    article = request.GET['article']
    # words = article.split()
    # words_count = len(words)
    # dict_words = {}
    # for word in words:
    #     if word in dict_words:
    #         dict_words[word] += 1
    #     else:
    #         dict_words[word] = 1
    # var_dict = sorted(dict_words.items(),key=operator.itemgetter(1),reverse=True)
    var_dict,words_count = counter.count(article)
    # return render(request,'result.html',{'age':message})
    return render(request,'result.html',{'article':article,'words_count':words_count,'dict_words':var_dict})
