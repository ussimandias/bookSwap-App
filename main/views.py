# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from main.models import courseBook
from main.models import Buy
from main.models import Wishlist
from main.models import BookClub
from django.shortcuts import render_to_response
from main.models import Sale
from django import forms
from django.template import RequestContext
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate

class AuthorForm(forms.Form):
    first = forms.CharField(max_length=100)
    last = forms.CharField(max_length=100)
    #sender = forms.EmailField()
    #cc_myself = forms.BooleanField(required=False)

class ContactForm(forms.Form):
    Book = forms.CharField(max_length=100)
    Author = forms.CharField()
    user = forms.CharField()
    #user = forms.EmailField()
    #cc_myself = forms.BooleanField(required=False)

#class ContactForm(forms.Form):
#    subject = forms.CharField(max_length=100)
#    message = forms.CharField()
#    sender = forms.EmailField()
#    cc_myself = forms.BooleanField(required=False)

def home(request):
    book = courseBook.objects.all()
    #prnMsg = 'We have ' + str(len(book)) + 'Books'
    q = len(book)
    users= User.objects.count()
    #noun = 'book' if q==1  else 'books'
    f = AuthorForm()


    #return HttpResponse('Wellcome to my home page\n'+ prnMsg)
    return render_to_response('home.html',
    {'booklog': q,'users':users, 'login':request.user, 'form': f}, 
     context_instance=RequestContext(request))


def books(request):
    book = courseBook.objects.all()
    #Title = BookClub.objects.all()
    #q = len(Title)
    
    if request.method == 'POST':
        k = ContactForm(request.POST)
        if k .is_valid(): 
            #process form
        
            k = Buy(Title = k.cleaned_data['Book'], 
                      Owner = k.cleaned_data['user'],
                      author = k.cleaned_data['Author'])
            
            k.save()   
   
            return HttpResponse('The Book title was sucessully added!! %s %s %s' %(k.Title, k.Owner, k.author))


    else:
        k = ContactForm() 
        

    return render_to_response ('books.html', 
    {'list':books, 'form': k }, context_instance=RequestContext(request))
 
## uncomment to revert to step back    
#    return render_to_response('books.html', 
#   {'books':book , 'list':book, 'form': k })
    #return HttpResponse("Book list goes here")


def detail(request, id):
    book = courseBook.objects.get(id = id)
    return render_to_response('detail.html', {'book':book})    
    #return HttpResponse("Book detail view for id" + id)
    #return HttpResponse("Book detail view for" + book.Title)
    

def buyView(request):
    #title = Buy.objects.all()
    #q = len(title)
    
    booksToBuy = Buy.objects.all()
    k = len(booksToBuy)
    
    if request.method == 'POST':
        k = ContactForm(request.POST)
        if k .is_valid(): 
            #process form
        
            k = Buy(Title = k.cleaned_data['Book'], 
                      Owner = k.cleaned_data['user'],
                      author = k.cleaned_data['Author'])
            
            k.save()            
            #name = q.cleaned_data['Book'] + q.cleaned_data['Author']
            #subject = q.cleaned_data['subject']
            #return HttpResponse('Validated!!' + subject)
            #return HttpResponse('Validated!!' + name)
            return HttpResponse('your validation was successfull!! %s %s %s' %(k.Title, k.Owner, k.author))


    else:
        k = ContactForm() 
        

    return render_to_response ('buy.html', 
    {'list2':booksToBuy, 'form': k }, context_instance=RequestContext(request))




#   return HttpResponse('buy.html')
#   return render_to_response('buy.html',)
#   return render_to_response('buy.html',
#    {'titles':title})

def salesList(request):
    booksForSale = Sale.objects.all()
    q = len(booksForSale)
    
    if request.method == 'POST':
        q = ContactForm(request.POST)
        if q .is_valid(): 
            #process form
        
            q = Sale(Title = q.cleaned_data['Book'], 
                      Owner = q.cleaned_data['user'],
                      author = q.cleaned_data['Author'])
            
            q.save()            
            #name = q.cleaned_data['Book'] + q.cleaned_data['Author']
            #subject = q.cleaned_data['subject']
            #return HttpResponse('Validated!!' + subject)
            #return HttpResponse('Validated!!' + name)
            return HttpResponse('Thanks for adding!! %s %s %s' % (q.Title, q.Owner, q.author))


    else:
        q = ContactForm() 
        

    return render_to_response ('sale.html', 
    {'list':booksForSale, 'form': q }, context_instance=RequestContext(request))

def search(request):

    ## todo a split search strings into words and use each word
    #words = request.GET['search'].split(' ')
    #kind = words[0]
    #words = words[1:]
    #q = Q(Title__icontains='') # Always true
    #for w in words:
    #    q = q & Q(Title__icontains=w)
    #if kind == 'a':
    #    q = q & Q(Title__icontains='The')
    #else:
    #    q = q & Q(Title__icontains='Pragmatic')
    
    ## a simple way to do Boolean OR
    q=(Q(Title__icontains=request.GET['search'])|
      Q(author__icontains=request.GET['search']))   
    
    bs = courseBook.objects.filter(q)    
    
    ## a simple way to join 2 searches
    #xs = courseBook.objects.filter(author__icontains=request.GET['search'])
    #ys = courseBook.objects.filter(author__icontains=request.GET['search'])
    #bs = list(xs) + list(ys)

    ## todo a normal search
    #bs = courseBook.objects.filter(Title__icontains=request.GET['search'])
    
    return render_to_response ('search.html', {'books': bs},
    context_instance=RequestContext(request))
    #return HttpResponse("Searching for " + request.GET['search'] + ": " + str(bs))

def logoutView(request):
    logout(request)
    #return HttpResponse('Log Out')
    return HttpResponseRedirect(reverse ('home'))

def loginView(request):
    username = request.POST['username']
    password = request.POST['password']
    
    u = authenticate(username=username, password=password)
    if u is not None and u.is_active:
        login(request, u)
        # Return an 'invalid login' error message.
        return HttpResponseRedirect(reverse ('home'))
    return HttpResponse('Go back to homepage and enter your username and password')

    #return HttpResponse(str(r))
    

