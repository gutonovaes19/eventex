from django.contrib import admin
from eventex.core.models import Speaker
from django.utils.html import format_html #modificado via forum


class SpeakerModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name','photo_img', 'website_link']

    def website_link(self,obj):
        #modificado via forun
        return format_html('<a href="{0}">{0}</a>', obj.website)
    website_link.allow_tags = True
    website_link.short_description = 'website'

    def photo_img(self, obj):
        return format_html('<img width="32px" src="{0}" />', obj.photo)
    photo_img.allow_tags = True
    photo_img.short_description = 'foto'

admin.site.register(Speaker, SpeakerModelAdmin)
