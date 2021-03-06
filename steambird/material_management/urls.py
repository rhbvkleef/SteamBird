from django.urls import path

from .views import AddMaterialView, ISBNLookupView, ISBNView, ISBNDetailView, DOIDetailView, \
    ISBNSearchApiView, DOISearchApiView, OtherDetailView

# pylint: disable=invalid-name
app_name = 'material_management'

# pylint: disable=invalid-name
urlpatterns = [
    path('isbn/search/<str:isbn>', ISBNLookupView.as_view(), name='isbnlookup'),
    path('isbn', ISBNView.as_view(), name='isbn'),
    path('isbn/<str:isbn>', ISBNDetailView.as_view(), name='isbndetail'),
    path('doi/<str:doi>', DOIDetailView.as_view(), name='articledetail'),
    path('other/<int:pk>', OtherDetailView.as_view(), name='otherdetail'),


    path('api/isbn/search', ISBNSearchApiView.as_view(), name='isbn.search'),
    path('api/doi/search', DOISearchApiView.as_view(), name='doi.search'),

    path('material/new', AddMaterialView.as_view(), name='material.create'),
]
