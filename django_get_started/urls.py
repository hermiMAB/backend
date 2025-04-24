from datetime import datetime
from django.urls import path, re_path
from app import views
from app.forms import BootstrapAuthenticationForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    
    path('login/', auth_views.LoginView.as_view(
        template_name='app/login.html',
        authentication_form=BootstrapAuthenticationForm,
        extra_context={
            'title': 'Log in',
            'year': datetime.now().year,
        }),
        name='login'
    ),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'),
        name='logout'
    ),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # path('admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    # path('admin/', admin.site.urls),
]
