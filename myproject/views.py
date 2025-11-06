from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

# def home(request):
#     return HttpResponse("Welcome to Home Page")


# def contact(request):
#     return HttpResponse("Contact view function view based")


# class About(View):
#     def get(self, request):
#         return HttpResponse("Class Based view")


def profile(request,username):
    return HttpResponse(f"Hi {username}")

def product_detail(request, id):
    return redirect('blog-post', id)

def blog_post(request, slug):
    return HttpResponse(f"Blog Slug: {slug}")

def item_detail(request, item_id):
    return HttpResponse(f"Item UUID is: {item_id}")

def media_handler(request, path_file):
    return HttpResponse(f"Path File is: {path_file}")


def go_to_post(request):
    url = reverse('go_to_post')
    return HttpResponse(f"URL Path: {url}")