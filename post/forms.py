from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {
            'placeholder': 'Введите название статьи',
            'class': 'inline text-input title-input'}
        self.fields['image'].widget.attrs = {'class': 'file-input', 'id': 'image-upload'}
        self.fields['text'].widget.attrs = {'style': 'height: 21em; padding: 12px;', 'class': 'text-input'}

    class Meta:
        model = Post
        fields = ('title', 'text', 'image',)