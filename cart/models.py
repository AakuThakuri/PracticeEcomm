from django.db import models
from django.conf import settings
from home.models import *
# Create your models here.
class Cart(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
	slug = models.CharField(max_length = 300)
	items = models.ForeignKey(Item, on_delete = models.CASCADE)
	quantity = models.IntegerField(default = 1)
	checkout = models.BooleanField(default = False)
	total = models.IntegerField(null = True)

	def __str__(self):
		return self.user.username

	def get_remove_cart_url(self):
		return reverse('cart:remove_cart' , kwargs = {'slug':self.slug})

	def get_delete_cart_url(self):
		return reverse('cart:delete_cart' , kwargs = {'slug':self.slug})		

    

    	
