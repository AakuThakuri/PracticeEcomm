from django.shortcuts import render,redirect

from django.views.generic import View
from .models import * 
from django.contrib.auth.models import User
from django.contrib import messages
from cart.models import *
# Create your views here.
class BaseView(View):
	views = {}


class HomeView(BaseView):
	def get(self, request):
		if request.user.username:
			self.views['no_order'] = Cart.objects.filter(user = request.user, checkout =False).count()
		print(self.views['no_order'])
		
		self.views['items'] = Item.objects.all()
		self.views['categories'] = Category.objects.all()
		self.views['subcategories'] = Subcategory.objects.all()
		self.views['sliders'] = Slider.objects.all()
			  
 
		return render(request, 'index.html', self.views)

class SubCategory(BaseView):
	def get(self, request, slug):
		ids = Subcategory.objects.get(slug = slug).id
		self.views['subcat_items'] = Item.objects.filter(subcategory_id = ids)
		

		return render(request,'subcategory.html',self.views)

class ProductView(BaseView):
	def get(self, request,slug):
		self.views['product_details'] = Item.objects.filter(slug = slug)
		self.views['hot_product'] = Item.objects.filter(labels = 'hot')
		return render(request,'single.html' , self.views )

class SearchView(BaseView):
	def get(self, request):
		query = request.GET.get('query', None)
		if not query:
			return redirect('/')
		self.views['search_query']	= Item.objects.filter(title__icontains = query)
		return render(request,'search.html' ,self.views)


def signup(request):
	if request.method == "POST":
		username = request.POST['username']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']
		if password == cpassword:
			if User.objects.filter(username=username).exists():
				messages.error(request,'The username is already exist')
				return redirect('/signup')

			elif User.objects.filter(email = email).exists():
				messages.error(request,'The email is already exist')
				return redirect('/signup')

			else:
				user = User.objects.create_user(
					username = username,
					first_name = first_name, 
					last_name = last_name,
					email = email,
					password = password)
				user.save()
				messages.success(request,'You are registred!')
				return redirect('/signup')

				


	return render(request,'register.html')

from django.core.mail import EmailMessage

def contact(request):
	views = {}
	if request.method == "POST":
		name = request.method.POST['name']
		email = request.method.POST['email']
		message = request.method.POST['message']
		data = Contact.objects.create(
			name = name,
			email = email,
			message = message)
		data.save()
		send_email = EmailMessage(
			'Message from Customer'
			f'Hello admin {name} is trying to connect with you. His mail is {email}. His message is {message}.'
			'',
			['']
			)
		send_email.send()
		message.success(request ,'email has sent')
	views['infos'] = Information.objects.all()	

	return render(request,'contact.html' , views)



	# .........API........


from rest_framework import routers, serializers, viewsets

from .serializer import *

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer	

from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend

class ItemListView(generics.ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	filter_backends = [filters.SearchFilter, filters.OrderingFilter,DjangoFilterBackend]
	filter_fields = ['category','subcategory','labels','stock']
	ordering_fields = ['id','price','title']
	search_fields = ['title']  



from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView	

class ItemCRUDView(APIView):
	def get_object(self, pk):
		try:
			return Item.objects.get(pk = pk)
		except:
			pass

	def get(self, request , pk, format = None):
		item = self.get_object(pk)
		serializer = ItemSerializer(item)
		return Response(serializer.data)

	def put(self, request, pk, format = None):
		item = self.get_object(pk)
		serializer = ItemSerializer(item, data = request.data)
		if serializer.valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.error ,status = status.HTTP_200_BAD_REQUEST)
		
	def delete(self, request, pk, format = None):
		item = self.get_object(pk)
		item.delete()
		return Response("Data is deleted !",status = status.HTTP_200_OK)

# api_url = 'https://localhost:8000/api_url/item'
# def api_view(request):
# 	response = requests.get(api_url)
# 	records = response.txt
# 	records = json.loads(records)

# 	return render(request,'text.html', {items:records})



			
    
    
    
    