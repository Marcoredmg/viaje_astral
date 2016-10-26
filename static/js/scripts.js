function CalcularDescuento(){
	precio_unitario = parseInt(document.getElementById('tbPrecio').value);
	descuento = .15;
	num_personas = document.getElementById('selectPersonas').value;
	

	if(num_personas == 3){
		precio_final = precio_unitario - (precio_unitario * descuento);
		precioFinal.textContent = "$" + precio_final + " USD c/u"
	}

}