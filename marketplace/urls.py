from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
	#path('market/', include('market.urls')), # nancy: index page 
    #path('', include('market.urls')),
    # Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    path('users/', include('users.urls')), #new
    path('users/', include('django.contrib.auth.urls')), #new
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


