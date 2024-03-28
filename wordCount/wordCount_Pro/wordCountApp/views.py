from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")

def wordCount(request):
    return render(request, "wordCount.html")

def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()

    #전체 글자 수
    characters = len(entered_text)

    #띄어쓰기 제외 글자수
    characters_nospace = characters

    for i in range(characters_nospace):
        if ' ' in entered_text[i]:
            characters_nospace -= 1


    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, "result.html", {'characters' : characters, 'characters_nospace' : characters_nospace, 'word_list': word_list, 'alltext': entered_text, 'dictionary': word_dictionary.items()}, )

def hello(request):
    entered_name = request.GET['myname']

    return render(request, "hello.html", {'myname': entered_name})