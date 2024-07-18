from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
# from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView

from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.customer.forms import CreateCustomerForm
from apps.customer.models import Customer
from apps.location.forms import StoreForm, StoreImageFormSet, AreaForm, AisleForm, UprightForm, AssignItemForm
from apps.location.models import Store, Area, Aisle, Upright, AssignItem
from apps.product.models import Product
from apps.user.forms import CreateUserForm
from apps.user.models import User
from apps.user.views import ListUserViewJson


def location(request):
    return HttpResponse('hello world')

    # def post(self, request, *args, **kwargs):
    #     form = CreateCustomerForm(request.POST)
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

class ListLocationView(AdminRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'location/list.html'

class ListLocationViewJson(AdminRequiredMixin, AjayDatatableView):
    model = User
    columns = ['first_name', 'last_name', 'email', 'actions']
    exclude_from_search_columns = ['actions']
    # extra_search_columns = ['']

    def get_initial_queryset(self):
        return self.model.objects.filter(user_type='customer')

    def render_column(self, row, column):

        if column == 'actions':
            detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
                reverse('admin-location-detail', kwargs={'customer_id': row.pk}))
            return detail_action
        else:
            return super(ListLocationViewJson, self).render_column(row, column)




# class LocationTemplateView(TemplateView):
#     model = Product
#     template_name = 'location/detail.html'


class StoreCreateView(CreateView):
    model = Store
    form_class = StoreForm
    template_name = 'location/form.html'
    success_url = reverse_lazy('admin-location-list')

    def get_success_url(self):
        return reverse_lazy('admin-location-detail', kwargs={'customer_id': self.kwargs['customer_id']})

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['customer_id'] = self.kwargs['customer_id']
        return context

    def form_valid(self, form):
        store  = form.save(commit=False)
        customer_id = self.kwargs['customer_id']
        customer = get_object_or_404(User, id=customer_id)
        store.customer =customer
        store.save()
        return super().form_valid(form)

    def post(self,request, *args, **kwargs):
        self.object  = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# class StoreTemplateView(TemplateView):
#     template_name = 'location/store_template.html'

class ListCustomerLocationView(TemplateView):
    template_name = 'location/store_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer_id = self.kwargs.get('customer_id')
        context['customer'] = get_object_or_404(User, id=customer_id)
        context['stores'] = Store.objects.filter(customer_id=customer_id)
        return context

class ListLocationDetailViewJson(AdminRequiredMixin, AjayDatatableView):
    model = Store
    columns = ['customer_id','name','actions']

    def get_initial_queryset(self):
        customer_id = self.kwargs.get('customer_id')
        return self.model.objects.filter(customer_id=customer_id)

    def render_column(self, row, column):

        if column == 'actions':
            detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
                reverse('admin-location-area', kwargs={'store_id': row.pk}))
            return detail_action
        else:
            return super(ListLocationDetailViewJson, self).render_column(row, column)


class AreaTemplateView(TemplateView):
    template_name = 'location/area_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        store_id = self.kwargs.get('store_id')
        context['store'] = get_object_or_404(Store, id=store_id)

        return context


class AreaCreateView(CreateView):
    model = Area
    form_class = AreaForm
    template_name = 'location/area_form.html'
    success_url = reverse_lazy('admin-location-list')

    def get_success_url(self):
        return reverse_lazy('admin-location-area', kwargs={'store_id': self.kwargs['store_id']})

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['store_id'] = self.kwargs['store_id']
        return context

    def form_valid(self, form):
        area  = form.save(commit=False)
        store_id = self.kwargs['store_id']
        store = get_object_or_404(Store, id=store_id)
        area.store =store
        area.save()
        return super().form_valid(form)

    def post(self,request, *args, **kwargs):
        self.object  = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ListLocationAreaViewJson(AjayDatatableView):
    model = Area
    columns = ['store_id','id','area_name','actions']


    def get_initial_queryset(self):
        store_id = self.kwargs.get('store_id')
        return self.model.objects.filter(store_id=store_id)

    def render_column(self, row, column):

        if column == 'actions':
            detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
                reverse('admin-location-asile', kwargs={'area_id': row.pk}))
            return detail_action
        else:
            return super(ListLocationAreaViewJson, self).render_column(row, column)

class AsileTemplateView(TemplateView):
    template_name = 'location/asile_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        area_id = self.kwargs.get('area_id')
        context['area'] = get_object_or_404(Area, id=area_id)

        return context

class AisleCreateView(CreateView):
    model = Aisle
    form_class = AisleForm
    template_name = 'location/asile_form.html'
    success_url = reverse_lazy('admin-location-asile')

    def get_success_url(self):
        return reverse_lazy('admin-location-asile', kwargs={'area_id': self.kwargs['area_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['area_id'] = self.kwargs['area_id']
        return context

    def form_valid(self, form):
        aisle = form.save(commit=False)
        area_id = self.kwargs['area_id']
        area = get_object_or_404(Area, id=area_id)
        aisle.area = area
        aisle.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ListLocationAisleViewJson(AjayDatatableView):
    model = Aisle
    columns = ['id','area_id','aisle_name','actions']

    def get_initial_queryset(self):
        area_id = self.kwargs.get('area_id')
        return self.model.objects.filter(area_id=area_id)

    def render_column(self, row, column):

        if column == 'actions':
            detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
                reverse('admin-location-upright',kwargs={'aisle_id': row.pk}))
            return detail_action
        else:

            return super(ListLocationAisleViewJson, self).render_column(row, column)

class UprightTemplateView(TemplateView):
    template_name = 'location/upright_template.html'
#
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aisle_id = self.kwargs.get('aisle_id')
        context['aisle'] = get_object_or_404(Aisle, id=aisle_id)

        return context
#
#
class UprightCreateView(CreateView):
    model = Upright
    form_class = UprightForm
    template_name = 'location/upright_form.html'
    success_url = reverse_lazy('admin-location-upright')
#
    def get_success_url(self):
        return reverse_lazy('admin-location-upright', kwargs={'aisle_id': self.kwargs['aisle_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aisle_id'] = self.kwargs['aisle_id']
        return context

    def form_valid(self, form):
        upright = form.save(commit=False)
        aisle_id = self.kwargs['aisle_id']
        aisle = get_object_or_404(Aisle, id=aisle_id)
        upright.aisle = aisle
        upright.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
#
class ListLocationUprightViewJson(AjayDatatableView):
    model = Upright
    columns = ['id','aisle_id','upright_name','actions']

    def get_initial_queryset(self):
        aisle_id = self.kwargs.get('aisle_id')
        return self.model.objects.filter(aisle_id=aisle_id)

    def render_column(self, row, column):

        if column == 'actions':
            detail_action = '<a href={} role="button" class="btn btn-info btn-xs mr-1 text-white">Detail</a>'.format(
                reverse('admin-location-assign', kwargs={'upright_id': row.pk}))
            return detail_action
        else:

            return super(ListLocationUprightViewJson, self).render_column(row, column)

class AssignItemTemplateView(TemplateView):
    template_name = 'location/assign_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        upright_id = self.kwargs.get('upright_id')
        context['upright'] = get_object_or_404(Upright, id=upright_id)

        return context


class AssignItemCreateView(CreateView):
    model = AssignItem
    form_class = AssignItemForm
    template_name = 'location/assign_form.html'
    success_url = reverse_lazy('admin-location-assign')

    def get_success_url(self):
        return reverse_lazy('admin-location-assign', kwargs={'upright_id': self.kwargs['upright_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upright_id'] = self.kwargs['upright_id']
        return context

    def form_valid(self, form):
        assign = form.save(commit=False)
        upright_id = self.kwargs['upright_id']
        upright = get_object_or_404(Upright, id=upright_id)
        assign.upright = upright
        assign.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ListLocationAssignItemViewJson(AjayDatatableView):
    model = AssignItem
    columns = ['id','upright_id','upc','sku','barcode_number','actions']

    def get_initial_queryset(self):
        upright_id = self.kwargs.get('upright_id')
        return self.model.objects.filter(upright_id=upright_id)