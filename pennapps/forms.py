from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Applicant
from .models import Application
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = Applicant
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['school', 'year', 'major', 'phone_number', 'birthday', 'q1', 'q2', 'first_hackathon', 'team_member_1', 'team_member_2', 'team_member_3']
    def clean_team_member(self,field_name):
        email = self.cleaned_data.get(field_name)
        if email:
            try:
                user = Applicant.objects.get(email=email)
            except Applicant.DoesNotExist:
                raise forms.ValidationError("This user does not exist")
            return email
    def clean_team_member_1(self):
        return self.clean_team_member('team_member_1')
    def clean_team_member_2(self):
        return self.clean_team_member('team_member_2')
    def clean_team_member_3(self):
        return self.clean_team_member('team_member_3')
    def clean(self):
        cleaned_data = super().clean()
        is_penn_student = self.initial.get('is_penn_student', False)  # Assuming is_penn_student is passed in the initial data
        if is_penn_student:
            cleaned_data['school'] = 'University of Pennsylvania'
        required_fields = ['school', 'phone_number', 'birthday', 'q1', 'q2']
        for field in required_fields:
            if not cleaned_data.get(field):
                # raise forms.ValidationError("Please fill out all required fields.")
                self.add_error(field,f'Please fill out the {field} field')
        team_members = [cleaned_data.get('team_member_1'), cleaned_data.get('team_member_2'), cleaned_data.get('team_member_3')]
        team_members = [email for email in team_members if email]
        if len(team_members) > 3:
            raise forms.ValidationError("You can't have more than 3 team members")
        return cleaned_data