//$(document).on('submit','#ADDCART', function (e) {
$("form").on("submit", function (e) {	


	var form = $(this);
//	alert(form.attr('action'));	
	
	e.preventDefault();
	
	
	$.ajax({		
	
		type:'POST',
		
		url:form.attr('action'),
		
		data:form.serialize(),
		
//		data:
//				{
//					product:$('#product').val(),
//					quantity:$('#qty').val(),
//					csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),					
//		},
//		success:function () {alert('This is great');},
//		error:function(){ alert('Exception:'); }
	});

});

function updateQty(num,self){
	
	var domElement = jQuery(self);
	var buttonWrapper = domElement.parent();
	
	var qtyfield = buttonWrapper.find('.qty');
	val = Number(qtyfield.val());
	if(num){
		qtyfield.val(val+1);
	}
	else{
		if(val-1 > 0){
			qtyfield.val(val-1);
		}

	}
	return false;
}

function updateText(type,self) { 
 
 var domElement = jQuery(self);
 var onelevel = domElement.parent(); 
 
 var pricefield = onelevel.find('.prod_price');
	
 
 pricefield.text(domElement.val());

}



/* This is all carousel logi which will trigger the read */
$('#carousel_bucket').bind('slid.bs.carousel', function (e) {
   idx = $("#carousel_bucket .item.active").index();

	cat_idx = 	$("#carousel_category .item.active").index();
	if(cat_idx==0) category="Organic";
	if(cat_idx==1) category="Home Grown";
	if(cat_idx==2) category="Ooty Special";
	
   if(idx==0){
		window.location='/product/?bucket=Curry&category='+category;
   }

	if(idx==1){
		window.location='/product/?bucket=Base&category='+category;
	}   

	if(idx==2){
		window.location='/product/?bucket=Thooran&category='+category;
	}   
   
   
});
$('#carousel_category').bind('slid.bs.carousel', function (e) {
   idx = $("#carousel_category .item.active").index();

	buc_idx = 	$("#carousel_bucket .item.active").index();
	if(buc_idx==0) bucket="Curry";
	if(buc_idx==1) bucket="Base";
	if(buc_idx==2) bucket="Thooran";


   if(idx==0){
		window.location='/product/?bucket='+bucket+'&category=Organic';
   }

	if(idx==1){
		window.location='/product/?bucket='+bucket+'&category=Home Grown';
	}   

	if(idx==2){
		window.location='/product/?bucket='+bucket+'&category=Ooty Special';
	}   
   
   
});

