from django.contrib import admin
from django.urls import path, include
from drf_yasg import views, openapi
from rest_framework import permissions


schema_view = views.get_schema_view(
    openapi.Info(
        title='Contacts  API',
        default_version='v1',
        description='Test description',
        terms_of_service='https://google.com/policies/terms',
        contact=openapi.Contact(
            email='godfredderi47@gmail.com',
        ),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/auth/', include('accounts.urls')),
    path('api/contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
