from django.shortcuts import render,HttpResponse,redirect
from django.http.request import HttpHeaders
from numpy import save, sort
from home.models import Contact,user_token
import requests
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Blogpost
import json
from mac import settings
from oauth2client.service_account import ServiceAccountCredentials
# Create your views here.

# import firebase_admin
# from firebase_admin import credentials, messaging

# cred = credentials.Certificate(settings.cred)
# firebase_admin.initialize_app(cred)

# SCOPES = ['https://www.googleapis.com/auth/sqlservice.admin']

# UserAlreadyExists = False

def send_notification(registration_ids , message_title , message_desc,image_url,slug):
    fcm_api = "AAAAW7CQbWY:APA91bHkdTmXrb87FkVNVLrdHCj7Cy8mJnwqSGrZI5PB0et2aoPo7vHwHPirCoPHrg4IMBvEfHzsIKKlar7hTHyC-yWRD4CzQATrehIq-FUxW8dKC98ARsfK4HxPilbN4pFgGA5pOhKB"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : message_title,
            "image" : "https://movieloverss.com/media/"+str(image_url),
            "icon": "https://movieloverss.com/static/favicon.ico",
            "click_action": "https://movieloverss.com/blog/"+slug,
        }
    }
    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())    


    
def home(request):
    myposts = Blogpost.objects.all().order_by("-pub_date")
    
    # get 4 popular Post 
    popularPosts = Blogpost.objects.all().order_by("-PostViews")
    popularPost = popularPosts[slice(0,4)]
    
    # get letest uploaded posts
    latestPost = Blogpost.objects.last()
    # latestPost = Blogpost.objects.filter(PostViews = 4)
    
    # get 6 latest posts
    lengthOfPosts = len(myposts)
    if(lengthOfPosts >= 6):
        recentPost = myposts[slice(0,6)]
    else:
        recentPost = myposts
        
        
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
    
    
    
    return render(request,'home/home.html', {'myposts': myposts,'latestPost':latestPost,'recentPost':recentPost,'postViews':popularPost,'NoOFAnimePosts':NoOFAnimePosts,'NoOfYouWillLoveToKnowPosts':NoOfYouWillLoveToKnowPosts,'NoOFSuperHeroPosts':NoOFSuperHeroPosts,'NoOFHollywoodPost':NoOFHollywoodPost,'NoOFBollywoodPost':NoOFBollywoodPost})
    # return render(request,'home/home.html', {'myposts': myposts})

def subscribeUs(request):
    if request.method == 'POST':
        
        token = request.POST['token']
        try:
            newUser = user_token(token=token,subscribe=True)
            # newUser = User.objects.create_user("yash","kharey300@gmail.com","1234qwer")
            # newUser.token = token
            newUser.save()
            messages.success(request, 'Thank you for subscribing us')
        except:
            messages.success(request, 'You are already connected with us')
        
        return redirect('/')
        # return redirect("/")
    else:
        return HttpResponse('404 - not Found')

def send(request):
    allUserTokens = user_token.objects.all()
    myposts = Blogpost.objects.last()
    registration  = []
    title = myposts.title
    preContent = myposts.preContent[slice(0,100)]
    poster = myposts.poster
    slug = myposts.slug
    for i in allUserTokens:
        registration.append(i.token)
    
      
    send_notification(registration , title , preContent,poster,slug)
    return redirect("/")



def aboutus(request):
    
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
  
    return render(request,'home/about.html',{'NoOFAnimePosts':NoOFAnimePosts,'NoOfYouWillLoveToKnowPosts':NoOfYouWillLoveToKnowPosts,'NoOFSuperHeroPosts':NoOFSuperHeroPosts,'NoOFHollywoodPost':NoOFHollywoodPost,'NoOFBollywoodPost':NoOFBollywoodPost}) 
    
def contactus(request):     
    
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        subject = request.POST['subject']   
        
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, 'Please fill the form Correctly')
        
        else:
            contact = Contact(name=name ,email=email,phone=phone,content=content)
            contact.save()
            send_mail(subject,'From: ' + email +" - " + content, email,['movieloverss.contact@gmail.com'])
            messages.success(request, 'Your message has been sent')
        
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
  
    return render(request,'home/contact.html',{'NoOFAnimePosts':NoOFAnimePosts,'NoOfYouWillLoveToKnowPosts':NoOfYouWillLoveToKnowPosts,'NoOFSuperHeroPosts':NoOFSuperHeroPosts,'NoOFHollywoodPost':NoOFHollywoodPost,'NoOFBollywoodPost':NoOFBollywoodPost})  

    
def search(request):
    query = request.GET['query']
    if len(query)>70:
        allPost = Blogpost.objects.none()
    else:
        allPostTitle = Blogpost.objects.filter(title__icontains=query)
        allPostAuthor = Blogpost.objects.filter(author__icontains=query)
        allPostContent = Blogpost.objects.filter(content__icontains=query)
        allPost = allPostTitle.union(allPostContent,allPostAuthor).order_by("-pub_date")
            
    if allPost.count() == 0:
         messages.warning(request, 'Please refine your query')
         
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
  
    return render(request,'home/search.html',{'allPost': allPost, 'query':query,'NoOFAnimePosts':NoOFAnimePosts,'NoOfYouWillLoveToKnowPosts':NoOfYouWillLoveToKnowPosts,'NoOFSuperHeroPosts':NoOFSuperHeroPosts,'NoOFHollywoodPost':NoOFHollywoodPost,'NoOFBollywoodPost':NoOFBollywoodPost})  
    # return HttpResponse("this is search")
      