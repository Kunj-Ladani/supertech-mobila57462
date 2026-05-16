from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

# =========================
# ADDED LINE
# =========================
from django.contrib import admin
# =========================
   
    
# Url Set
  
urlpatterns = [
    # =========================
    # ADDED LINE
    # =========================
    path('admin/', admin.site.urls),
    # =========================

    path('adminapp/', include('adminapp.urls')),
    path('', include('userapp.urls')),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# =========================
# ADDED FOR STATIC FILES (CSS, JS)
# =========================
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# =========================