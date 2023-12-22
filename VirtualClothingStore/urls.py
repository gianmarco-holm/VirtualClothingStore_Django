from django.contrib import admin
from django.urls import path
from VirtualClothingStore import views as local_views
from Products import views as productos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', local_views.helloWorld),
    path('sorted/', local_views.sorted),
    path('hi/<str:name>/<int:age>/', local_views.sayHi),
    path('products/', productos_views.listarProductos)
]
