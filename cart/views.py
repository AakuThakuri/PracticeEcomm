from django.shortcuts import render
from home.views import *
from .models import *

# Create your views here.
class CartView(BaseView):
	def get(self, request):
		self.views['carts'] = Cart.objects.filter()
		return render(request , 'wishlist.html',self.views)

def cart(request,slug):
	if Cart.objects.filter(slug = slug).exists():
		quantity = Cart.objects.get(slug = slug).quantity
		quantity = quantity +1
		if Item.objects.filter(slug = slug).exists():
			price = Item.objects.get(slug = slug).price
			discounted_price = Item.objects.get(slug = slug).discounted_price
			if discounted_price >0:
				total = discounted_price * quantity
			else:
				total = price * quantity
				
		Cart.objects.filter(slug = slug).update(quantity = quantity , total = total)

	else:
		price = Item.objects.get(slug = slug).price
		discounted_price = Item.objects.get(slug = slug).discounted_price
		if discounted_price >0:
			total = discounted_price
		else:
			total = price
		username = request.user			
		
		
			
		data = Cart.objects.create(
			user = username,
			slug = slug,
			items = Item.objects.filter(slug = slug)[0],
			total = total
			)
		data.save()
	return redirect('/cart/')	


def removecart(request,slug):
	if Cart.objects.filter(slug = slug,user = request.user,checkout =False).exists():
		quantity = Cart.objects.get(slug = slug).quantity
		price = Item.objects.get(slug = slug).price
		discounted_price = Item.objects.get(slug = slug).discounted_price
			
		if quantity >1:
			quantity = quantity -1
			if discounted_price >0:
				total = discounted_price * quantity
			else:
				total = price * quantity
			Cart.objects.filter(slug = slug,user = request.user,checkout =False).update(quantity = quantity, total = total)	
		    
		else:
			pass
	return redirect('/cart/')

def deletecart(request,slug):
	if Cart.objects.filter(slug = slug,user = request.user,checkout =False).exists():
		
		Cart.objects.filter(slug = slug,user = request.user,checkout =False).delete()
	return redirect('/cart/')



				