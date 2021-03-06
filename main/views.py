from django.shortcuts import render
from main.models import Product, Product_category, Product_bucket
from django.http import HttpResponse
from django.db.models import Prefetch


# Create your views here.

def index (request):
	
	#setting default bucket
	bucket = 'Curry'	
	
	if request.method=='GET':
		bucket 	= request.GET.get('bucket')

	
	#set the correct box active
	curry 	= 	''
	base		=	''
	thooran	=	''	
	
	
	if bucket == 'Curry':
		curry='active'
	elif bucket == 'Base':
		base='active'
	elif bucket == 'Thooran':
		thooran='active'	
	

	bucketset 	=  Product_bucket.objects.filter(bucket=bucket).all()
	productset	=	Product.objects.filter(name__in=[bucket.name for bucket in bucketset]).all()	
	categoryset	=	Product_category.objects.filter(name__in=[product.name for product in productset]).all()
		
#	productset	=	Product.objects.filter(name__in=[bucket.name for bucket in bucketset]).all()
#	categoryset	=	Product_category.objects.filter(name__in=[product.name for product in productset], category=category).all()
	
	print(bucketset)
	print(categoryset)
	print(productset)
	
	
	
	
#	if request.POST.get('addtocart') != None:
#		print(request.POST.get('qty'))
#		print("Add qty ",request.POST.get('product'))
#		add_to_cart(request, request.POST.get('product'), request.POST.get('qty'))
	
	if request.POST.get('session') != None:
		view_cart(request)

	if request.POST.get('refresh') != None:
		print("Refreshing ")		
		clear_cart(request)
	
	return render(request, 'main/product.html',{
															  'products':productset, 
															  'categories':categoryset,
															  'carousel':'display:none',
															  'base':base,
															  'curry':curry,
															  'thooran':thooran,																  
																		  
															  })


def add_to_cart(request):
	

	if request.method == 'POST':
		print(request.POST)
#		print("Button pressed", request.POST['action'])
		product = request.POST['product']
		qty	  = request.POST['qty']	
	else:
		return HttpResponse({})	
	
	cart = request.session.get('cart', {})	
	
	
	print('Product added :', product)
	if(product not in cart):
		cart[product] = qty
	else:
		cart[product] = int(cart[product]) + int(qty)

	request.session['cart'] = cart
	
	return HttpResponse({})
  
    
def view_cart(request):
    cart = request.session.get('cart', {})
    print("Cart : ", cart)
    
    return HttpResponse({})
    
    
    
def clear_cart(request):
	cart = {}
	request.session['cart'] = cart
	
	
	return HttpResponse({})