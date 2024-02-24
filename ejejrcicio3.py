def descuento(producto):


  if producto > 500:
     descuento = producto * 0.10
     print(f"El descuento del producto es {descuento}")
     return 0
  else:
     descuento = producto * 0
     print(f"El descuento del producto es {descuento}")
     return 0
producto = int(input("Ingrese cual es el precio del producto: "))
descuento(producto)
      