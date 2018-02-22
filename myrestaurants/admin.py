# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.contrib import admin

# Register your models here.
from django.contrib import admin
import models

admin.site.register(models.Restaurant)
admin.site.register(models.Dish)
admin.site.register(models.RestaurantReview)
