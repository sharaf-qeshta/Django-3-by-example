from django import forms
from .models import Comment


# Remember
# that Django has two base classes to build forms: Form and ModelForm.
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=256)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):  # for searching
    query = forms.CharField()


'''
The save() method is available for ModelForm but not 
for Form instances, since they are not linked to any model.

'''


'''
You are currently using SQLite for your blog project. This is sufficient for 
development purposes. However, for a production environment, you will need 
a more powerful database, such as PostgreSQL, MariaDB, MySQL, or Oracle.
'''