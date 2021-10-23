# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<br><br><br><center><a href="https://facebook.com"><button style="height:50px;width:100px">Facebook</button></a>
#     <a href="https://youtube.com"><button style="height:50px;width:100px">YouTube</button></a>
#     <a href="https://web.whatsapp.com"><button style="height:50px;width:100px">WhatsApp</button></a>
#     <a href="https://open.spotify.com"><button style="height:50px;width:100px">Spotify</button></a></center>''')
#
# def about(request):
#     return HttpResponse('About Dewansh Khandelwal')

def index(request):
    # param = {'name' : 'Dewansh', 'place': 'Ujjain'}
    # return render(request, 'index.html', param)
    return render(request, 'index.html')
    # return HttpResponse("Hello")

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def analyze(request):
    # get the text
    dj_text = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,=<>./?@#$%^&*_~'''
        analyzed = ""
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        # analyze the text
        dj_text = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in dj_text:
            analyzed+=char.upper()
        params = {'purpose':'Capitalizing the Text', 'analyzed_text': analyzed}
        dj_text = analyzed

        # return render(request, 'analyze.html', params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in dj_text:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose':'Capitalizing the Text', 'analyzed_text': analyzed}
        dj_text = analyzed
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(dj_text):
            if not(dj_text[index]==" " and dj_text[index+1]==" "):
                analyzed += char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover != "on"):
        return HttpResponse("Error 404 : Please select at-least one operation and Try Again..!!!")

    return render(request, 'analyze.html', params)
# def capitalzefirst(request):
#     return HttpResponse("capitalzefirst")
#
# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
# def spaceremove(request):
#     return  HttpResponse("spaceremove")
#
# def charcount(request):
#     return HttpResponse("charcount")