import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView

from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.customer.views import ListCustomerViewJson
from apps.item.forms import AddItemForm, CSVUploadForm
from apps.item.models import Item
import pandas as pd
from pandas.errors import EmptyDataError

def mukesh(request):
    return HttpResponse('hello world')

class CreateItem(CreateView):
    model = Item
    form_class = AddItemForm
    template_name = 'item/form.html'
    success_url = reverse_lazy('admin-item-list')


    def form_valid(self, form):
        user = form.save(commit=False)  # Don't save to the database yet
        user.user_type = 'customer'
        user.save()  # Save the user to the database
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form = CreateCustomerForm(request.POST)
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

class ListItemView(AdminRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'item/list.html'

class ListItemViewJson(AdminRequiredMixin, AjayDatatableView):
    model = Item
    columns = ['item_name', 'sku', 'UPC_number', 'Price', 'Description','image','actions']
    exclude_from_search_columns = ['actions']
    # extra_search_columns = ['']

    def get_initial_queryset(self):
        return self.model.objects.all()

    def render_column(self, row, column):
        if column == 'is_active':
            if row.is_active:
                return '<span class="badge badge-success">Active</span>'
            else:
                return '<span class="badge badge-danger">Inactive</span>'
        if column == 'image':
            return f'<img src="{row.image}" height=50px alt="Sample Image">'

        if column == 'actions':
            # detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
            #     reverse('admin-user-detail', kwargs={'pk': row.pk}))
            edit_action = '<a href={} role="button" class="btn btn-warning btn-xs mr-1 text-white">Edit</a>'.format(
                reverse('admin-user-edit', kwargs={'pk': row.pk}))
            delete_action = '<a href="javascript:;" class="remove_record btn btn-danger btn-xs" data-url={} role="button">Delete</a>'.format(
                reverse('admin-user-delete', kwargs={'pk': row.pk}))
            return edit_action + delete_action
        else:
            return super(ListItemViewJson, self).render_column(row, column)





def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            file_data = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(file_data)
            print(reader)
            headers = reader.fieldnames
            print(f"CSV Headers: {headers}")
            for row in reader:
               try:
                   Item.objects.create(
                       item_name=row['Item_name'],
                       sku=row['SKU'],
                       UPC_number=row['UPC_number'],
                       Price=row['Price'],
                       Description=row['Description'],
                       image=row['image'],
                   )
               except Exception as e:
                   print(f'Error inserting in Row{e}')
        return render(request, 'item/displayCSV.html')
    else:
        form = CSVUploadForm()
    return render(request, 'item/csv.html', {'form': form})
