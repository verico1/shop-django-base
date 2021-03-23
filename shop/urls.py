from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('account/', include('accounts.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('products/', include('products.urls')),
    path('staff/', include('staff.urls')),
    path('payment/', include('pay.urls')),
    path('payment/', include('zarinpal.urls')),
]


handler404 = 'app.views.not_found'
handler500 = 'app.views.server_error'
handler403 = 'app.views.permission_denied'
handler400 = 'app.views.bad_request'

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)