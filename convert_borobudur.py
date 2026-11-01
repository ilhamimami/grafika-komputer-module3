import trimesh
from pathlib import Path

source = Path("borobudur_temple/scene.gltf")
output = Path("data/borobudur.obj")

scene = trimesh.load(source, force="scene")
mesh = scene.dump(concatenate=True)

output.parent.mkdir(parents=True, exist_ok=True)
mesh.export(output)

print("Konversi berhasil!")
print("Vertices:", len(mesh.vertices))
print("Triangles:", len(mesh.faces))
print("UV:", mesh.visual.uv is not None)
print("Output:", output)
