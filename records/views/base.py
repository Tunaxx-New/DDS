from django.apps import apps
from django.forms import modelform_factory
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


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
        context['model_name'] = self.model_name
        context['create_url'] = f"{self.model_name.lower()}-create"
        context['delete_url_name'] = f"{self.model_name.lower()}-delete"
        context['update_url_name'] = f"{self.model_name.lower()}-update"
        return context


class GenericModelCreateView(CreateView):
    template_name = 'records/item-form.html'
    context_object_name = 'items'
    model_name = None
    item_name = None
    reverse_lazy_name = None

    def get_queryset(self):
        model = apps.get_model('records', self.model_name)
        return model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_name'] = self.item_name
        return context

    def get_model(self):
        return apps.get_model('records', self.model_name)

    def get_success_url(self):
        return reverse_lazy(self.reverse_lazy_name)

    def get_form_class(self):
        from django.forms import modelform_factory
        return modelform_factory(self.get_model(), fields='__all__')


class GenericModelDeleteView(DeleteView):
    template_name = 'records/item-delete.html'
    model_name = None
    reverse_lazy_name = None

    def get_object(self, queryset=None):
        model = apps.get_model('records', self.model_name)
        return model.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reverse_lazy_name'] = self.reverse_lazy_name
        return context

    def get_success_url(self):
        return reverse_lazy(self.reverse_lazy_name)


class GenericModelUpdateView(UpdateView):
    template_name = 'records/item-form.html'
    model_name = None
    item_name = None
    reverse_lazy_name = None

    def get_object(self, queryset=None):
        model = apps.get_model('records', self.model_name)
        return model.objects.get(pk=self.kwargs['pk'])

    def get_form_class(self):
        model = apps.get_model('records', self.model_name)
        return modelform_factory(model, fields='__all__')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_name'] = self.item_name
        return context

    def get_success_url(self):
        return reverse_lazy(self.reverse_lazy_name)
