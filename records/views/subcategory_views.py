from .base import GenericModelListView, GenericModelCreateView, GenericModelDeleteView, GenericModelUpdateView


class RecordSubCategoryListView(GenericModelListView):
    model_name = 'SubCategory'
    item_name = 'Подкатегория'


class RecordSubCategoryCreateView(GenericModelCreateView):
    model_name = 'SubCategory'
    item_name = 'Подкатегория'
    reverse_lazy_name = 'subcategories'


class RecordSubCategoryDeleteView(GenericModelDeleteView):
    model_name = 'SubCategory'
    reverse_lazy_name = 'subcategories'


class RecordSubCategoryUpdateView(GenericModelUpdateView):
    model_name = 'SubCategory'
    item_name = 'Подкатегория'
    reverse_lazy_name = 'subcategories'
