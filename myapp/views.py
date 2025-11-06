from django.http import Http404
from django.shortcuts import get_object_or_404, render,redirect
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash

from .forms import BlogPostForm

from .models import Profile
from .models import BlogPost
from .models import Blog
from .models import Student
from .forms import RegistrationForm
from .forms import EventForm
from .models import BlogPermissionPost

from .models import Book
from django.db.models import Avg, Count, Max, DecimalField, F, ExpressionWrapper

#Basic QUeries

def basic_queries(request):
    try:
        all_books = Book.objects.all() # SELECT * FROM book;
        filter_books = Book.objects.filter(author__name='apj') # SELECT * FROM book WHERE author_name = 'apj';
        exclude_books = Book.objects.exclude(price__lt=500)
        get_book = Book.objects.get(title='wings of fire')

        context = {
            'all_books' : all_books,
            'filter_books' : filter_books,
            'exclude_books' : exclude_books,
            'get_book' : get_book
        }

        return render(request, 'basic_queries.html', context)
    except Book.DoesNotExist:
        raise Http404("Book not found")



#Aggregations

def aggregation_demo(request):
    avg_price = Book.objects.aggregate(Avg('price'))
    total_books = Book.objects.aggregate(Count('id'))
    max_price = Book.objects.aggregate(Max('price'))

    annotated_books = Book.objects.annotate(
        discounted_price = ExpressionWrapper(
            F('price') * 0.9,
            output_field = DecimalField(max_digits=6, decimal_places =2)
        )
    )

    context = {
        'avg_price' : avg_price,
        'total_books' : total_books,
        'max_price' : max_price,
        'annotated_books' : annotated_books
    }

    return render(request, 'aggregation.html', context)


#F Expression
def f_expression_demo(request):
    Book.objects.update(price=F('price')+50)
    books = Book.objects.all()
    return render(request, 'f_expression.html', {'books' : books})

#Raw SQL 

def raw_sql_demo(request):
    books = Book.objects.raw('SELECT id, title, price FROM myapp_book WHERE price > %s', [300])
    return render(request, 'raw_sql.html', {'books' : books})

#query Optimization

def optimization_demo(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'optimization.html', {'books': books})

def custom_manager_demo(request):
    expensive_books = Book.objects.expensive()
    return render(request, 'custom_manager.html', {'books' : expensive_books})

@login_required
@permission_required('myapp.add_blogpermissionpost',raise_exception=True)
def add_blog_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        BlogPermissionPost.objects.create(title=title, content=content, author=request.user)
        messages.success(request, "Blog post added successfully!!")
        return redirect("dashboard")
    
    return render(request, "add_blog.html")


@login_required
@permission_required('myapp.change_blogpermissionpost',raise_exception=True)
def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPermissionPost, id= post_id)
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        messages.success(request, "Blog post updated successfully!!")
        return redirect("view_posts")
    return render(request,"edit_blog.html", {"post":post})



@login_required
def view_posts(request):
    posts = BlogPermissionPost.objects.all()
    return render(request, "view_posts.html",{"posts":posts})


@login_required

@permission_required('myapp.delete_blogpermissionpost',raise_exception=True)

def delete_blog_post(request, post_id):
    post = get_object_or_404(BlogPermissionPost, id=post_id)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Blog post deleted successfully!!")
        return redirect("view_posts")
    return render(request, "delete_blog.html", {"post":post})



















































def register_auth(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully!!!")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request,"register_auth.html",{"form":form})



def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "login.html",{"form":form})


def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully!!!")
            return redirect("dashboard")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "change_password.html", {"form": form})
















def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            return render(request,"event_success.html",{"name": form.cleaned_data['name']})
    else:
        form = EventForm()
        return render(request,"creat_event.html",{"form":form})
        






















def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username = username,email=email,password=password)
            return render(request, "success.html",{"username": username})
        else:
            return render(request,"register.html",{"form":form})
    else:
        form = RegistrationForm()
        return render(request,"register.html",{"form":form})














def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = BlogPostForm()
    return render(request, "create_post.html",{"form":form})



















def one_to_one_demo(request):
    users = User.objects.select_related('profile').all()
    # profile = Profile.objects.filter(user=user).first()
    return render(request,'one_to_one.html', {'users':users, 'profile': profile})


def one_to_many_demo(request):
    blog = Blog.objects.first()
    comments = blog.comment_set.all()if blog else []
    return render(request, 'one_to_many.html',{'blog':blog, 'comments':comments})


def many_to_many_demo(request):
    student = Student.objects.first()
    courses = student.courses.all() if student else []
    return render(request, 'many_to_many.html',{'student':student, 'courses':courses})







def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, "post_list.html", {"posts" : posts})























# Create your views here.

# def home(request):
#     context = {
#         'user_name' : 'Zaheer',
#         'items' : ['Laptop','Mobile','Tablet']
#     }
#     return render(request, "home.html", context)

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request,'about.html')

def post_detail(request):
    post={"title": "My Blog", "created_at": datetime(2025,1,24,10,22)}
    return render(request, "post_detail.html", {"post": post})

def profile(request):
    user = {"username": "ravi"}
    return render(request,"profile.html", {"user":user})

def user_list(request):
    users = ["Ravi", "Sita", "Arjun", "Priya", "Kiran"]
    return render(request,"users.html", {"users":users})

def product_detail(request):
    product = {"name": "Laptop", "price":50000}
    return render(request, "product_detail.html", {"product" :product})

def welcome(request):
    user = {"is_authenticated": False, "username":"Ravi"}
    return render(request, "welcome.html", {"user": user})

def items_list(request):
    items = ["Apple", "Banana", "Mango"]
    return render(request, "items.html", {"items": items})