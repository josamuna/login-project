from loginsystem.views import LoginViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', LoginViewset, basename='login')
urlpatterns = router.urls

# from django.urls import path
# from loginsystem.views import (
#     LoginListView, 
#     LoginDetailView, 
#     LoginCreateView, 
#     LoginUpdateView, 
#     LoginDeleteView)

# urlpatterns = [
#     path('', LoginListView.as_view()),
#     path('register/', LoginCreateView.as_view()),
#     path('<pk>/', LoginDetailView.as_view()),
#     path('<pk>/update/', LoginUpdateView.as_view()),
#     path('<pk>/delete/', LoginDeleteView.as_view()),
# ]