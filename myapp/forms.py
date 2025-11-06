from django import forms

from .models import BlogPost

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)



class EventForm(forms.Form):
    name = forms.CharField(max_length=100)
    event_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    category = forms.ChoiceField(choices=[('tech','Tech'),('music','Music'),('art','Art')])



class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20,required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email must be @example.com")
        return email
    

    def clean(self):
        cleaned_data = super().clean()
        pw = cleaned_data.get("password")
        cpw = cleaned_data.get("confirm_password")

        if pw and cpw and pw!=cpw:
            raise forms.ValidationError("Passwords do not match")









class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost 
        fields = ["title","content", "views", "published"]
