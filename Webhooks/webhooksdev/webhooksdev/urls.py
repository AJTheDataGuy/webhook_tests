from webhooks.views import webhook_reciever

"""
URL configuration for webhooksdev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook/', webhook_reciever,name='webhook'),
    path('webhook_job_created/', webhook_reciever,name='webhook'),
    path('webhook_driver_assigned/', webhook_reciever,name='webhook'),
    path('webhook_driver_unassigned/', webhook_reciever,name='webhook'),
    path('webhook_driver_arrived_pickup/', webhook_reciever,name='webhook'),
    path('webhook_driver_picked_up/', webhook_reciever,name='webhook'),
    path('webhook_driver_arrived_drop_off/', webhook_reciever,name='webhook'),
    path('webhook_job_delivered/', webhook_reciever,name='webhook'),
    path('webhook_job_canceled/', webhook_reciever,name='webhook'),
    path('webhook_job_details_updated/', webhook_reciever,name='webhook'),
    path('webhook_job_damaged_freight/', webhook_reciever,name='webhook'),
    path('webhook_job_futile_pickup/', webhook_reciever,name='webhook'),
    path('webhook_driver_breakdown/', webhook_reciever,name='webhook'),
    path('webhook_driver_breakdown_cleared/', webhook_reciever,name='webhook'),
    path('webhook_trip_sheet_created/', webhook_reciever,name='webhook'),
    path('webhook_trip_sheet_updated/', webhook_reciever,name='webhook'),
    path('webhook_driver_breakdown/', webhook_reciever,name='webhook'),
    path('webhook_driver_breakdown_cleared/', webhook_reciever,name='webhook'),
    path('webhook_trip_sheet_created/', webhook_reciever,name='webhook'),
    path('webhook_trip_sheet_updated/', webhook_reciever,name='webhook'),
]
