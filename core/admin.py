from django.contrib import admin

from core.models import Restaurant, Vote, IndividualVote


# Register your models here.
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Restaurant._meta.fields]
    model = Restaurant


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vote._meta.fields]
    model = Restaurant


@admin.register(IndividualVote)
class IndividualVoteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in IndividualVote._meta.fields]
    model = IndividualVote
