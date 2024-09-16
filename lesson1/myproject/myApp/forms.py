from django import forms
from . import models


# Create Custom Form in this way


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["title", "body", "slug", "banner"]
