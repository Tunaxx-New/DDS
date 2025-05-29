from .base import GenericModelListView, GenericModelCreateView, GenericModelDeleteView, GenericModelUpdateView


class RecordCategoryListView(GenericModelListView):
    model_name = 'Category'
    item_name = 'Категория'


class RecordCategoryCreateView(GenericModelCreateView):
    model_name = 'Category'
    item_name = 'Категория'
    reverse_lazy_name = 'categories'


class RecordCategoryDeleteView(GenericModelDeleteView):
    model_name = 'Category'
    reverse_lazy_name = 'categories'


class RecordCategoryUpdateView(GenericModelUpdateView):
    model_name = 'Category'
    item_name = 'Категория'
    reverse_lazy_name = 'categories'
