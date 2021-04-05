from django.urls import path
from mysite import views
from django.contrib.auth.views import LogoutView

""" 
sitemap

app_name='*'
path(... , name='**')

sitemaps.py
return("*:**")
"""
app_name = 'mysite'

    
urlpatterns =[
    path('', views.index, name='home'),

    path('login/', views.Login.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', views.signup),
    path('mypage/', views.MypageView.as_view()),
    path('contact/', views.ContactView.as_view()),
    # pay.html のaction が /pay ならurlsは pay、 /pay/ ならpay/
    path('pay', views.PayView.as_view()),

    path('ping/', views.ping),
]