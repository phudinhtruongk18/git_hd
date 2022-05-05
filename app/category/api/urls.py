from django.urls import path, include

from .views import CategoryDetail
from .views import CategoryListCreateAPIView


urlpatterns = [
    path('v2/', include('category.api.routers'), name='test_api'),
    # API 
    path('single/<int:pk>/', CategoryDetail.as_view(), name='test_api_sing'),
    path('list/', CategoryListCreateAPIView.as_view(), name='test_api'),
    # path('api/', CategoryList.as_view(), name='api_list_category'),
    # path('api/category/<str:pk>/', CategoryDetail.as_view(), name='api_detail_category'),
    # path('api/search/', CategoryListDetailfilter.as_view(), name='api_search_category'),

    # # category Admin URLs
    # path('api/admin/create/', CreateCategory.as_view(), name='api_create_category'),
    # path('api/admin/edit/categorydetail/<int:pk>/', AdminCategoryDetail.as_view(), name='api_admindetail_category'),
    # path('api/admin/edit/<int:pk>/', EditCategory.as_view(), name='api_edit_category'),
    # path('api/admin/delete/<int:pk>/', DeleteCategory.as_view(), name='api_delete_category'),
]