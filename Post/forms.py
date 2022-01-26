from django import forms
from . import models

class AddQuestion(forms.ModelForm):
    class Meta:
        model = models.question
        fields = ['Que_text','tags']

class AddAnswer(forms.ModelForm):
    class Meta:
        model = models.answer
        fields = ['Ans_body']
        widgets = {
            'Ans_body': forms.Textarea(attrs={'class':'form-control'}),
        }

class AddComment_Ques(forms.ModelForm):
    class Meta:
        model = models.comment
        fields = ['comment_text']

class EditComment(forms.ModelForm):
    class Meta:
        model = models.comment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={'class':'form-control'}),
        }

class AddComment_Ans(forms.ModelForm):
    class Meta:
        model = models.comment
        fields = ['comment_text']

class EditForm(forms.ModelForm):
    class Meta:
        model = models.question
        fields = ['Que_text','tags']
        widgets = {
            'Que_text': forms.Textarea(attrs={'class':'form-control'}),
        }