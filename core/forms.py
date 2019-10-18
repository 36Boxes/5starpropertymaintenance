
from django import forms
from django_select2.forms import Select2MultipleWidget


work_categories = (
    ('Roofing','Roofing'),
    ('Brickwork', 'Brickwork'),
    ('Driveway', 'Driveway'),
    ('Patio', 'Patio'),
    ('Turfing', 'Turfing'),
    ('Facias and Soffits', 'Facias & Soffits '),
    ('Guttering', 'Guttering'),
    ('Flat Roofing', 'Flat Roofing'),
    ('Plastering', 'Plastering'),
    ('Painting', 'Painting'),
    ('Rendering', 'Rendering'),
    ('Pebble Dashing', 'Pebble Dashing'),
    ('Fencing', 'Fencing'),
    ('Extensions', 'Extensions')
)


class Enquiry_Form(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'John',
        'class': 'form-control'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Smith',
        'class': 'form-control'
    }))
    phone = forms.CharField(max_length=11,widget=forms.TextInput(attrs={
        'placeholder' : '07123123123',
        'class': 'form-control'
    }))
    issue_category = forms.ChoiceField(choices= work_categories)
    issue = forms.CharField(max_length=5000, widget=forms.Textarea(attrs={
        'placeholder' : 'Brief Description of your issue',
        'class': 'form-control'
    }))




ratings = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


def get_choices():
    from .models import Before_and_afters
    projects = Before_and_afters.objects.filter(review=None)
    choices = ()
    for name in projects:
        project_name = name.project_name
        ob_to_go_in_list = (project_name, project_name)
        choices += (ob_to_go_in_list),
    return choices

class Review_Form(forms.Form):
    def __init__(self, *args, **kwargs):
        super(Review_Form, self).__init__(*args, **kwargs)
        self.fields['project'] = forms.ChoiceField(
            choices=get_choices(), widget=forms.Select(choices=get_choices()), required=True)
    rating = forms.ChoiceField(choices=ratings)
    customer_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'John Smith',
        'class': 'form-control'
    }))
    review = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder' : 'A Brief Description of what pleased you!',
        'class' : 'form-control'
    }))