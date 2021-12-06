from django.contrib import admin
from django import forms as admin_forms
from django.utils.translation import gettext_lazy as _

from roots.models import Attendance
from comp482_tma3.users.models import User

class AttendanceAdminForm(admin_forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AttendanceAdminForm, self).__init__(*args, **kwargs)
        self.fields['children'].queryset = User.objects.filter(role="CHILD")
