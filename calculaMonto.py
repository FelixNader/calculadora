import denom
#denom contiene lista de denominaciones
monto=134
#monto a separar en denominaciones
for d in denom.den:
#itera la denominacion
    alcanza=monto/d
    #Calcula si alcanza billetes de la denominacion
    if alcanza * d > 0:
        print('monto alcanza ' , alcanza , 'billetes de ' ,d)
        valor=alcanza*d
        print(monto, '-', valor)
        '''si el valor monetario de la denominacion rebasa el monto
        actual de la denominacion, imprime el valor actual del monto
         y el valor a deducir del mismo'''
    if  alcanza * d  >= d:
        monto=monto-(alcanza*d)
        print(monto)
        '''deduce el monto pendiente lo asigna como nuevo
        monto el imprime el nuevo monto a deducir'''
