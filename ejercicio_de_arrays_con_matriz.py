import bpy
bpy.ops.object.select_all(action='SELECT') # selecciono todo
bpy.ops.object.delete(use_global=False) # lo elimino
bpy.ops.mesh.primitive_cube_add() # agregamos un cubo
bpy.data.objects["Cube"].name='Cubo' # cambiamos el nombre por defecto Cube por Cubo

# creamos una lista que contiene 3 listas con 3 numeros 0 dentro de cada una:
def create_matrix(n, m):
    return [[0 for j in range(n)] for i in range(m)]

matriz = create_matrix(3,3)
# ya tenemos nuestra lista=[ [0,0,0],[0,0,0],[0,0,0] ]
# ahora seteo a mano los valores de offset:
matriz[0] = [2,0,0]
matriz[1] = [0,2,0]
matriz[2] = [0,0,2]

#settings:
veces = 3
ob = "Cubo" 
repeticiones_cubo = 5

# primero creo los 3 arrays y seteo los valores compartidos:
def creadordearrays(ob,veces,bloques):
    for i in range(veces):
        bpy.ops.object.modifier_add(type='ARRAY') # agregamos el modificador ARRAY
        bpy.data.objects[ob].modifiers[i].count=bloques # ponemos el número de cubos

# ejecuto la funcion y le paso los valores de los settings:
creadordearrays(ob,veces,repeticiones_cubo)

# por cada vez que se ejecuta, se ejecuta a un modificador distinto con settings distintos cada uno:
def setteo(ob,cual):
    for i in range(3): #<-- por cada uno de los numeros de slots (a setear) de relative offset displace:
        bpy.data.objects[ob].modifiers[cual].relative_offset_displace[i-1] = matriz[i-1][cual]

# ejecuto el setteo el numero de veces tanto como numero de modificadores tiene:
for i in range(len(bpy.data.objects[ob].modifiers)):
    setteo(ob,i)
