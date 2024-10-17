from django.urls import path, include 
from rest_framework_simplejwt import views as jwt_views 
from . import views


urlpatterns = [
    path('api/', views.apiOverview, name='api'),
    path('api/items', views.CreateItem.as_view(), name='create_item'),
    path('register/', views.RegisterView.as_view()),
    # path('login/', views.MyTokenObtainPairView.as_view()),
    path("items/<str:pk>", views.UpdateItem.as_view()),
    path("", views.ReadItem.as_view()),
    path("items/<str:pk>", views.DeleteItem.as_view()),
    path("items/<str:pk>", views.ReadItemByID.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'), 
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
] 