from django.contrib import admin
from .models import Header,Tournament,Winner,User,game

# Custom admin class for User model

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_lastname', 'user_email', 'wallet_balance')  # Display fields in the admin list view
    
    def get_readonly_fields(self, request, obj=None):
        """Set `wallet_balance` as readonly for non-superusers."""
        if not request.user.is_superuser:
            return self.readonly_fields + ('wallet_balance',)  # Add wallet_balance to readonly
        return self.readonly_fields  # No changes for superusers

admin.site.register(User,UserAdmin)
admin.site.register(Header)
admin.site.register(Tournament)
admin.site.register(Winner)
# admin.site.register(User)
admin.site.register(game)
