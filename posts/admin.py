from django.contrib import admin

# Register your models here.
from posts.models import Post
from users.models import Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin"""
    # List of attributes that will show in the admin
    list_display = ('__str__', 'title', 'photo', 'created', 'modified')
    # Read only fields
    readonly_fields = ('created', 'modified')
    # List of editables in situ
    list_editable = ('title', 'photo')
    # Search Fields
    search_fields = (
        'profile__user__email',
        'profile__user__username',
        'profile__user__first_name',
        'profile__user__last_name',
        'title'
    )
    # Fields which cannot be filtered
    list_filter = (
        'profile__user__is_active',
        'profile__user__is_staff',
        'created',
        'modified',
    )