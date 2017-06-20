""" Django forms of ADMIN core explore federated search
"""
from django import forms

# list of possible protocols available in the form
PROTOCOLS = (('http', 'HTTP'),
             ('https', 'HTTPS'))


class RepositoryForm(forms.Form):
    """ Form to register a new repository.
    """
    name = forms.CharField(label='Instance Name', max_length=100, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    endpoint = forms.CharField(label='Endpoint', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               required=True)
    client_id = forms.CharField(label='Client ID', max_length=100, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    client_secret = forms.CharField(label='Client Secret', max_length=100, required=True,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    timeout = forms.IntegerField(label="Timeout (s)", min_value=1, max_value=60, initial=1,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}))


class RefreshRepositoryForm(forms.Form):
    """ Form to refresh the token of a repository.
    """
    client_id = forms.CharField(label='Client ID', max_length=100, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    client_secret = forms.CharField(label='Client Secret', max_length=100, required=True,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    timeout = forms.IntegerField(label="Timeout (s)", min_value=1, max_value=60, initial=1,
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}))
