# Django
from django.shortcuts import render
from faker import Faker

fake = Faker()

def generate():
    limit = 20
    categorias = ['Hombre', 'Mujer', 'Niños']
    tallas = ['S', 'M', 'L', 'XL']
    productos = []

    for _ in range(limit):
        producto = {
            'idProducto': fake.uuid4(),
            'nombreProducto': fake.company(),
            'precioProducto': fake.random_int(min=10, max=100),
            'descripcionProducto': fake.text(),
            'stockProducto': fake.random_int(min=10, max=100),
            'imagenProducto': fake.image_url(width=640, height=480),
            'categoriaProducto': fake.random_element(categorias),
            'colorProducto': fake.color_name(),
            'tallaProducto': fake.random_element(tallas),
            'fechaCreacionProducto': fake.date_time_this_decade().strftime('%b - %dth, %Y %H:%M hrs')
        }
        productos.append(producto)

    return productos

def listarProductos(request):
  productos = generate()
  return render(request,'catalogo.html', {'productos': productos})

# # Django
# from django.http import HttpResponse

# # Utilities
# from faker import Faker

# fake = Faker()

# def generate():
#     limit = 20
#     categorias = ['Hombre', 'Mujer', 'Niños']
#     tallas = ['S', 'M', 'L', 'XL']
#     productos = []

#     for _ in range(limit):
#         producto = {
#             'idProducto': fake.uuid4(),
#             'nombreProducto': fake.company(),
#             'precioProducto': fake.random_int(min=10, max=100),
#             'descripcionProducto': fake.text(),
#             'stockProducto': fake.random_int(min=10, max=100),
#             'imagenProducto': fake.image_url(width=640, height=480),
#             'categoriaProducto': fake.random_element(categorias),
#             'colorProducto': fake.color_name(),
#             'tallaProducto': fake.random_element(tallas),
#             'fechaCreacionProducto': fake.date_time_this_decade().strftime('%b - %dth, %Y %H:%M hrs')
#         }
#         productos.append(producto)

#     return productos

# def listarProductos(request):
#     contenido = []
#     productos = generate()

#     for producto in productos:
#         contenido.append(
#             f"<p><strong>{producto['nombreProducto']}</strong></p>"
#             f"<p><small>{producto['descripcionProducto']}</small></p>"
#             f"<figure><img src='{producto['imagenProducto']}' style='height:100px'/></figure>"
#         )

#     return HttpResponse("<br>".join(contenido))