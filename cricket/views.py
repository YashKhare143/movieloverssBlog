from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cricketpost,User_IP
from blog.models import Blogpost
from itertools import chain

# from math import ceil

bollywood = ""
hollywood = ""
superhero = ""
youWillLoveToKnow = ""
anime = ""

def cricketHome(request):
    blogposts = Cricketpost.objects.all().order_by("-pub_date")
    
    # blog_paginator = Paginator(Cricketpost, 12)
    # page_num = request.GET.get('page')
    
    # page = blog_paginator.get_page(page_num)
    
    # print(NoOfBlog)
      #get no of category posts
    youWillLoveToKnowPost = Blogpost.objects.filter(category = 'you-will-love-to-know') 
    NoOfYouWillLoveToKnowPosts = len(youWillLoveToKnowPost)
    
    cricketPosts = Cricketpost.objects.filter(category = 'cricket') 
    NoOFCricketPosts = len(cricketPosts)
    
    superheroPost = Blogpost.objects.filter(category = 'superhero') 
    NoOFSuperHeroPosts = len(superheroPost)
    
    hollywoodPost = Blogpost.objects.filter(category = 'hollywood') 
    NoOFHollywoodPost = len(hollywoodPost)
    
    bollywoodPost = Blogpost.objects.filter(category = 'bollywood') 
    NoOFBollywoodPost = len(bollywoodPost)
    
    context = {
        # 'page': page,
        # "blog_paginator":blog_paginator,
        'blogposts':blogposts,
        'NoOFCricketPosts':NoOFCricketPosts,
        'NoOfYouWillLoveToKnowPosts':NoOfYouWillLoveToKnowPosts,
        'NoOFSuperHeroPosts':NoOFSuperHeroPosts,
        'NoOFHollywoodPost':NoOFHollywoodPost,
        'NoOFBollywoodPost':NoOFBollywoodPost
    }
    
    return render(request,'cricket/cricketHome.html', context)

def cricketpost(request,slug):
    post = Cricketpost.objects.filter(slug = slug)[0]
    
    def get_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
        
    userisUnique=True;
    ip=get_ip(request)
    user= User_IP(userIP=ip,slug = slug)
    postSlug = User_IP.objects.filter(slug=slug)
    for i in postSlug:
        if(ip==i.userIP):
            userisUnique = False
            
    if(userisUnique==True):
        # userisUnique=True  
        user.save()
        # print('user is unique true')
    else:
        pass
        # print('user is unique false')
        # print('user is ',ip)
        
        
    view=User_IP.objects.filter(slug=slug).count()
    post.PostViews = view
    post.save()
    
      #get no of category posts
    youWillLoveToKnowPost = Blogpost.objects.filter(category = 'you-will-love-to-know') 
    NoOfYouWillLoveToKnowPosts = len(youWillLoveToKnowPost)
    
    cricketPosts = Cricketpost.objects.filter(category = 'cricket') 
    NoOFCricketPosts = len(cricketPosts)
    
    superheroPost = Blogpost.objects.filter(category = 'superhero') 
    NoOFSuperHeroPosts = len(superheroPost)
    
    hollywoodPost = Blogpost.objects.filter(category = 'hollywood') 
    NoOFHollywoodPost = len(hollywoodPost)
    
    bollywoodPost = Blogpost.objects.filter(category = 'bollywood') 
    NoOFBollywoodPost = len(bollywoodPost)
    
    return render(request,'cricket/cricketpost.html',{'post':post,'view':view,'NoOFCricketPosts':NoOFCricketPosts,'NoOfYouWillLoveToKnowPosts':NoOfYouWillLoveToKnowPosts,'NoOFSuperHeroPosts':NoOFSuperHeroPosts,'NoOFHollywoodPost':NoOFHollywoodPost,'NoOFBollywoodPost':NoOFBollywoodPost})
   
