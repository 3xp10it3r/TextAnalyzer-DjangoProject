# this is created by me -- happy
from django.http import HttpResponse
from django.shortcuts import render
import string
# from itertools import Counter
#
from collections import Counter



def index(request):
    return render(request, 'index1.html')


def analyzer(request):
    textget = request.GET.get('text', 'default')
    punOn = request.GET.get('tb', 'off')
    newline = request.GET.get('nl',"off")
    extraspace = request.GET.get('es',"off")
    upperc = request.GET.get("up","off")
    lowerc = request.GET.get("lw","off")
    charcount = request.GET.get("cc","off")
    # print(textget,punOn)
    if (punOn == "on"):
        analyzed_Value = textget.translate(str.maketrans(dict.fromkeys(string.punctuation)))
        params = {'purpose': 'Punctuation Analyzed', 'analyzed_Value': analyzed_Value}
        return render(request, 'analyzed1.html', params)
    elif(newline=='on'):
        analyzed_Value = ""
        for char in textget:
            if(char=='\n'):
                continue
            analyzed_Value+=char
        # analyzed_Value = textget.translate(str.maketrans(dict.fromkeys(string.punctuation)))
        params = {'purpose': 'New Line Remover', 'analyzed_Value': analyzed_Value}
        return render(request, 'analyzed1.html', params)
    elif(extraspace=="on"):
        analyzed_Value = textget.replace("  "," ")
        params = {'purpose': 'ExtraSpace Remover', 'analyzed_Value': analyzed_Value}
        return render(request, 'analyzed1.html', params)
    elif(upperc=="on"):
        analyzed_Value = textget.upper()
        params = {'purpose': 'UpperCase', 'analyzed_Value': analyzed_Value}
        return render(request, 'analyzed1.html', params)
    elif(lowerc=="on"):
        analyzed_Value = textget.lower()
        params = {'purpose': 'LowerCase', 'analyzed_Value': analyzed_Value}
        return render(request, 'analyzed1.html', params)
    elif(charcount=="on"):
        x=Counter(textget)
        li=[]
        for key,value in x.items():
            li.append([key,value])
        analyzed_Value = li
        params = {'purpose': 'CharCounts', 'analyzed_Value': analyzed_Value}
        return render(request, 'analyzed1.html', params)
    else:
        return HttpResponse("Error")

# def textAccess(request):
#     f = open("one.txt","r")
#     return HttpResponse(f.read())

# def CapitalizeFirst(request):
#     textg = request.GET.get('text','default')
#     return HttpResponse('''<button onclick="document.location='http://127.0.0.1:8000/templateAccess'">HOME</button>''')


# def about(request):
#     return HttpResponse("<h1>HAppy BHai ka Website</h1>")


# def removePunc(request):
#     return HttpResponse('''<button onclick="document.location='http://127.0.0.1:8000/templateAccess'">HOME</button>''')
# def newlineRemove(request):
#     return HttpResponse("New line Remover")
# def spaceRemove(request):
#     return HttpResponse("space Remover")
# def splitted(request):
#     return HttpResponse("splitted")
# def templateAccess(request):
#     # params = {'name':'Digvijay','place':'USA'}
#     # return render(request,'index.html',params)
#     return render(request,'index.html')
