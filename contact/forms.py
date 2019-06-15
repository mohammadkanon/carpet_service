from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'comment']

    # def __init__(self, single, user_info, *args, **kwargs):
    #
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     self.tour = single
    #     if user_info is not False:
    #         self.fields['visitor_name'].initial = user_info['user_name']
    #         self.fields['visitor_email'].initial = user_info['user_email']
    #
    # def save(self, commit=False):
    #     this_obj = super(CommentForm, self).save(commit=False)
    #     this_obj.tour = self.tour
    #     this_obj.save()
    #
    #     return this_obj