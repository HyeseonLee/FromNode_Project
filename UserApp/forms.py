from django import forms
from .models import User,Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name')
        
# user의 기본 기능은 더 있습니다! 없을경우 profileform에 추가하기

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         modle = Profile
#         fields = ('ex')
