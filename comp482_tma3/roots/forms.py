from django.contrib import admin
from django import forms as admin_forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import gettext_lazy as _


from roots.models import Child, Classroom, \
    ContactInfo, Food, Meal, Menu, Nap, Parent, Person, Registration, Toileting


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


class ToiletingAdminForm(admin_forms.ModelForm):
    class Meta:
        model = Toileting
        fields = '__all__'
