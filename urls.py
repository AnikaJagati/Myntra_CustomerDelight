from django.urls import path , include
from . import views
from trial1 import settings
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
   # path('', include('part1.urls'))
   path('',views.index,name="index"),
  # path('upload',views.model_form_upload,name="showimg"),
   #path('add',views.add,name="add")
   path('up', views.simple_upload, name = 'create'),
   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)