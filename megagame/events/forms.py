from django import forms

class ArticleForm(forms.Form):
    data = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Чтобы отделить основную'
                                'часть от заголовка - ' 
                                'оставь между ними пустую строку'
            }
        ), 
        label=''
    )

    def split_header_and_body(self):
        data_text = self.data['data']
        if '\r\n\r\n' in data_text:
            return data_text.split('\r\n\r\n', 1)
        else:
            return data_text