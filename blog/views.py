from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost,User_IP
from .models import Blogpost,User_IP,playlist
from itertools import chain

# from math import ceil

bollywood = ""
hollywood = ""
superhero = ""
youWillLoveToKnow = ""
anime = ""

def blogHome(request):
    blogposts = Blogpost.objects.all().order_by("-pub_date")
    playlists = playlist.objects.all()
    allPost = list(chain(playlists,blogposts))
    
    blog_paginator = Paginator(allPost, 12)
    
    page_num = request.GET.get('page')
    
    page = blog_paginator.get_page(page_num)
    NoOfBlog={}
    for i in playlists:
      if(i.playlist == True):
        for j in blogposts:
          if(i.name == j.PlaylistName):
            blogInPlaylist =  Blogpost.objects.filter(PlaylistName = i.name)
                    
            NoOfBlog.update({i.name:blogInPlaylist.count()})
    
    # print(NoOfBlog)
      #get no of category posts
    youWillLoveToKnowPost = Blogpost.objects.filter(category = 'you-will-love-to-know') 
    NoOfYouWillLoveToKnowPosts = len(youWillLoveToKnowPost)
    
    animePosts = Blogpost.objects.filter(category = 'anime') 
    NoOFAnimePosts = len(animePosts)
    
    superheroPost = Blogpost.objects.filter(category = 'superhero') 
    NoOFSuperHeroPosts = len(superheroPost)
    
    hollywoodPost = Blogpost.objects.filter(category = 'hollywood') 
    NoOFHollywoodPost = len(hollywoodPost)
    
    bollywoodPost = Blogpost.objects.filter(category = 'bollywood') 
    NoOFBollywoodPost = len(bollywoodPost)
    
    context = {
        'page': page,
        "blog_paginator":blog_paginator,
        "allPost":allPost,
        'blogposts':blogposts,
        "playlists":playlists,
        "NoOfBlog":NoOfBlog,
        'NoOFAnimePosts':NoOFAnimePosts,
        'NoOfYouWillLoveToKnowPosts':NoOfYouWillLoveToKnowPosts,
        'NoOFSuperHeroPosts':NoOFSuperHeroPosts,
        'NoOFHollywoodPost':NoOFHollywoodPost,
        'NoOFBollywoodPost':NoOFBollywoodPost
    }
    
    return render(request,'blog/blogHome.html', context)

def blogpost(request,slug):
    post = Blogpost.objects.filter(slug = slug)[0]
    
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
    
    animePosts = Blogpost.objects.filter(category = 'anime') 
    NoOFAnimePosts = len(animePosts)
    
    superheroPost = Blogpost.objects.filter(category = 'superhero') 
    NoOFSuperHeroPosts = len(superheroPost)
    
    hollywoodPost = Blogpost.objects.filter(category = 'hollywood') 
    NoOFHollywoodPost = len(hollywoodPost)
    
    bollywoodPost = Blogpost.objects.filter(category = 'bollywood') 
    NoOFBollywoodPost = len(bollywoodPost)
    
    return render(request,'blog/blogpost.html',{'post':post,'view':view,'NoOFAnimePosts':NoOFAnimePosts,'NoOfYouWillLoveToKnowPosts':NoOfYouWillLoveToKnowPosts,'NoOFSuperHeroPosts':NoOFSuperHeroPosts,'NoOFHollywoodPost':NoOFHollywoodPost,'NoOFBollywoodPost':NoOFBollywoodPost})
    
def category_bollywood(request):
    post = Blogpost.objects.filter(category = 'bollywood').order_by("-pub_date")

    
    bollywood = "active"
      #get no of category posts
    youWillLoveToKnowPost = Blogpost.objects.filter(category = 'you-will-love-to-know') 
    NoOfYouWillLoveToKnowPosts = len(youWillLoveToKnowPost)
    
    animePosts = Blogpost.objects.filter(category = 'anime') 
    NoOFAnimePosts = len(animePosts)
    
    superheroPost = Blogpost.objects.filter(category = 'superhero') 
    NoOFSuperHeroPosts = len(superheroPost)
    
    hollywoodPost = Blogpost.objects.filter(category = 'hollywood') 
    NoOFHollywoodPost = len(hollywoodPost)
    
    bollywoodPost = Blogpost.objects.filter(category = 'bollywood') 
    NoOFBollywoodPost = len(bollywoodPost)
    
    return render(request,'blog/category.html', {'myposts': post,'bollywood':bollywood,'NoOFAnimePosts':NoOFAnimePosts,'NoOfYouWillLoveToKnowPosts':NoOfYouWillLoveToKnowPosts,'NoOFSuperHeroPosts':NoOFSuperHeroPosts,'NoOFHollywoodPost':NoOFHollywoodPost,'NoOFBollywoodPost':NoOFBollywoodPost,'NoOFAnimePosts':NoOFAnimePosts,'NoOfYouWillLoveToKnowPosts':NoOfYouWillLoveToKnowPosts,'NoOFSuperHeroPosts':NoOFSuperHeroPosts,'NoOFHollywoodPost':NoOFHollywoodPost,'NoOFBollywoodPost':NoOFBollywoodPost})
   
def category_hollywood(request):
   
    post = Blogpost.objects.filter(category = 'hollywood').order_by("-pub_date")
 
    hollywood = "active"
      #get no of category posts
    youWillLoveToKnowPost = Blogpost.objects.filter(category = 'you-will-love-to-know') 
    NoOfYouWillLoveToKnowPosts = len(youWillLoveToKnowPost)
    
    animePosts = Blogpost.objects.filter(category = 'anime') 
    NoOFAnimePosts = len(animePosts)
    
    superheroPost = Blogpost.objects.filter(category = 'superhero') 
    NoOFSuperHeroPosts = len(superheroPost)
    
    hollywoodPost = Blogpost.objects.filter(category = 'hollywood') 
    NoOFHollywoodPost = len(hollywoodPost)
    
    bollywoodPost = Blogpost.objects.filter(category = 'bollywood') 
    NoOFBollywoodPost = len(bollywoodPost)
    return render(request,'blog/category.html', {'myposts': post,'hollywood':hollywood,'NoOFAnimePosts':NoOFAnimePosts,'NoOfYouWillLoveToKnowPosts':NoOfYouWillLoveToKnowPosts,'NoOFSuperHeroPosts':NoOFSuperHeroPosts,'NoOFHollywoodPost':NoOFHollywoodPost,'NoOFBollywoodPost':NoOFBollywoodPost})
   
def category_superhero(request):
    post = Blogpost.objects.filter(category = 'superhero').order_by("-pub_date")
   
    superhero = "active"
      #get no of category posts
    youWillLoveToKnowPost = Blogpost.objects.filter(category = 'you-will-love-to-know') 
    NoOfYouWillLoveToKnowPosts = len(youWillLoveToKnowPost)
    
    animePosts = Blogpost.objects.filter(category = 'anime') 
    NoOFAnimePosts = len(animePosts)
    
    superheroPost = Blogpost.objects.filter(category = 'superhero') 
    NoOFSuperHeroPosts = len(superheroPost)
    
    hollywoodPost = Blogpost.objects.filter(category = 'hollywood') 
    NoOFHollywoodPost = len(hollywoodPost)
    
    bollywoodPost = Blogpost.objects.filter(category = 'bollywood') 
    NoOFBollywoodPost = len(bollywoodPost)
    return render(request,'blog/category.html', {'myposts': post,'superhero':superhero,'NoOFAnimePosts':NoOFAnimePosts,'NoOfYouWillLoveToKnowPosts':NoOfYouWillLoveToKnowPosts,'NoOFSuperHeroPosts':NoOFSuperHeroPosts,'NoOFHollywoodPost':NoOFHollywoodPost,'NoOFBollywoodPost':NoOFBollywoodPost})
   
def category_youWillLoveToKnow(request):
    post = Blogpost.objects.filter(category = 'you-will-love-to-know').order_by("-pub_date")
   
    youWillLoveToKnow = "active"
      #get no of category posts
    youWillLoveToKnowPost = Blogpost.objects.filter(category = 'you-will-love-to-know') 
    NoOfYouWillLoveToKnowPosts = len(youWillLoveToKnowPost)
    
    animePosts = Blogpost.objects.filter(category = 'anime') 
    NoOFAnimePosts = len(animePosts)
    
    superheroPost = Blogpost.objects.filter(category = 'superhero') 
    NoOFSuperHeroPosts = len(superheroPost)
    
    hollywoodPost = Blogpost.objects.filter(category = 'hollywood') 
    NoOFHollywoodPost = len(hollywoodPost)
    
    bollywoodPost = Blogpost.objects.filter(category = 'bollywood') 
    NoOFBollywoodPost = len(bollywoodPost)
    return render(request,'blog/category.html', {'myposts': post,'youWillLoveToKnow':youWillLoveToKnow,'NoOFAnimePosts':NoOFAnimePosts,'NoOfYouWillLoveToKnowPosts':NoOfYouWillLoveToKnowPosts,'NoOFSuperHeroPosts':NoOFSuperHeroPosts,'NoOFHollywoodPost':NoOFHollywoodPost,'NoOFBollywoodPost':NoOFBollywoodPost})
   
def category_anime(request):
    post = Blogpost.objects.filter(category = 'anime').order_by("-pub_date")
   
    anime = "active"
      #get no of category posts
    youWillLoveToKnowPost = Blogpost.objects.filter(category = 'you-will-love-to-know') 
    NoOfYouWillLoveToKnowPosts = len(youWillLoveToKnowPost)
    
    animePosts = Blogpost.objects.filter(category = 'anime') 
    NoOFAnimePosts = len(animePosts)
    
    superheroPost = Blogpost.objects.filter(category = 'superhero') 
    NoOFSuperHeroPosts = len(superheroPost)
    
    hollywoodPost = Blogpost.objects.filter(category = 'hollywood') 
    NoOFHollywoodPost = len(hollywoodPost)
    
    bollywoodPost = Blogpost.objects.filter(category = 'bollywood') 
    NoOFBollywoodPost = len(bollywoodPost)
    return render(request,'blog/category.html', {'myposts': post,'anime':anime,'NoOFAnimePosts':NoOFAnimePosts,'NoOfYouWillLoveToKnowPosts':NoOfYouWillLoveToKnowPosts,'NoOFSuperHeroPosts':NoOFSuperHeroPosts,'NoOFHollywoodPost':NoOFHollywoodPost,'NoOFBollywoodPost':NoOFBollywoodPost})
   