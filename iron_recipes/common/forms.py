from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)
        widgets = {
            'comment_text': forms.Textarea(attrs={'placeholder': 'Add comment...', })
        }


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by recipe name...',
            }
        )
    )


class CommentEditForm(CommentForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Search by recipe name...',
            }
        )


class CommentDeleteForm(CommentForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
