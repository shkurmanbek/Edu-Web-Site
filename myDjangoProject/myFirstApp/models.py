from django.db import models

# Create your models here.
class Article(models.Model):
	article_name = models.CharField(max_length = 1000)
	article_text = models.TextField()
	article_date = models.DateTimeField('date published')
	
	def __str__(self):
		return self.article_name
		
class Editor(models.Model):
	editor_name = models.CharField(max_length = 100)
	editor_surname = models.CharField(max_length = 100)
	
	def __str__(self):
		return self.editor_name + " " + self.editor_surname 
		
class User(models.Model):
	user_name = models.CharField(max_length = 100)
	user_surname = models.CharField(max_length = 100)
	user_dob = models.DateTimeField('date of birth')
	
	def __str__(self):
		return self.user_name + " " + self.user_surname

class Comments(models.Model):
	comments_text = models.TextField()

	def __str__(self):
		return self.comments_text

class Ads(models.Model):
	ads_owner = models.CharField(max_length=100)
	ads_content = models.TextField()
	
	def __str__(self):
		return self.ads_content
		
class QuantityOfViews(models.Model):
	number_of_views = models.IntegerField()
	link_to_hidden_ad = models.TextField()
	
	def getNumberOfViews(self):
		return self.number_of_views











