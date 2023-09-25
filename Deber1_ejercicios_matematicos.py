'''CADA EJERCICIO DEBE EJECUTARSE INDIVIDUALMENTE'''

personas=4
rebanada_persona=2
pizza_comprada=5
rebanadaxpizza=8
rebanadascomidas=personas*rebanada_persona
rebanadas_disponibles=pizza_comprada*rebanadaxpizza
rebanadas_sobrantes=rebanadas_disponibles-rebanadascomidas
print('El numero de rebanadas sobrantes es:',rebanadas_sobrantes)

'''EJERCICIO 2'''
Camisas=8
preciocamisa=20
descuento=0.2
compra=4
costosindescuento=compra*preciocamisa
montodescuento=costosindescuento*descuento
total=costosindescuento-montodescuento
print('El costo total con descuento es:',total)

'''EJERCICIO 3'''
distancia=800
tiempo=4
velocidad=distancia/tiempo
print('La velocidad del avion es:',velocidad)

'''EJERCICIO 4'''

camisetas=15
chaquetas=50
descuento=0.1 
compra1=((camisetas)*2+chaquetas)
stotal=compra1*descuento 
total=compra1-stotal
print('El costo con descuento es:',total)

'''EJERCICIO 5'''
paginasxdia=500/5
print('El numero de paginas a leer son:',paginasxdia)

'''EJERCICIO 6'''

costo_celular=250
tiempo=12
pagos=costo_celular/tiempo
print('El precio mensual a pagar es:',pagos)


'''EJERCICIO 7'''

costoviaje=50
descuento=0.15
estudiantes=3
pago=costoviaje*estudiantes
pagodescuento=(pago*descuento)
total=pago-pagodescuento
print('El costo del viaje seria de',total,'Para los 3 estudiantes')


'''EJERCICIO 8'''

pesofideos=500
rinde=5
porciones=3
gramosxpersona=100
gramos_a_cocinar=(((rinde*porciones)/pesofideos))*gramosxpersona
print('Los gramos a cocinar son',gramos_a_cocinar*100,'por persona')

'''EJERCICIO 9'''

unidades_en_paquete=24
personas=6
corresponden=unidades_en_paquete/personas
print('La cantidad de galletas que les corresponde a cada persona es de:',corresponden)

'''EJERCICIO 10'''
dinero_inicial=200
deposito_mensual=50
meses=12
dinero=(deposito_mensual*meses)+dinero_inicial
print('El dinero despues de 12 meses es',dinero)