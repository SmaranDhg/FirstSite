""" this is first web application """

''' here we learn how the http resposnse works '''

from django.http import HttpResponse
from django.shortcuts import render
import string
import re

''' this was first intro class so basics '''

# ''' methods are loaded with the help of http respose we use dive into certain url path '''
# ''' all the methods should get the http request as argument and http resposse as the return isnt that intuitive '''
# def index(request):
#     return HttpResponse('''<h1>Harry</h1>
#      <a href="https://github.com/SmaranDhg/WW3
# "> GitHub of Smaran </a>>''')

# def About(request):
#     return HttpResponse("about\nmotherfucker") 


# here the url pipline 
#  '''
def index(request):
      return render(request,"Index2.html")


def Dishes(request):
    return HttpResponse(''' <h1> Dishes </h1> 
    <ol><dl>
    <dl>
    <a href="Applepie/">Applepie</a>
    </dt>
    <dd>Trust me its dillicius</dd>
    </dl>
    <dl>Cran Berry Cheese Cake</dt>
    <dd>oh! its cheesy</dd>
    </dl>
    <dl>Spicey cottage Cheese</dt>
    <dd>Yeah, never good with the spice you know</dd>
    </dl>
    </ol> ''')



def Applepie(request):
    return render(request,"Applepie.html")


def CranberryCheeseCake(request):
    return HttpResponse("")


def SpiceyCottageCheese(request):
    return HttpResponse("")

# you can manipulate with data given  by the user as follow
def Analyzer(request):
    # just printing what is input in the screen
    #  djText=request.GET.get("text","default")

    ''' now for the post request we use '''
    djText=request.POST.get('text','default')
    # now the input from the checkbox
    rmPunc=request.POST.get("rmPunc","off")
    print(rmPunc)#here the texxt is just the name of text area which store the input string in the string
    print(djText)
    # now to remove the punction we use the translation
    analyzed=djText
    if rmPunc=="on":
     trans=djText.maketrans("","",string.punctuation);
     analyzed=djText.translate(trans)
    else:
        return HttpResponse("error")
        

    # now the definig the parameters
    params={"purpose":"Remove Punctuation",'analyzed_text':analyzed}
    return render(request,"analyze2.html",params)

