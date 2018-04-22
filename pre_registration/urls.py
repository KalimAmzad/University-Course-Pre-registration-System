from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^student/', include('student.urls')),
    url(r'^teacher/', include('teacher.urls')),
    url(r'^result/', include('result.urls')),
    url(r'^section/', include('section.urls')),
    # python-social-auth
    #url('social-auth/', include('social.apps.django_app.urls', namespace='social')),
]
admin.site.site_title = "Pre Registration System"
admin.site.site_header = 'IIUC Pre Registration System'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
