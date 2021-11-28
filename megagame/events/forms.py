from django import forms

class ArticleForm(forms.Form):
    data = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Чтобы отделить основную'
                                'часть от заголовка - ' 
                                'напиши ее с новой строки'
            }
        ), 
        label=''
    )

    def split_header_and_body(self):
        data_text = self.data['data']
        if '\n' in data_text:
            return data_text.split('\n', 1)
        else:
            return data_text