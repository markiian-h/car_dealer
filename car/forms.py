from django import forms
from .models import *

ENGINE_CHOICES = (
    ('e', 'Electric'),
    ('d', 'Diesel'),
    ('g1', 'Gasoline'),
    ('g2', 'Gas'),
)


class BaseUpdateClass:

    def clean_model(self):
        brand = self.cleaned_data['brand']
        data = self.cleaned_data['model']
        self.cleaned_data.pop('brand')
        m = Model.objects.filter(name=data)
        if m:
            return m[0]
        else:
            b = Brand.objects.filter(name=brand)
            if b:
                m = Model(name=data, brand=b[0])
                m.save()
                return Model.objects.last()
            else:
                b = Brand(name=brand)
                b.save()
                b_last = Brand.objects.last()
                m = Model(name=data, brand=b_last)
                m.save()
                return Model.objects.last()

    def clean_color(self):
        data = self.cleaned_data['color']
        c = Color.objects.filter(name=data)
        if c:
            return c[0]

        c = Color(name=data)
        c.save()
        return c

    def clean_picture(self):
        data = self.cleaned_data['picture']
        p = Picture.objects.filter(url=data)
        if p:
            return p[0]
        p = Picture(url=data, meta_data='meta')
        p.save()
        return Picture.objects.last()


class BaseCarForm(forms.ModelForm):
    brand = forms.CharField(max_length=64)
    model = forms.CharField(max_length=64)
    color = forms.CharField(max_length=64)
    picture = forms.ImageField()

    class Meta:
        model = Car
        fields = ['brand', 'model', 'color', 'picture', 'is_published', 'price', 'year', 'engine_type', 'capacity',
                  'gear_case', 'doors']


class AddCarForm(BaseCarForm, BaseUpdateClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CarUpdateForm(BaseCarForm, BaseUpdateClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
