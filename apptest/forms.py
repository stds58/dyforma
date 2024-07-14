
from django import forms
from .models import Head, Position
from django.forms.models import inlineformset_factory
from django.forms.models import BaseInlineFormSet


#ChildrenFormset = inlineformset_factory(Head, Position, fields = '__all__')
HeadFormSet = inlineformset_factory(Head, Position, fields = '__all__')

# class BaseChildrenFormset(BaseInlineFormSet):
#     def add_fields(self, form, index):
#         super(BaseChildrenFormset, self).add_fields(form, index)
#
#         # save the formset in the 'nested' property
#         form.nested = ChildrenFormset(
#             instance=form.instance,
#             data=form.data if form.is_bound else None,
#             files=form.files if form.is_bound else None,
#             prefix='address-%s-%s' % (
#                 form.prefix,
#                 ChildrenFormset.get_default_prefix()),
#             extra=1)


# ChildrenFormset = inlineformset_factory(Head,
#                                         Position,
#                                         formset=BaseChildrenFormset,
#                                         extra=1)

class HeadForm(forms.ModelForm):
    class Meta:
        model = Head
        fields = [
        'id',
        'f1',
        'f2'
        ]


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = [
        'id',
        'f3',
        'f4',
        'head'
        ]


