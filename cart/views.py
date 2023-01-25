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
		Cart.objects.filter(slug = slug).update(quantity = quantity)

	else:
		username = request.user
		data = Cart.objects.create(
			user = username,
			slug = slug,
			items = Item.objects.filter(slug = slug)[0]
			)
		data.save()
	return redirect('/cart/')	


def removecart(request,slug):
	if Cart.objects.filter(slug = slug,user = request.user,checkout =False).exists():
		quantity = Cart.objects.get(slug = slug).quantity
		if quantity >1:
			quantity = quantity -1
			Cart.objects.filter(slug = slug,user = request.user,checkout =False).update(quantity = quantity)
		    
		else:
			pass
	return redirect('/cart/')

def deletecart(request,slug):
	if Cart.objects.filter(slug = slug,user = request.user,checkout =False).exists():
		
		Cart.objects.filter(slug = slug,user = request.user,checkout =False).delete()
	return redirect('/cart/')			