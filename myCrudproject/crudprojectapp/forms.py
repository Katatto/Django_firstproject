from django import forms  
from crudprojectapp.models import Student  

class StudentForm(forms.ModelForm):  
    # GENDER_CHOICES = [
    #     ('female', 'Female'),
    #     ('male', 'Male'),
    #     ('other', 'Other'),
    # ]

    # gender = forms.ChoiceField(
    #     choices=GENDER_CHOICES,
    #     widget=forms.RadioSelect(attrs={'class': 'form-control'}),
    # )

    class Meta:  
        model = Student  
        fields = ['fname','lname','gender','address','email','contact'] 
      
        widgets = { 
            'fname': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'lname': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'gender': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'address': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.NumberInput(attrs={ 'class': 'form-control' }),
      }
        
        