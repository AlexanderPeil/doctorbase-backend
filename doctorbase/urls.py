from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from doctorbase_backend.views import DoctorViewSet, PatientViewSet, AppointmentViewSet


router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
