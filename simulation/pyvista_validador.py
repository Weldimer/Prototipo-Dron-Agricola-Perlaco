import os
import trimesh

def validar_malla(filepath):
    if not os.path.exists(filepath):
        print(f"Archivo no encontrado: {filepath}")
        return False
    mesh = trimesh.load(filepath)
    print(f"Malla {filepath} estanca: {mesh.is_watertight}")
    return mesh.is_watertight
