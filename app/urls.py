from django.urls import path
from . import views
from .views import CategoryView , ProductDetail,CategoryTitle,CustomerRegistrationView,ProfileView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view 
from .forms import LoginForm,MyPasswordResetForm,MyPasswordChangeForm
urlpatterns = [
    path("", views.home),
    path("about/", views.about,name="about"),
    path("contact/", views.contact,name="contact"),
    path("category/<slug:val>/", CategoryView.as_view(), name="category"),
    path("category-name/<val>/", CategoryTitle.as_view(), name="category-name"),
    path("product-detail/<int:pk>/", ProductDetail.as_view(), name="product-detail"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("address/", views.address, name="address"),
    path("updateAddress/<int:pk>", views.UpdateAddress.as_view(), name="updateAddress"),
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"),
    path("cart/", views.show_cart, name="showcart"),
    path("checkout/", views.checkout.as_view(), name="checkout"),
    path("pluscart/", views.plus_cart),
    path("minuscart/", views.minus_cart),
    path("removecart/", views.remove_cart),
    #login authentication
    path("registration/", CustomerRegistrationView.as_view(), name="customerregistration"),

    
    path("accounts/login/", auth_view.LoginView.as_view(template_name='app/login.html'
    ,authentication_form=LoginForm), name="login"),
    
    path("password-reset/", auth_view.PasswordResetView.as_view(template_name='app/password_reset.html'
    ,form_class=MyPasswordResetForm), name="password_reset"),
    
    path("passwordchange/", auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html'
    ,form_class=MyPasswordChangeForm,success_url='/passwordchangedone') ,name="passwordchange"),
    
    path("passwordchangedone/", auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html')
    ,name="passwordchangedone"),
    
    path("logout/", auth_view.LogoutView.as_view(next_page='login'), name="logout"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)