"""HTTP PIE commands
Command to get the access and refresh tokens:
http post http://127.0.0.1:8000/api/token/ username=hp password=admin

-To get the data with access topken-

http http://127.0.0.1:8000/api/vendors/ "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MTExMTg2LCJpYXQiOjE3MTYxMTA4ODYsImp0aSI6IjVkNmQ5YzU1NTU3OTQ4ZDhiYzQ3ZjI3MmJkNjU0ZDYyIiwidXNlcl9pZCI6Mn0.eqaVrqLHvkZxCZyI-LExts5eoP4RfIqhrMCBnHrieU8"

http POST http://127.0.0.1:8000/api/token/refresh refresh=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNjE4OTI4MywiaWF0IjoxNzE2MTAyODgzLCJqdGkiOiIxNDQ5MzRiMmI4MzQ0NTE0OTM5NGY3N2M5MDg0ZGU4OSIsInVzZXJfaWQiOjJ9.l9Hu7rA-8vYtmW4qor2CzmfmjBq-g_a74vpPltsYHUo

"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('main.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
