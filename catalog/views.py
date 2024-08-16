from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = ('main/product_form.html')
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        if form.is_valid():
            product = form.save()
            product.slug = slugify(product.product)
            product.save()
        return super().form_valid(form)

    # def contact(request):
    #     if request.method == 'POST':
    #         name = request.POST.get('name')
    #         tel = request.POST.get('tel')
    #         message = request.POST.get('message')
    #         print(f'You have new message from {name}({tel}): {message}')
    #     return render(request, 'main/contact.html')


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = ('main/product_form.html')

    def get_success_url(self):
        return reverse('catalog:product_view', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    template_name = ('main/product_delete.html')
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_list')

class ProductListView(ListView):
    model = Product
    template_name = ('main/product_list.html')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        products = self.get_queryset()
        for product in products:
            product.version = product.version_set.filter(is_current=True).first()

        context_data['object_list'] = products
        return context_data


class ProductDetailView(DetailView):
    model = Product
    template_name = ('main/product_detail.html')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object
