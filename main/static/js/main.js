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




