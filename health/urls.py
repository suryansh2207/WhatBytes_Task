from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    PatientViewSet,
    DoctorViewSet,
    PatientDoctorMappingViewSet,
    get_doctors_for_patient
)

# Create a router for our ViewSets
router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'mappings', PatientDoctorMappingViewSet, basename='mapping')

urlpatterns = [
    # Register view - kept at root level to match test expectations
    path('register/', RegisterView.as_view({'post': 'create'}), name='register'),
    
    # Login endpoints
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    
    # Special endpoint for getting all doctors for a specific patient
    path('patient/<int:patient_id>/doctors/', get_doctors_for_patient, name='get_doctors_for_patient'),
    
    # Include router URLs
    path('', include(router.urls)),
]