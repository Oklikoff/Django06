from django import forms
from .models import *
from .models import Product


class FormaSok(forms.Form):
    all = Company.objects.all()
    mas=[]
    for a in all:
        mas.append((a.id,a.title))
    print(mas)
    # firma=forms.ModelChoiceField(all,)
    #firma = forms.ChoiceField(choices=tuple(mas),required=False)
    firma = forms.ModelChoiceField(Company.objects.all(), required=False)
    sok=forms.ModelChoiceField(Product.objects.all(),required=False)

class FormaStudents(forms.Form):
    all = Course.objects.all()
    mas=[]
    for a in all:
        mas.append((a.id,a.title))
    print(mas)

    course = forms.ModelChoiceField(Course.objects.all(), required=False)
    name=forms.ModelChoiceField(Student.objects.all(),required=False)

class FormaUser(forms.Form):
    user=forms.ModelChoiceField(User.objects.all())