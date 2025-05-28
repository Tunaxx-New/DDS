from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from records.views import *

urlpatterns = [
    path('purposes/', RecordPurposeListView.as_view(), name='purposes'),
    path('types/', RecordTypeListView.as_view(), name='types'),
    path('categories/', RecordCategoryListView.as_view(), name='categories'),
    path('subcategories/', RecordSubCategoryListView.as_view(), name='subcategories'),
    path('records/create/', RecordCreateView.as_view(), name='records-create'),
    path('', RecordListView.as_view(), name='records'),
]

urlpatterns.extend(
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
