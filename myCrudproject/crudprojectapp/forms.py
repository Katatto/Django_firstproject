from django import forms  
from crudprojectapp.models import Student  

class StudentForm(forms.ModelForm):  
 
    # gender = forms.ChoiceField(
    #         choices=[("Female", "Female"), ("Male", "Male"), ("Other", "Other")],
    #         widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
    #     )


    class Meta:  
        model = Student  
        fields = ['fname','lname','gender', 'address','email','contact'] 
      
        widgets = { 
            'fname': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'lname': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'gender': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'address': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.NumberInput(attrs={ 'class': 'form-control' }),
      }
        
        