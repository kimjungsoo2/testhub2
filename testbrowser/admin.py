from django.contrib import admin
from testbrowser.models import Primarydomain, Secondarydomain, Component, TestExecution, Testcase

# Register your models here.
admin.site.register(Primarydomain)
admin.site.register(Secondarydomain)
admin.site.register(Component)
admin.site.register(TestExecution)
admin.site.register(Testcase)