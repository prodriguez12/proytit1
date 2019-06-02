"""proytit1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from input.views import input_new_view, input_single_view, input_list_view
from output.views import output_single_view
from pages.views import home_view, apply_view

urlpatterns = [
	path('', home_view , name='home'),
    path('admin/', admin.site.urls),
    path('input/<int:input_id>/', input_single_view, name = 'input'),
    path('inputs/', input_list_view, name = 'inputs'),
    path('input/new', input_new_view, name = 'inputnew'),
    path('output/<int:output_id>/', output_single_view, name = 'output'),
    path('apply/<int:input_id>', apply_view, name='process'),
]
