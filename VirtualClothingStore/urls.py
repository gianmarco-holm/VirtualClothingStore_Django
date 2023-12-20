from django.contrib import admin
from django.urls import path
from VirtualClothingStore import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', views.helloWorld),
    path('hi/', views.hi),
]
