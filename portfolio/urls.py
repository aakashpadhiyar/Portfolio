from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import job.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', job.views.home, name='home'),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
