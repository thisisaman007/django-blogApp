from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'author':'aman',
        'title': "Aman's post 1",
        'content': 'hey this is aman srivsstava and this is my first django project , copy pasted from the corey shefers tutorials.',
        'date_posted': '30th May, 2020'
    },  {
        'author':'aman',
        'title': "Aman's post 111",
        'content': 'hey this is aman srivsstava and this is my first django project , copy pasted from the corey shefers tutorials.',
        'date_posted': '30th May, 2020'
    },  {
        'author':'aman',
        'title': "Aman's post 1222",
        'content': 'hey this is aman srivsstava and this is my first django project , copy pasted from the corey shefers tutorials.',
        'date_posted': '30th May, 2020'
    }
]
def home(request):
    context={
        "posts":posts
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html')