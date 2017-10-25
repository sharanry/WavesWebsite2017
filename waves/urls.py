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
from home.views import home, beauvista, events, carpedictum, specials, florence, underconstruction, contactus, ourteam, sponsors
from csr.views import csr, csrreg
from registration.views import reg
from events import views as EventViews

# for static
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^spinoff/reg/$', spinoffreg.as_view(), name='spinoffreg'),
    url(r'^smtf/reg/$', smtfreg.as_view(), name='smtfreg'),
    url(r'^inverse/reg/$', inversereg.as_view(), name='inversereg'),
    url(r'^reg/$', reg.as_view(), name='reg'),
    url(r'^socialcause/reg/$', csrreg.as_view(), name='csrreg'),
    url(r'^socialcause/$', csr.as_view(), name='csr'),
    url(r'^tshirt/$', EventViews.tshirt.as_view(), name='tshirt'),
    url(r'^lexomniamoot/$', EventViews.moot.as_view(), name='moot'),
    # url(r'^caricreatures/$', EventViews.caricreatures.as_view(), name='caricreatures'),
    # url(r'^doodle/$', EventViews.doodle.as_view(), name='doodle'),
    url(r'^ohsnap/$', EventViews.ohSnap.as_view(), name='ohSnap'),
    url(r'^short/$', EventViews.short.as_view(), name='short'),
    url(r'^irshad/$', EventViews.irshad.as_view(), name='irshad'),
    url(r'^events/$', events.as_view(), name='events'),
    # url(r'^carpedictum/$', EventViews.carpedictum.as_view(), name='carpedictum'),
    url(r'^beauvista/$', underconstruction.as_view(), name='beauvista'),
    url(r'^specials/$', specials.as_view(), name='specials'),
    url(r'^florence/$', florence.as_view(), name='florence'),
    url(r'^our_team/$', ourteam.as_view(), name='ourteam'),
    url(r'^sponsors/$', sponsors.as_view(), name='sponsors'),
    url(r'^contact_us/$', contactus.as_view(), name='contactus'),

# --------------------------------------------------------------------------------
    url(r'^alaap/$', EventViews.alaap.as_view(), name='alaap'),    
    url(r'^artathon/$', EventViews.artathon.as_view(), name='artathon'),    
    url(r'^blindart/$', EventViews.blindart.as_view(), name='blindart'),    
    url(r'^boow/$', EventViews.boow.as_view(), name='boow'),    
    url(r'^caricreatures/$', EventViews.caricreatures.as_view(), name='caricreatures'),    
    url(r'^contention/$', EventViews.contention.as_view(), name='contention'),    
    url(r'^corture/$', EventViews.corture.as_view(), name='corture'),    
    url(r'^culturalgauntel/$', EventViews.culturalgauntel.as_view(), name='culturalgauntel'),    
    url(r'^dancingduo/$', EventViews.dancingduo.as_view(), name='dancingduo'),    
    url(r'^doodle/$', EventViews.doodle.as_view(), name='doodle'),    
    url(r'^fashp/$', EventViews.fashp.as_view(), name='fashp'),    
    url(r'^indianrock/$', EventViews.indianrock.as_view(), name='indianrock'),    
    url(r'^inverse/$', EventViews.inverse.as_view(), name='inverse'),    
    url(r'^irshaad/$', EventViews.irshaad.as_view(), name='irshaad'),    
    url(r'^jukebox/$', EventViews.jukebox.as_view(), name='jukebox'),    
    url(r'^mela/$', EventViews.mela.as_view(), name='mela'),    
    url(r'^moot/$', EventViews.moot.as_view(), name='moot'),    
    url(r'^mrwaves/$', EventViews.mrwaves.as_view(), name='mrwaves'),
    url(r'^natyanjali/$', EventViews.natyanjali.as_view(), name='natyanjali'),
    url(r'^nukkadnatak/$', EventViews.nukkadnatak.as_view(), name='nukkadnatak'),
    url(r'^portrature/$', EventViews.portrature.as_view(), name='portrature'),
    url(r'^rangmanch/$', EventViews.rangmanch.as_view(), name='rangmanch'),
    url(r'^searock/$', EventViews.searock.as_view(), name='searock'),
    url(r'^sf/$', EventViews.sf.as_view(), name='sf'),
    url(r'^sizzle/$', EventViews.sizzle.as_view(), name='sizzle'),
    url(r'^skime/$', EventViews.skime.as_view(), name='skime'),
    url(r'^smtf/$', EventViews.smtf.as_view(), name='smtf'),
    url(r'^solonote/$', EventViews.solonote.as_view(), name='solonote'),
    url(r'^sota/$', EventViews.sota.as_view(), name='sota'),
    url(r'^spinoff/$', EventViews.spinoff.as_view(), name='spinoff'),
    url(r'^wordgames/$', EventViews.wordgames.as_view(), name='wordgames'),

# ----------------------------------------------------------------------------------
    url(r'^$', home.as_view(), name='home'),
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
