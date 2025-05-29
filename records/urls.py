from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from records.views import *

urlpatterns = [
    path('purposes/', RecordPurposeListView.as_view(), name='purposes'),
    path('purposes/create', RecordPurposeCreateView.as_view(), name='purpose-create'),
    path('purposes/delete/<int:pk>/', RecordPurposeDeleteView.as_view(), name='purpose-delete'),
    path('purposes/update/<int:pk>/', RecordPurposeUpdateView.as_view(), name='purpose-update'),

    path('types/', RecordTypeListView.as_view(), name='types'),
    path('types/create', RecordTypeCreateView.as_view(), name='type-create'),
    path('types/delete/<int:pk>/', RecordTypeDeleteView.as_view(), name='type-delete'),
    path('types/update/<int:pk>/', RecordTypeUpdateView.as_view(), name='type-update'),

    path('categories/', RecordCategoryListView.as_view(), name='categories'),
    path('categories/create', RecordCategoryCreateView.as_view(), name='category-create'),
    path('categories/delete/<int:pk>/', RecordCategoryDeleteView.as_view(), name='category-delete'),
    path('categories/update/<int:pk>/', RecordCategoryUpdateView.as_view(), name='category-update'),

    path('subcategories/<int:category_id>', RecordSubCategoryListView.as_view(), name='subcategories'),
    path('subcategories/create/<int:category_id>', RecordSubCategoryCreateView.as_view(), name='subcategory-create'),
    path('subcategories/delete/<int:pk>/', RecordSubCategoryDeleteView.as_view(), name='subcategory-delete'),
    path('subcategories/update/<int:pk>/', RecordSubCategoryUpdateView.as_view(), name='subcategory-update'),
    path('ajax/load-subcategories/', load_subcategories, name='ajax_load_subcategories'),

    path('', RecordListView.as_view(), name='records'),
    path('records/create/', RecordCreateView.as_view(), name='records-create'),
    path('records/delete/<int:pk>/', RecordDeleteView.as_view(), name='records-delete'),
    path('records/update/<int:pk>/', RecordUpdateView.as_view(), name='records-update'),
]

urlpatterns.extend(
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
