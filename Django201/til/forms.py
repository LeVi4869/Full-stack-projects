from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update(
      {'class': 'my-2'}
    )
    self.fields['username'].widget.attrs.update(
      {'style': 'width: 500px'}
    )
    self.fields['password'].widget.attrs.update(
      {'class': 'my-2'}
    )
    self.fields['password'].widget.attrs.update(
      {'style': 'width: 506px'}
    )
    