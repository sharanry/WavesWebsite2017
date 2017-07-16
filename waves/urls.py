"""waves URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from spinoff.views import spinoffreg
from smtf.views import smtfreg
from poetryslam.views import inversereg
from home.views import home
from csr.views import csr, csrreg

# for static
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^spinoff/reg', spinoffreg.as_view(), name='spinoffreg'),
    url(r'^smtf/reg', smtfreg.as_view(), name='smtfreg'),
    url(r'^inverse/reg', inversereg.as_view(), name='inversereg'),
    url(r'^csr/reg', csrreg.as_view(), name='csrreg'),
    url(r'^csr', csr.as_view(), name='csr'),
    url(r'^', home.as_view(), name='home'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
