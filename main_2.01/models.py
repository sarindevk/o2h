from django.db import models

class Product(models.Model):

	KG				=	'KG'
	GM				=	'gm'
	
	UNITS = (
		(KG, 'KG'),
		(GM, 'gm'),
	)
	
	
	name 		=	models.CharField(max_length=40, primary_key=True)	
	#name		= models.OneToOneField(Product_bucket,on_delete=models.CASCADE,primary_key=True)
	desc 		= 	models.CharField(max_length=140)
#	price 	= 	models.DecimalField(max_digits=10, decimal_places=2)
	unit		=	models.CharField(max_length=2,choices=UNITS,default=KG)
	image		=	models.ImageField(upload_to='prod_images/')
#	avlb_qty	=	models.DecimalField(max_digits=10, decimal_places=2)
	writeup	=	models.TextField(blank=True, null=True)
	source	=	models.TextField(blank=True, null=True)
	
	def __str__(self):
		return str(self.name)		
	
	class Meta:
		db_table = 'master_products' 
#		unique_together = ('name','category')	

class Product_bucket(models.Model):

# Declaring constants 
	BASE		=	'Base'	
	CURRY		=	'Curry'
	THORAN	=	'Thooran'

	BUCKETS = (
	 (BASE,'Base'),
	 (CURRY,'Curry'),
	 (THORAN,'Thooran'),
	)
	
	name 		= 	models.ForeignKey(Product)	
	bucket	=	models.CharField(max_length=40,choices=BUCKETS,default=BASE)	
	
	def __str__(self):
		return str(self.name)	
	
	
	class Meta:
		db_table = 'product_bucket'
		unique_together = ('name','bucket')	 
	
	
class Product_category(models.Model):

# Declaring constants 
	ORGANIC		=	'Organic'	
	HOMEGROWN	=	'Home Grown'
	OOTYSPECIAL	=	'Ooty Special'

	CATEGORIES = (
	 (HOMEGROWN,'Home Grown'),
	 (OOTYSPECIAL,'Ooty Special'),
	 (ORGANIC,'Organic'),
	)
	
	name 		=	models.ForeignKey(Product)		
	category	=	models.CharField(max_length=40,choices=CATEGORIES,default=ORGANIC)	
	price 	= 	models.DecimalField(max_digits=10, decimal_places=2)
	min_qty	=	models.DecimalField(max_digits=2,decimal_places=2)
	avlb_qty	=	models.DecimalField(max_digits=10, decimal_places=2)	
	image		=	models.ImageField(upload_to='prod_images/',null=True,blank=True)
	writeup	=	models.TextField(blank=True, null=True)
	source	=	models.TextField(blank=True, null=True)
	
	def __str__(self):
		return str(self.name)		
	
	
	class Meta:
		db_table = 'product_category' 
		unique_together = ('name','category')	