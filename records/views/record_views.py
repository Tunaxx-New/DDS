from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from records.forms import RecordForm
from records.models import Record, Purpose, Category, SubCategory


class RecordListView(ListView):
    model = Record
    template_name = 'records/records-list.html'
    context_object_name = 'records'

    def get_queryset(self):
        qs = super().get_queryset().select_related('purpose', 'category', 'subcategory', 'type')

        purpose_id = self.request.GET.get('purpose')
        category_id = self.request.GET.get('category')
        subcategory_id = self.request.GET.get('subcategory')

        if purpose_id:
            qs = qs.filter(purpose_id=purpose_id)
        if subcategory_id:
            qs = qs.filter(subcategory_id=subcategory_id)
        if category_id:
            qs = qs.filter(category_id=category_id)

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
            },
        })
        context['delete_url_name'] = "records-delete"
        context['update_url_name'] = "records-update"
        return context


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'records/records-form.html'
    success_url = reverse_lazy('records')


class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    template_name = 'records/records-form.html'
    success_url = reverse_lazy('records')


class RecordDeleteView(DeleteView):
    model = Record
    template_name = 'records/item-delete.html'
    success_url = reverse_lazy('records')
    reverse_lazy_name = 'records'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the URL pattern name (not the URL string)
        context['reverse_lazy_name'] = self.reverse_lazy_name
        return context
