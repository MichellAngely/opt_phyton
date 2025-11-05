#Michell Angely G

#Cantidad de la pizzas del cliente
pizzas=int(input("¿Cuántas pizzas desea?"))

#Precio
precio_pizza= 5

#Precio de envio por pizza
envio_xpizza= 2 * pizzas
total_envio1= (precio_pizza * pizzas) + envio_xpizza

#Precio alzado
envio_alzado= 9
total_envio2= (precio_pizza * pizzas) + envio_alzado

#Muestra:
print("-_-_-El total de su pedido es:-_-_-")
print(f"Pizzas deseadas: {pizzas}")
print(f"Envio por pizza: {total_envio1}$")
print(f"Envio por alzado: {total_envio2}$")

#input relata una oración y espera respuesta
#int interpreta la respuesta por número
#print relata lo interpretado anteriormente escrito