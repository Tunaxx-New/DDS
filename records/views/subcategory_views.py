from django.apps import apps
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse

from .base import GenericModelListView, GenericModelCreateView, GenericModelDeleteView, GenericModelUpdateView
from ..models import Category


class RecordSubCategoryListView(GenericModelListView):
    model_name = 'SubCategory'
    item_name = 'Подкатегория'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')

        context['item_name'] = self.item_name
        context['create_url'] = f"{self.model_name.lower()}-create"
        context['delete_url_name'] = f"{self.model_name.lower()}-delete"
        context['update_url_name'] = f"{self.model_name.lower()}-update"

        if category_id:
            category_model = apps.get_model('records', 'Category')
            context['category'] = category_model.objects.filter(pk=category_id).first()

        return context



class RecordSubCategoryCreateView(GenericModelCreateView):
    model_name = 'SubCategory'
    item_name = 'Подкатегория'
    reverse_lazy_name = 'subcategories'

    def dispatch(self, request, *args, **kwargs):
        # Grab the parent category
        self.category = get_object_or_404(Category, pk=self.kwargs['category_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.category = self.category
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['item_name'] = self.item_name
        return context

    def get_success_url(self):
        return reverse_lazy(self.reverse_lazy_name, kwargs={'category_id': self.category.id})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['category'].initial = self.category
        form.fields['category'].disabled = True
        return form


class RecordSubCategoryDeleteView(GenericModelDeleteView):
    model_name = 'SubCategory'
    item_name = 'Подкатегория'
    reverse_lazy_name = 'subcategories'

    def dispatch(self, request, *args, **kwargs):
        self.category = get_object_or_404(Category, pk=self.kwargs['category_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['item_name'] = self.item_name
        return context

    def get_success_url(self):
        return reverse_lazy(self.reverse_lazy_name, kwargs={'category_id': self.category.id})


class RecordSubCategoryUpdateView(GenericModelUpdateView):
    model_name = 'SubCategory'
    item_name = 'Подкатегория'
    reverse_lazy_name = 'subcategories'

    def dispatch(self, request, *args, **kwargs):
        # Grab the parent category
        self.category = get_object_or_404(Category, pk=self.kwargs['category_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.category = self.category
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['item_name'] = self.item_name
        return context

    def get_success_url(self):
        return reverse_lazy(self.reverse_lazy_name, kwargs={'category_id': self.category.id})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['category'].initial = self.category
        form.fields['category'].disabled = True
        return form
