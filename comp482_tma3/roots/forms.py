import logging
import datetime
import dateutil.relativedelta

from django.core.exceptions import ValidationError

from django import forms as forms
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

from phonenumber_field.formfields import PhoneNumberField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, ButtonHolder, Div, Fieldset, HTML, Layout, Submit

class DateInput(forms.widgets.DateInput):
    input_type = 'date'

class CheckInForm(forms.Form):
    class Children(TextChoices):
        T = 'Tina', _("Tina")
        L = 'Lotanna', _("Lotanna")
        M = 'Mei', _("Mei")


    def validate_check_in_time(self):
        input_time = datetime.datetime.now().replace(hour=self.hour, minute=self.minute, second=self.second)
        diff = input_time - datetime.datetime.now()
        delta = datetime.timedelta(minutes=30)
        opening = datetime.datetime.now().replace(hour=6, minute=0, second=0)
        if  diff > delta:
            raise ValidationError("Cannot check in more than 30 minutes in advance.")

        if input_time < opening:
            raise ValidationError("Cannot check in before the centre opens at %s." % opening.strftime('%I:%M %p'))

    children = forms.MultipleChoiceField(label="Children to Check In", required=True, choices = Children.choices,
                                               widget=forms.CheckboxSelectMultiple())
    check_in_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True,
                                          initial=datetime.datetime.now().strftime('%Y-%m-%d'))
    check_in_time = forms.TimeField(widget=forms.DateInput(attrs={'type': 'time'}), required=True,
                                          initial=datetime.datetime.now().strftime('%I:%M'),
                                          validators=[validate_check_in_time])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['check_in_date'].widget.attrs['readonly'] = True
        self.helper = FormHelper()
        self.helper.form_id = "child_check_in_form"
        self.helper.form_class = "roots-form"
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            Div(
                HTML("""
                    <h1 class='text-center mb-5'>Check In</h1>
                """),
                Fieldset(
                    '',
                    Div(
                        'children',
                        css_class = 'row'
                    ),
                    Div(
                        'check_in_date',
                        'check_in_time',
                        css_class = 'row'
                    ),
                ),
                ButtonHolder(
                    Submit('submit', 'Check In', css_class='btn-primary')
                ),
                css_class = 'container w-50 mt-5'
            ),
        )


class CheckOutForm(forms.Form):
    class Children(TextChoices):
        T = 'Tina', _("Tina")
        L = 'Lotanna', _("Lotanna")
        M = 'Mei', _("Mei")


    def validate_check_out_time(self):
        input_time = datetime.datetime.now().replace(hour=self.hour, minute=self.minute, second=self.second)
        diff = input_time - datetime.datetime.now()
        delta = datetime.timedelta(minutes=30)
        closing = datetime.datetime.now().replace(hour=17, minute=0, second=0)
        if input_time > closing:
            raise ValidationError("Cannot check out after the centre closes at %s." % closing.strftime('%I:%M %p'))

        if abs(diff) > delta:
            raise ValidationError("Cannot check out more than 30 minutes ahead of time.")

    children = forms.MultipleChoiceField(label="Children to Check Out", required=True, choices = Children.choices,
                                               widget=forms.CheckboxSelectMultiple())
    check_out_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True,
                                          initial=datetime.datetime.now().strftime('%Y-%m-%d'))
    check_out_time = forms.TimeField(widget=forms.DateInput(attrs={'type': 'time'}), required=True,
                                          initial=datetime.datetime.now().strftime('%I:%M'),
                                     validators=[validate_check_out_time])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['check_out_date'].widget.attrs['readonly'] = True
        self.helper = FormHelper()
        self.helper.form_id = "child_check_out_form"
        self.helper.form_class = "roots-form"
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            Div(
                HTML("""
                    <h1 class='text-center mb-5'>Check In</h1>
                """),
                Fieldset(
                    '',
                    Div(
                        'children',
                        css_class = 'row'
                    ),
                    Div(
                        'check_out_date',
                        'check_out_time',
                        css_class = 'row'
                    ),
                ),
                ButtonHolder(
                    Submit('submit', 'Check Out', css_class='btn-primary')
                ),
                css_class = 'container w-50 mt-5'
            ),
        )


class NapForm(forms.Form):
    class Children(TextChoices):
        T = 'Tina', _("Tina")
        L = 'Lotanna', _("Lotanna")
        M = 'Mei', _("Mei")


    def clean(self):
        if self.cleaned_data['nap_start_time'] > self.cleaned_data['nap_end_time']:
            self.add_error('nap_start_time', 'Nap cannot end before it begins.')

        return self.cleaned_data

    children = forms.MultipleChoiceField(label="Children", required=True, choices = Children.choices,
                                               widget=forms.CheckboxSelectMultiple())
    nap_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True,
                                          initial=datetime.datetime.now().strftime('%Y-%m-%d'))
    nap_start_time = forms.TimeField(widget=forms.DateInput(attrs={'type': 'time'}), required=True,
                                          initial=datetime.datetime.now().strftime('%I:%M'))
    nap_end_time = forms.TimeField(widget=forms.DateInput(attrs={'type': 'time'}), required=True,
                                           initial=datetime.datetime.now().strftime('%I:%M'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nap_date'].widget.attrs['readonly'] = True
        self.helper = FormHelper()
        self.helper.form_id = "child_nap_form"
        self.helper.form_class = "roots-form"
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            Div(
                HTML("""
                    <h1 class='text-center mb-5'>Nap</h1>
                """),
                Fieldset(
                    '',
                    Div(
                        'children',
                        css_class = 'row'
                    ),
                    Div(
                        'nap_date',
                        css_class = 'row'
                    ),
                    Div(
                        'nap_start_time',
                        css_class = 'row'
                    ),
                    Div(
                        'nap_end_time',
                        css_class = 'row'
                    )
                ),
                ButtonHolder(
                    Submit('submit', 'Log Nap', css_class='btn-primary')
                ),
                css_class = 'container w-50 mt-5'
            ),
        )


class RegisterChildForm(forms.Form):
    class Classrooms(TextChoices):
        JKL1 = 'JKL1', _('Junior Kindergarten Level 1')
        JKL2 = 'JKL2', _('Junior Kindergarten Level 2')


    class Provinces(TextChoices):
        AB = 'AB', _("AB")
        BC = 'BC', _("BC")
        MB = 'MB', _("MB")
        NB = "NB", _("NB")
        NL = "NL", _("NL")
        NS = "NS", _("NS")
        NT = "NT", _("NT")
        NU = "NU", _("NU")
        ON = "ON", _("ON")
        PE = "PE", _("PE")
        QC = "QC", _("QC")
        SK = "SK", _("SK")
        YT = "YT", _("YT")


    def validate_child_date_of_birth(self):
        input_date = datetime.datetime.now().replace(year=self.year, day=self.day, month=self.month)
        cut_off_birth_date = datetime.datetime.now() - dateutil.relativedelta.relativedelta(years=6)
        if input_date < cut_off_birth_date:
            raise ValidationError("The centre does not accept children six years old or older.")

    child_classroom = forms.ChoiceField(
        label = "Classroom",
        widget = forms.Select(),
        choices = Classrooms.choices,
        required = True,
    )

    child_first_name = forms.CharField(label="First Name", max_length=255, required=True)
    child_last_name = forms.CharField(label="Last Name", max_length=266, required=True)
    child_date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(
        attrs={'type': 'date'}), validators=[validate_child_date_of_birth])

    child_lives_with_guardian1 = forms.BooleanField(label="Child's Primary Address", required=False)
    child_lives_with_guardian2 = forms.BooleanField(label="Child's Primary Address", required=False)
    guardian1_first_name = forms.CharField(label="First Name", max_length=255, required=True)
    guardian1_last_name = forms.CharField(label="Last Name", max_length=266, required=True)
    guardian1_date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(
        attrs={'type': 'date',}))
    guardian1_address = forms.CharField(label="Address", max_length=255, required=True)
    guardian1_city = forms.CharField(label="City", max_length=255, required=True, initial="Chilliwack")
    guardian1_province = forms.ChoiceField(
        widget = forms.Select(),
        choices=Provinces.choices,
        initial = 'BC',
        required=True)
    guardian1_country = forms.CharField(label="Country", max_length=255, required=True, initial="Canada")
    guardian1_postal_code = forms.CharField(label="Postal Code", max_length=255, required=True)
    guardian1_phone1 = PhoneNumberField(widget=forms.TextInput(attrs={}), label="Primary Phone Number", required=True)
    guardian1_phone2 = PhoneNumberField(widget=forms.TextInput(attrs={}), label="Alternate Phone Number", required=False)

    guardian2_first_name = forms.CharField(label="First Name", max_length=255, required=False)
    guardian2_last_name = forms.CharField(label="Last Name", max_length=266, required=False)
    guardian2_date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(
        attrs={'type': 'date', }), required=False)
    guardian2_address = forms.CharField(label="Address", max_length=255, required=False)
    guardian2_city = forms.CharField(label="City", max_length=255, required=False, initial="Chilliwack")
    guardian2_province = forms.ChoiceField(
        widget=forms.Select(),
        choices=Provinces.choices,
        initial='BC',
        required=False)
    guardian2_country = forms.CharField(label="Country", max_length=255, required=False, initial="Canada")
    guardian2_postal_code = forms.CharField(label="Postal Code", max_length=255, required=False)
    guardian2_phone1 = PhoneNumberField(widget=forms.TextInput(attrs={}), label="Primary Phone Number",
                                        required=False)
    guardian2_phone2 = PhoneNumberField(widget=forms.TextInput(attrs={}), label="Alternate Phone Number",
                                        required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "child_registration_form"
        self.helper.form_class = "roots-form"
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            Div(
                HTML("""<h1>New Registration</h1>"""),
                # Classroom
                Fieldset(
                    'Classroom',
                    Div(
                        'child_classroom',
                        css_class = 'row',
                    ),
                ),
                # Child
                Fieldset(
                    'Child',
                    Div(
                        Div(
                            'child_first_name',
                            css_class = "col",
                        ),
                        Div(
                            'child_last_name',
                            css_class = "col",
                        ),
                        css_class = 'row'
                    ),
                    'child_date_of_birth',
                ),
                # Guardian 1
                Fieldset(
                    'Parent',
                    Div(
                        Div(
                            'guardian1_first_name',
                            css_class = 'col',
                        ),
                        Div(
                            'guardian1_last_name',
                            css_class = 'col',
                        ),
                        css_class = 'row',
                    ),
                    Div(
                        'guardian1_date_of_birth',
                        css_class = 'row',
                    ),
                    Fieldset(
                        '',
                        #Div(
                        #    'child_lives_with_guardian1',
                        #    css_class = 'row',
                        #),
                        Div(
                            Div(
                                'guardian1_address',
                                css_class = 'col',
                            ),
                            Div(
                                'guardian2_city',
                                css_class = 'col',
                            ),
                            css_class = 'row',
                        ),
                        Div(
                            Div(
                                'guardian1_province',
                                css_class = 'col',
                            ),
                            Div(
                                'guardian1_country',
                                css_class = 'col',
                            ),
                            Div(
                                'guardian1_postal_code',
                                css_class = 'col',
                            ),
                            css_class = 'row',
                        ),
                        Div(
                            Div(
                                'guardian1_phone1',
                                css_class = 'col',
                            ),
                            Div(
                                'guardian1_phone2',
                                css_class = 'col',
                            ),
                            css_class = 'row',
                        ),
                    ),
                ),
                #HTML("""
                #    <input class='btn-secondary' type='button' value='Add Guardian' name='addGuardian2' id='button-id-guardian2Button'>
                #"""),
                Fieldset(
                    'Guardian 2',
                    Div(
                        Div(
                            Div(
                                'guardian2_first_name',
                                css_class='col',
                            ),
                            Div(
                                'guardian2_last_name',
                                css_class='col',
                            ),
                            css_class='row',
                        ),
                        Div(
                            'guardian2_date_of_birth',
                            css_class='row',
                        ),
                        Fieldset(
                            '',
                        Div(
                            'child_lives_with_guardian2',
                            css_class = 'row',
                        ),
                        Div(
                            Div(
                                'guardian2_address',
                                css_class='col',
                            ),
                            Div(
                                'guardian2_city',
                                css_class='col',
                            ),
                            css_class='row',
                        ),
                        Div(
                            Div(
                                'guardian2_province',
                                css_class='col',
                            ),
                            Div(
                                'guardian2_country',
                                css_class='col',
                            ),
                            Div(
                                'guardian2_postal_code',
                                css_class='col',
                            ),
                            css_class='row',
                        ),
                        Div(
                            Div(
                                'guardian2_phone1',
                                css_class='col',
                            ),
                            Div(
                                'guardian2_phone2',
                                css_class='col',
                            ),
                            css_class='row',
                            ),
                        ),
                    ),
                    css_class='d-none',
                    css_id='register_guardian2',
                ),
                ButtonHolder(
                    Submit('submit', 'Register', css_class='btn-primary')
                ),
                css_class = 'container w-50'
            ),
        )


class ToiletingForm(forms.Form):
    class Children(TextChoices):
        T = 'Tina', _("Tina")
        L = 'Lotanna', _("Lotanna")
        M = 'Mei', _("Mei")


    class Options(TextChoices):
        PEE = 'Pee', _("Pee")
        POO = 'Poo', _("Poo")
        BOTH = 'Both', _("Both")
        NONE = 'None', _("None")


    def validate_results(self):
        if 'None' in self and len(self) > 1:
            raise ValidationError("Result cannot be 'None' and something else.")


    children = forms.ChoiceField(label="Children", required=True, choices = Children.choices)
    toileting_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True,
                                          initial=datetime.datetime.now().strftime('%Y-%m-%d'))
    toileting_time = forms.TimeField(widget=forms.DateInput(attrs={'type': 'time'}), required=True,
                                          initial=datetime.datetime.now().strftime('%I:%M'))
    results = forms.MultipleChoiceField(label="Results", required=True, choices=Options.choices,
                                               widget=forms.CheckboxSelectMultiple(), validators=[validate_results])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['toileting_date'].widget.attrs['readonly'] = True
        self.helper.form_id = "child_toileting_form"
        self.helper.form_class = "roots-form"
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            Div(
                HTML("""
                    <h1 class='text-center mb-5'>Toileting</h1>
                """),
                Fieldset(
                    '',
                    Div(
                        'children',
                        css_class = 'row'
                    ),
                    Div(
                        'toileting_date',
                        css_class = 'row'
                    ),
                    Div(
                        'toileting_time',
                        css_class = 'row'
                    ),
                    Div(
                        'results',
                        css_class = 'row'
                    )
                ),
                ButtonHolder(
                    Submit('submit', 'Log Toileting', css_class='btn-primary')
                ),
                css_class = 'container w-50 mt-5'
            ),
        )
