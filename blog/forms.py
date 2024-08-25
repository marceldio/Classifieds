from django import forms
from django.forms import ModelForm

from blog.models import Blog, Version

# class StyleForMixin:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'

class BlogModeratorForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'is_published')


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('views_counter','owner', 'is_published')

    # Список запрещенных слов
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно',
                       'обман', 'полиция', 'радар']


    def clean_name(self):
        name = self.cleaned_data.get('title')
        if any(word in name.lower() for word in self.forbidden_words):
            raise forms.ValidationError('The title contains forbidden words.')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('content')
        if any(word in description.lower() for word in self.forbidden_words):
            raise forms.ValidationError('The content contains forbidden words.')
        return description


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
