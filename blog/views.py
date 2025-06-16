from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import Http404
from django.urls import reverse
import logging
from .models import Post, AboutUs
from django.core.paginator import Paginator
from .forms import ContactForm
# Create your views here.

# static demo data.......
# posts = [
#         {'id':1,'title': 'Post 1', 'content': "Content of the Post 1"},
#         {'id':2,'title': 'Post 2', 'content': "Content of the Post 2"},
#         {'id':3,'title': 'Post 3', 'content': "Content of the Post 3"},
#         {'id':4,'title': 'Post 4', 'content': "Content of the Post 4"},
#         ]

def index(request):
    blog_title="Latest Posts"
    # getting data from post model
    all_posts= Post.objects.all()

    # paginotor
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # logger=logging.getLogger("TESTING")
    # logger.debug(f'the page_obj variable is {page_obj}')
    # logger.debug(f'the page_number variable is {page_number}')
    # logger.debug(f'the paginator variable is {paginator}')
    # logger.debug(f'the all_posts variable is {all_posts}')

    return render(request,'blog/index.html',{'blog_title':blog_title, 'page_obj':page_obj})

def detail(request, slug):
    # static data
#    post= next((item for item in posts if item['id'] == int(post_id)), None)
    try:
# getting data from post id
        post= Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post  doesnot Exisit")
#    logger=logging.getLogger("TESTING")
#    logger.debug(f'the post variable is {post}')
    return render(request,'blog/detail.html',{'post':post,'related_posts':related_posts})

def plan(request,plan_id):
    return HttpResponse(f"hi iam in plan number in {plan_id}")

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("this is new URL")

def contact_view(request):
    if request.method =='POST':
         form=ContactForm(request.POST)
         name=request.POST.get('name')
         email=request.POST.get('email')
         message=request.POST.get('message')
         if form.is_valid():
            logger= logging.getLogger("TESTING")
            logger.debug(f'the form variable is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
            
            # SEND EMAIL
            success_message=" YOUR  EMAIL HAS BEEN SENT SUCESSFULLY, THANK YOU "
            return render(request,'blog/contact.html',{'form':form, 'success_message':success_message})
         else:
            logger= logging.getLogger("TESTING")
            logger.debug('The form validation is failure')
            return render(request,'blog/contact.html',{'form':form, 'name':name, 'email':email, 'message':message})
    return render(request,'blog/contact.html',{'blog_title':'Contact Us'})

def about_view(requests):
    about_content= AboutUs.objects.first().content
    return render(requests,'blog/about.html',{'about_content':about_content})
