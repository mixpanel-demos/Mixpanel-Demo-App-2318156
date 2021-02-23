from django.conf import settings
def settings_context_processor(request):
   return {
       'SITE_NAME': settings.SITE_NAME,
       'SITE_DOMAIN': settings.SITE_DOMAIN,
       'SITE_URL': settings.SITE_URL,
       'MIXPANEL_PROJECT_TOKEN': settings.MIXPANEL_PROJECT_TOKEN,
       'MIXPANEL_PROJECT_ID': settings.MIXPANEL_PROJECT_ID,
       'MIXPANEL_ADMIN_USERNAME': settings.MIXPANEL_ADMIN_USERNAME,
       'MIXPANEL_ADMIN_PASSWORD': settings.MIXPANEL_ADMIN_PASSWORD,
   }
