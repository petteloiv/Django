from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder' : '제목을 입력하세요.',
            }
        ),
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder':'내용을 입력하세요.',
                'rows' : 5,
                'cols':50,
                
            }
        ),
        error_messages={
            'required' : '내용이 입력되지 않으면 저장되지 않습니다.'
        }
    )

    class Meta:
        model = Article
        fields = '__all__'