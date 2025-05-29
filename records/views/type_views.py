from .base import GenericModelListView, GenericModelCreateView, GenericModelDeleteView, GenericModelUpdateView


class RecordTypeListView(GenericModelListView):
    model_name = 'Type'
    item_name = 'Тип'


class RecordTypeCreateView(GenericModelCreateView):
    model_name = 'Type'
    item_name = 'Тип'
    reverse_lazy_name = 'types'


class RecordTypeDeleteView(GenericModelDeleteView):
    model_name = 'Type'
    reverse_lazy_name = 'types'


class RecordTypeUpdateView(GenericModelUpdateView):
    model_name = 'Type'
    item_name = 'Тип'
    reverse_lazy_name = 'types'
