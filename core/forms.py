from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full border border-solid bg-transparent py-2 pl-6 pr-4 outline-none focus:border-blue-400 focus-visible:shadow-none dark:border-slate-500 dark:focus:border-blue-400 dark:bg-slate-800 dark:text-slate-300'
            })
            field.widget.attrs['errors'] = f"{field.label} الزامی است."
            
        # Add Alpine JS code to password fields
        self.fields['password1'].widget.attrs.update({
            'x-bind:type': "showPassword ? 'text' : 'password'"
        })
        self.fields['password2'].widget.attrs.update({
            'x-bind:type': "showRepeatPassword ? 'text' : 'password'"
        })
        
        # Add autofocus to the first_name field
        self.fields['first_name'].widget.attrs.update({
            'autofocus': 'autofocus'
        })