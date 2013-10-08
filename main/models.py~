# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# MVC = Model, View, Controller
# Models represent the data objects in the system.

#class Book(models.Model):
#    title = models.CharField(max_length=100)
#    ISBN = models.CharField(max_length=100)
#    Owner = models.ForeignKey(User)
#    posted_at = models.DateTimeField(auto_now_add=True)
       
#    def __unicode__(self):
#        return self.title + ' ISBN ' + str(self.ISBN) 


class BookClub(models.Model):
    
    RATING_OF_BOOK= (
       (u'N', u'New'),
       (u'G', u'Used'),
    )

    Title = models.CharField(max_length=100)
    body = models.TextField()
    rating = models.CharField(max_length=1,choices= RATING_OF_BOOK) 
    posted_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)   

    def __unicode__(self):
        #return render_to_response('buy.html')   
         return self.Title + ' at ' + str(self.posted_at)

      


class courseBook(models.Model):

    Title = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    
    STUDENT_MAJOR=(
    
    ('UN', 'Undergraduate'),
    ('GR', 'Graduate'),

    )
     
    Level = models.CharField(max_length=10,choices= STUDENT_MAJOR)    
  
    def __unicode__(self):
       return self.Title 

class Buy(models.Model):
    Title = models.CharField(max_length=100)
    author = models.CharField(max_length=100) 
    Owner = models.CharField(max_length=100)  
    def __unicode__(self):
        return str(self.Owner) + ' is looking to buy ' +  str(self.Title)


class Sale(models.Model):
    Title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    Owner = models.CharField(max_length=100) 

    def __unicode__(self):
        return str(self.Owner) + ' wants to sell ' +  str(self.Title)

class Wishlist(models.Model):
    Title = models.CharField(max_length=100)
    Comment = models.TextField()
    Condition = models.CharField(max_length=100)
    author = models.CharField(max_length=100) 
    posted_at = models.DateTimeField(auto_now_add=True)

    AVAIL_OF_BOOK= (
       (u'A', u'Available'),
       (u'N', u'Not Available'),
    )
 
    status = models.CharField(max_length=1,choices= AVAIL_OF_BOOK)

    def __unicode__(self):
        return self.Title + ' ' +  str(self.posted_at)


#admin.site.register(Book)
admin.site.register(BookClub)
admin.site.register(courseBook)
admin.site.register(Buy)
admin.site.register(Sale)
admin.site.register(Wishlist)



