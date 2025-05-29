from .base import GenericModelListView, GenericModelCreateView, GenericModelDeleteView, GenericModelUpdateView


class RecordPurposeListView(GenericModelListView):
    model_name = 'Purpose'
    item_name = 'Статус'


class RecordPurposeCreateView(GenericModelCreateView):
    model_name = 'Purpose'
    item_name = 'Статус'
    reverse_lazy_name = 'purposes'


class RecordPurposeDeleteView(GenericModelDeleteView):
    model_name = 'Purpose'
    reverse_lazy_name = 'purposes'


class RecordPurposeUpdateView(GenericModelUpdateView):
    model_name = 'Purpose'
    item_name = 'Статус'
    reverse_lazy_name = 'purposes'
