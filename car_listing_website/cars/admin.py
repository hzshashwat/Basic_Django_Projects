from django.contrib import admin
from cars.models import Car

# Register your models here.

# admin.site.register(Car)

class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Car Information', {'fields' : ['Model', 'Brand']}),
        ('Year Information', {'fields' : ['Year']})
    ]
    # fields = ['Year','Brand','Model']
admin.site.register(Car, CarAdmin)