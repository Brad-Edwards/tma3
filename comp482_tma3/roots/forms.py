import datetime
from dateutil.relativedelta import relativedelta
import logging
from django.core.exceptions import ValidationError

import django.db.models
from django.contrib import admin
from django import forms as admin_forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

from phonenumber_field.formfields import PhoneNumberField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, ButtonHolder, Div, Fieldset, HTML, Layout, Submit

from roots.models import Child, Classroom, \
    ContactInfo, Family, Food, Meal, Menu, Nap, Parent, Person, \
    Registration, Toileting

class DateInput(admin_forms.widgets.DateInput):
    input_type = 'date'


class ChildAdminForm(admin_forms.ModelForm):
    class Meta:
        model = Child
        fields = '__all__'


class ClassroomAdminForm(admin_forms.ModelForm):
    kids = admin_forms.ModelMultipleChoiceField(queryset=Child.objects.all(),
                                                label=_("Children"),
                                                required=False,
                                                widget=FilteredSelectMultiple(
                                                    _("kids"),
                                                    False,
                                                ))

    class Meta:
        model = Classroom
        fields = ['name', 'kids', 'short_name']

    def __init(self, *args, **kwargs):
        super(ClassroomAdminForm, self).__init__(*args, **kwargs)
        self.fields['kids'].queryset = Child.objects.all()


class ContactInfoAdminForm(admin_forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class FamilyAdminForm(admin_forms.ModelForm):
    class Meta:
        model = Family
        fields = '__all__'


class FoodAdminForm(admin_forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'


class MealAdminForm(admin_forms.ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'


class MenuAdminForm(admin_forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        food = admin_forms.ModelMultipleChoiceField(queryset=Food.objects.all(),
                                                label=_("Menu Items"),
                                                required=False,
                                                widget=FilteredSelectMultiple(
                                                    _("food"),
                                                    False,
                                                ))


class NapAdminForm(admin_forms.ModelForm):
    class Meta:
        model = Nap
        fields = '__all__'


class ParentAdminForm(admin_forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'


class PersonAdminForm(admin_forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class RegistrationAdminForm(admin_forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'


class CheckInForm(admin_forms.Form):
    class Children(TextChoices):
        T = 'Tina', _("Tina")
        L = 'Lotanna', _("Lotanna")
        M = 'Mei', _("Mei")

    children = admin_forms.MultipleChoiceField(label="Children to Check In", required=True, choices = Children.choices,
                                               widget=admin_forms.CheckboxSelectMultiple())
    check_in_date = admin_forms.DateField(widget=admin_forms.DateInput(attrs={'type': 'date'}), required=True,
                                          initial=datetime.datetime.now().strftime('%Y-%m-%d'))
    check_in_time = admin_forms.TimeField(widget=admin_forms.DateInput(attrs={'type': 'time'}), required=True,
                                          initial=datetime.datetime.now().strftime('%I:%M'))



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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


class RegisterChildForm(admin_forms.Form):
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


    child_classroom = admin_forms.ChoiceField(
        label = "Classroom",
        widget = admin_forms.Select(),
        choices = Classrooms.choices,
        required = True,
    )

    child_first_name = admin_forms.CharField(label="First Name", max_length=255, required=True)
    child_last_name = admin_forms.CharField(label="Last Name", max_length=266, required=True)
    child_date_of_birth = admin_forms.DateField(label="Date of Birth", widget=admin_forms.DateInput(
        attrs={'type': 'date'}))

    child_lives_with_guardian1 = admin_forms.BooleanField(label="Child's Primary Address", required=False)
    child_lives_with_guardian2 = admin_forms.BooleanField(label="Child's Primary Address", required=False)
    guardian1_first_name = admin_forms.CharField(label="First Name", max_length=255, required=True)
    guardian1_last_name = admin_forms.CharField(label="Last Name", max_length=266, required=True)
    guardian1_date_of_birth = admin_forms.DateField(label="Date of Birth", widget=admin_forms.DateInput(
        attrs={'type': 'date',}))
    guardian1_address = admin_forms.CharField(label="Address", max_length=255, required=True)
    guardian1_city = admin_forms.CharField(label="City", max_length=255, required=True, initial="Chilliwack")
    guardian1_province = admin_forms.ChoiceField(
        widget = admin_forms.Select(),
        choices=Provinces.choices,
        initial = 'BC',
        required=True)
    guardian1_country = admin_forms.CharField(label="Country", max_length=255, required=True, initial="Canada")
    guardian1_postal_code = admin_forms.CharField(label="Postal Code", max_length=255, required=True)
    guardian1_phone1 = PhoneNumberField(widget=admin_forms.TextInput(attrs={}), label="Primary Phone Number", required=True)
    guardian1_phone2 = PhoneNumberField(widget=admin_forms.TextInput(attrs={}), label="Alternate Phone Number", required=False)

    guardian2_first_name = admin_forms.CharField(label="First Name", max_length=255, required=False)
    guardian2_last_name = admin_forms.CharField(label="Last Name", max_length=266, required=False)
    guardian2_date_of_birth = admin_forms.DateField(label="Date of Birth", widget=admin_forms.DateInput(
        attrs={'type': 'date', }), required=False)
    guardian2_address = admin_forms.CharField(label="Address", max_length=255, required=False)
    guardian2_city = admin_forms.CharField(label="City", max_length=255, required=False, initial="Chilliwack")
    guardian2_province = admin_forms.ChoiceField(
        widget=admin_forms.Select(),
        choices=Provinces.choices,
        initial='BC',
        required=False)
    guardian2_country = admin_forms.CharField(label="Country", max_length=255, required=False, initial="Canada")
    guardian2_postal_code = admin_forms.CharField(label="Postal Code", max_length=255, required=False)
    guardian2_phone1 = PhoneNumberField(widget=admin_forms.TextInput(attrs={}), label="Primary Phone Number",
                                        required=False)
    guardian2_phone2 = PhoneNumberField(widget=admin_forms.TextInput(attrs={}), label="Alternate Phone Number",
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


class ToiletingAdminForm(admin_forms.ModelForm):
    class Meta:
        model = Toileting
        fields = '__all__'
