import bpy

scn = bpy.context.scene

def seleccionar_por_nombre(nombre):
    bpy.ops.object.select_all(action='DESELECT')
    for ob in bpy.data.objects:
        if ob.name.find(nombre) >= 0:
            ob.select = True
            scn.objects.active = bpy.data.objects[str(ob.name)]

def crar_nuevo_uvmap(ac, real):
    if ac >= real:
        bpy.ops.mesh.uv_texture_add()
        cuantos=len(ob.data.uv_textures)-1
        ob.data.uv_textures[cuantos].name = "nuevo_mapa_uv"
        ob.data.uv_textures[cuantos].active = True
        ob.data.uv_textures[cuantos].active_render = True    

def uv_chekeador(ob, real):
    ac = 0
    seleccionar_por_nombre(ob.name)
    # si no tiene uvs se las creamos y si tene las backupeamos y creamos nuevas:
    if len(ob.data.uv_layers) == 0:
        crar_nuevo_uvmap(ac, real)
    else:
        for uvi, uvs in enumerate(ob.data.uv_layers):
            # -1 no lo contiene, 0 si lo contiene:
            if uvs.name.find("backup_") != 0:
                # lo seleccionamos y lo renombramos
                #bpy.context.object.data.active_index = 0
                ob.data.uv_textures[uvi].active = True
                uvs.name = str("backup_") + str(uvs.name)
        if "nuevo_mapa_uv" not in ob.data.uv_textures:
            # y agregamos el nuevo mapa:    
            crar_nuevo_uvmap(ac, real)
    ac += 1

# cuantos materiales tiene (sin contar con 0):
total_mats = len(bpy.context.object.material_slots)
objetos = bpy.context.selected_objects
for a, ob in enumerate(objetos):
    #print(a)
    #print(ob)
    real = a
    uv_chekeador(ob, real)
    #creamos una nueva imagen por objeto donde ira el bakeo:
    #bpy.data.window_managers["WinMan"].(null) = "nuevo_map"
    nombre='nuevo_mapa_para_bakeo_0' + str(a)
    bpy.ops.image.new(name=nombre)
    for i in range(total_mats):
        if 'img_texture_automatic' not in bpy.context.object.material_slots[i].material.node_tree.nodes:
            bpy.context.object.material_slots[i].material.node_tree.nodes.new("ShaderNodeTexImage")
            bpy.context.object.material_slots[i].material.node_tree.nodes['Image Texture'].image = bpy.data.images[nombre]
            bpy.context.object.material_slots[i].material.node_tree.nodes['Image Texture'].name = 'img_texture_automatic'

    #bpy.ops.node.add_node(type="ShaderNodeTexImage", use_transform=False)
