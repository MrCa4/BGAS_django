from django import forms


class PostForm(forms.Form):

    post_title = forms.CharField(label='Описание ', max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'myfieldclass'}))
    img = forms.ImageField(label='Изображение ', required=False)
