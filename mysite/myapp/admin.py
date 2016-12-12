from django.contrib import admin

# Register your models here.
# from .forms import SignUpForm
from .models import SignUp


class SignUpAdmin(admin.ModelAdmin):
    # Customizing how adm works: displaying what I want to see
    # list_display = ["__str__", "date_created", "updated"]
    # form = SignUpForm
    list_display = ["__unicode__", "timestamp", "updated"]
# form = SignUpForm
# class Meta:
# 	model = SignUp


admin.site.register(SignUp, SignUpAdmin)
