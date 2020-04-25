from django.urls import path
from api.views import views
from api.views.viewsCBF import CategoryList,OrderList

urlpatterns = [
    # path('login/', obtain_jwt_token),
    path('category/', CategoryList.as_view()),
    path('products/', views.products_list),
    path('products/<int:product_id>', views.product_detail),
    path('products/<str:ctg>/', views.by_category),
    path('products/<str:ctg>/<int:product_id>/', views.by_category_detail),
    path('categories/', views.CategoryList.as_view()),
    path('orders/',OrderList.as_view())
]