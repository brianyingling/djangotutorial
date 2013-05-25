from django.db import models
from django import forms


class ContactForm(form.Form):
  subject = forms.CharField(max_length=100)
  email = forms.EmailField(required=False)
  message = forms.CharField(widget=forms.Textarea)

  # Django looks for any message starting with "clean_" and ends with
  #  the name of a field. If any such message exists, it's called during
  # validation.
  def clean_message(self):
    message = self.cleaned_data['message']
    num_words = len(message.split() )
    if num_words < 4:
      raise forms.ValidationError("Not enough words!")
    return message

# Create your models here.
