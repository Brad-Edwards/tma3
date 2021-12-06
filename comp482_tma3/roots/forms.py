from django.contrib import admin
from django import forms as admin_forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import gettext_lazy as _


from roots.models import Attendance, Classroom, ContactInfo, Food, Menu
from comp482_tma3.users.models import User

class AttendanceAdminForm(admin_forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AttendanceAdminForm, self).__init__(*args, **kwargs)
        self.fields['children'].queryset = User.objects.filter(role=User.UserRoles.CHILD)


class ClassroomAdminForm(admin_forms.ModelForm):
    kids = admin_forms.ModelMultipleChoiceField(queryset=User.objects.filter(role=User.UserRoles.CHILD),
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
        self.fields['kids'].queryset = User.objects.filter(role=User.UserRoles.CHILD)


class ContactInfoAdminForm(admin_forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class MenuAdminForm(admin_forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'


class FoodAdminForm(admin_forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'
