from django.urls import path, include
from rest_framework import routers
from invoices.views import InvoiceViewSet
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
