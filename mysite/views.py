# i have created the file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def analyze(request):
    # GET THE TEXT****************************************************************************


    djtext = request.POST.get('text', 'default')

    # RETRIVING CHECKBOXES**************************************************************
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps= request.POST.get('fullcaps', 'off')
    newlineremover= request.POST.get('newlineremover', 'off')
    spaceremover= request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    processDic={'removepunc':removepunc, 'fullcaps':fullcaps, 'newlineremover':newlineremover,'spaceremover':spaceremover,'charcount': charcount}
    tempcContent=" "
    purpose= " "
    # CHECKING CHECKBOXES**************************************************************************
    l=[]

    for key, value in processDic.items():

        print(str(key)+','+str(value))

        if(str(value)=='on'):

            if(str(key)=='removepunc'):
                l.append("Removed Punctuations")
                s="Removed Punctuations \t"
                punctuations = ''' !()-[]{};:'"<>.,/\?@#$%^&*_~ '''
                analyzed = ""
                for char in djtext:
                    if char not in punctuations:
                        analyzed= analyzed + char
                params= {'purpose':s, 'analyzed_text': analyzed}
                djtext = analyzed


            if(str(key)=='fullcaps'):
                l.append("Change to Uppercase")

                analyzed = ""
                for char in djtext:
                    analyzed= analyzed + char.upper()
                params = {'purpose': l, 'analyzed_text': analyzed}
                djtext = analyzed


            if(str(key)=='newlineremover'):
                l.append("New Line Remover")
                analyzed = ""
                for char in djtext:
                    if char!= "\n" and char!="\r":
                        analyzed = analyzed + char
                params = {'purpose': l, 'analyzed_text': analyzed}
                djtext=analyzed


            if (str(key) == 'spaceremover'):
                l.append("Extra Space Remover")
                analyzed = ""
                for index, char in enumerate(djtext):
                    if not (djtext[index] == " " and djtext[index + 1] == " "):
                        analyzed = analyzed + char
                params = {'purpose': l, 'analyzed_text': analyzed}
                djtext = analyzed

            if(str(key)=='charcount'):
                l.append("Character Counter")
                a= len(djtext)
                analyzed = djtext+"\n count="+str(a)

                params = {'purpose': l, 'analyzed_text': analyzed}
                djtext = analyzed

        # ANAYZE THE TEXT
    return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse("ERROR")



# **********************************************************************************************************************