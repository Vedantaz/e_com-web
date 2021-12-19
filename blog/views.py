from django.shortcuts import render
from django.http import HttpResponse
from . models import Blogpost
from django.core.paginator import Paginator 

# Create your views here.
def index(request ):
    myposts = Blogpost.objects.all()
    paginator = Paginator(myposts , 2)    # how many objects you want to show  i.e > number 1 becoz we have 4 elements .
    page_number = request.GET.get('page' , 2)    # to get and pass the page or to land in which page firstly .
    p = Paginator(myposts , 2)
    try:
        page = p.page(page_number)
        print(page)
    except :
        page = p.page(2)
        print(page)

    myposts_obj = paginator.get_page(page_number)
    return render(request, "blog/index.html" ,{'myposts':myposts})

def blogpost(request, id):
    
    post = Blogpost.objects.filter(post_id =  id)[0]
    print(post)
    return render(request, "blog/blogpost.html", {'post':post})



    
