from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CharliUser


class CharliUserCreationForm(UserCreationForm):

    class Meta:
        model = CharliUser
        fields = ("email", "first_name", "last_name")


class CharliUserChangeForm(UserChangeForm):

    class Meta:
        model = CharliUser
        fields = ("email", "first_name", "last_name")
        

# class SignUpForm(UserCreationForm):

# 	email = forms.EmailField(required=True)

# 	class Meta:
# 		model = User
# 		fields = ("username", "email", "password1", "password2")

# 	def save(self, commit=True):
# 		# import pdb; pdb.set_trace()
# 		user = super(SignUpForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user
