"""
URL configuration for Agri_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf 
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views as coreviews
from core.views import CustomLoginView
from farmer import views as farmer_views
from public_user import views as public_view
from django.contrib.auth import views as auth_views  
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='admin_page'),
    path('', coreviews.home, name="home"),
    path('login/', CustomLoginView.as_view(template_name="farmer/farmer_login.html"), name="login"),
    path('publiclogin/', CustomLoginView.as_view(template_name="public_user/public_login.html"), name="publiclogin"),
    path('logout/', auth_views.LogoutView.as_view(template_name="farmer/farmer_logout.html"), name='logout'),
    path('register/', farmer_views.register, name='register'),
    path('public_register/',public_view.public_registration,name='public_register'),
    path('farmerhome/',farmer_views.farmer_home,name='farmer_home'),
    path('userhome/', public_view.public_home, name='public_home'),
    path('farmer_profile/',farmer_views.farmer_profile,name='farmer_profile'),
    path('public_userprofile/',public_view.public_profile,name='userprofile'),
    path('create_product/',farmer_views.create_product,name='create_product'),
    path('farmer_products/',farmer_views.view_products,name='farmer_products'),
    path('farmer_product_update/',farmer_views.farmer_product_update,name='farmer_product_update'),
    path('product_delete/<str:product_id>/', farmer_views.product_delete, name='product_delete'),
    path('buy_now/<str:product_id>/', public_view.buy_now, name='buy_now'),
    path('secondpage_buynow/<str:product_id>/', public_view.secondpage_buynow, name='secondpage_buynow'),
    path('finalpage_buynow/<str:product_id>/<int:quantity>/', public_view.finalpage_buynow, name='finalpage_buynow'),
    path('payment/', public_view.payment_page, name='payment_page'),
    path('payment/success/', public_view.payment_success, name='payment_success'),
    path('my_orders/',public_view.my_orders,name='my_orders'),
    path('orders/',farmer_views.orders,name='orders'),
    path('update_order_status/<int:order_id>/', farmer_views.update_order_status, name='update_order_status'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

