from django.urls import path
from api.views import views
from api.views.viewsCBF import CategoryList, OrderList,UserViewSet
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken.views import ObtainAuthToken



router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # path('login/', obtain_jwt_token),
    path('category/', CategoryList.as_view()),
    path('products/', views.products_list, name="products"),
    path('products/<int:product_id>/', views.product_detail),
    path('products/<str:ctg>/', views.by_category),
    path('products/<str:ctg>/<int:product_id>/', views.by_category_detail),
    path('categories/', views.CategoryList.as_view()),
    path('orders/', OrderList.as_view()),
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('users/<str:name>/', views.getUserByName),
    path('users/',UserViewSet.as_view()),
    path('auth/',ObtainAuthToken.as_view())


]