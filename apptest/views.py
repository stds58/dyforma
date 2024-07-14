from django.shortcuts import render, get_object_or_404, redirect
from .models import Head, Position
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import HeadForm, PositionForm, HeadFormSet
from django.urls import reverse_lazy
from django.http import Http404, HttpResponseRedirect


class HeadList(ListView):
    model = Head
    orderng = 'id'
    template_name = 'HeadList.html'
    context_object_name = 'Heads'
    paginate_by = 10


class HeadView(CreateView):
    form_class = HeadForm
    model = Head
    template_name = 'HeadCreate.html'
    success_url = ''

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        head_form = HeadFormSet()
        return self.render_to_response(self.get_context_data(form=form,head_form=head_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        head_form =HeadFormSet(self.request.POST)
        if (form.is_valid() and head_form.is_valid()):
            #return super(HeadView, self).form_valid(form)
            return self.form_valid(form, head_form)
        else:
            return self.form_invalid(form, head_form)

    def form_valid(self, form, head_form):
        self.object = form.save()
        head_form.instance = self.object
        head_form.instance.user = self.request.user
        head_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, head_form):
        return self.render_to_response(self.get_context_data(form=form,head_form=head_form))



class PositionList(ListView):
    model = Position
    orderng = 'id'
    template_name = 'PositionList.html'
    context_object_name = 'Positions'
    paginate_by = 10


class PositionView(CreateView):
    form_class = PositionForm
    model = Position
    template_name = 'Edit.html'
    success_url = ''



