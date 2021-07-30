from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import TwitterUserModel
from twitteruser.forms import TwitterUserCreationForm


# Register your models here.
class TwitterUserAdmin(UserAdmin):
    model = TwitterUserModel
    add_form = TwitterUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User Info:', {
                'fields': (
                    'display_name',
                    'friends'
                )
            }
        )
    )


admin.site.register(TwitterUserModel, TwitterUserAdmin)


