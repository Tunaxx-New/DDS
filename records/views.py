from django.apps import apps
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from records.forms import RecordForm
from records.models import *


class GenericModelListView(ListView):
    template_name = 'records/item-list.html'
    context_object_name = 'items'
    model_name = None
    item_name = None

    def get_queryset(self):
        if not self.model_name:
            raise ValueError("model_name is not set")
        model = apps.get_model('records', self.model_name)
        return model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_name'] = self.item_name
        return context


class RecordPurposeListView(GenericModelListView):
    model_name = 'Purpose'
    item_name = 'Статус'


class RecordTypeListView(GenericModelListView):
    model_name = 'Type'
    item_name = 'Тип'


class RecordCategoryListView(GenericModelListView):
    model_name = 'Category'
    item_name = 'Категория'


class RecordSubCategoryListView(GenericModelListView):
    model_name = 'SubCategory'
    item_name = 'Подкатегория'


class RecordListView(ListView):
    template_name = 'records/records-list.html'
    context_object_name = 'records'
    model = Record

    def get_queryset(self):
        qs = super().get_queryset().select_related('purpose', 'subcategory__category', 'subcategory', 'type')

        purpose_id = self.request.GET.get('purpose')
        category_id = self.request.GET.get('category')
        subcategory_id = self.request.GET.get('subcategory')

        if purpose_id:
            qs = qs.filter(purpose_id=purpose_id)
        if subcategory_id:
            qs = qs.filter(subcategory_id=subcategory_id)
        if category_id:
            qs = qs.filter(subcategory__category_id=category_id)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'purposes': Purpose.objects.all(),
            'categories': Category.objects.all(),
            'subcategories': SubCategory.objects.all(),
            'selected': {
                'purpose': self.request.GET.get('purpose', ''),
                'category': self.request.GET.get('category', ''),
                'subcategory': self.request.GET.get('subcategory', ''),
            }
        })
        return context


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'records/records-create.html'
    success_url = reverse_lazy('records')

    def form_valid(self, form):
        return super().form_valid(form)
