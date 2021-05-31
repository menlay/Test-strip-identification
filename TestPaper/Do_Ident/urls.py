from . import views

from django.urls import path

urlpatterns=[ path('',views.hello),
              path('lv',views.lv),
              path('zhr',views.zhr),
              path('ipa',views.ipa),
              path('paper',views.paper),
              path('paper1', views.paper1),

              ]