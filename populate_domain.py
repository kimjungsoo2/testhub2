#!/usr/bin/env python
import os

def populate():
    
    p = add_primary('BAP Nuke')
    p = add_primary('Big Red Button')
    p = add_primary('Carrier')
    add_secondary(primary=p, name='E2E')
    add_secondary(primary=p, name='Network')
    p = add_primary('CAS')
    add_secondary(primary=p, name='CAS Server')
    p = add_primary('Core Services')
    add_secondary(primary=p, name='CCE-DeviceProvisioning')
    add_secondary(primary=p, name='SSO')
    add_secondary(primary=p, name='AccessIdentifyPortal')
    p = add_primary('CSP')
    add_secondary(primary=p, name='CSP Service')
    add_secondary(primary=p, name='CSP Client SDK')
    p = add_primary('Data Cloud')
    add_secondary(primary=p, name='Checkin')
    add_secondary(primary=p, name='Lotus')
    add_secondary(primary=p, name='Luna')
    p = add_primary('Droid Zap')
    add_secondary(primary=p, name='GCSP Client')
    add_secondary(primary=p, name='GCSP Backend')
    p = add_primary('GdrivePromo')
    add_secondary(primary=p, name='PromotionalOffer')
    p = add_primary('Motocare')
    add_secondary(primary=p, name='Client')
    p = add_primary('Notification')
    add_secondary(primary=p, name='Client')
    p = add_primary('OTA')
    add_secondary(primary=p, name='CDS Portal')
    add_secondary(primary=p, name='SUP Portal')
    add_secondary(primary=p, name='SSOTA Portal')
    p = add_primary('OTA-Client')
    add_secondary(primary=p, name='8226-Recovery')
    add_secondary(primary=p, name='Dual-sim')
    add_secondary(primary=p, name='10 sec timer')
    add_secondary(primary=p, name='Finger prints')
    add_secondary(primary=p, name='Autenticated download')
    add_secondary(primary=p, name='Silent-APK')
    add_secondary(primary=p, name='All')
    add_secondary(primary=p, name='Verizon')
    add_secondary(primary=p, name='Http error codes')
    add_secondary(primary=p, name='Low_battery')
    add_secondary(primary=p, name='cds-migration')
    add_secondary(primary=p, name='Setup-intiated')
    add_secondary(primary=p, name='Silent-OTA')
    add_secondary(primary=p, name='ROW')
    add_secondary(primary=p, name='ROW-UI Template')
    add_secondary(primary=p, name='VZW-UI Template')
    add_secondary(primary=p, name='VZW')
    add_secondary(primary=p, name='Verification_Methods')
    add_secondary(primary=p, name='UI-screens')
    add_secondary(primary=p, name='UI-Non-VZW screens')
    add_secondary(primary=p, name='UI-VZW screens')
    add_secondary(primary=p, name='AT&T port')
    add_secondary(primary=p, name='AT&T')
    add_secondary(primary=p, name='Exploratory')
    add_secondary(primary=p, name='Extra-space')
    add_secondary(primary=p, name='AT&T FOTA')
    add_secondary(primary=p, name='Middleware-Update')
    add_secondary(primary=p, name='Multi-user profile')
    add_secondary(primary=p, name='VZW-Zero-rated')
    add_secondary(primary=p, name='WI-FI_Discovery')
    add_secondary(primary=p, name='Download to data')
    add_secondary(primary=p, name='AT&T 30 sec timer')
    add_secondary(primary=p, name='Rich text')
    add_secondary(primary=p, name='Recovery')
    add_secondary(primary=p, name='Polling-Enhancements')
    add_secondary(primary=p, name='Ota-Cancel')
    add_secondary(primary=p, name='Motodrop')
    add_secondary(primary=p, name='Package Creation')
    add_secondary(primary=p, name='Rooted')
    add_secondary(primary=p, name='Instrumentation')
    add_secondary(primary=p, name='KPI')
    add_secondary(primary=p, name='Sdcard')
    add_secondary(primary=p, name='Network Info')
    add_secondary(primary=p, name='Sync polling for Jbrel1 only')
    add_secondary(primary=p, name='Sync polling for Jbrel2 only')
    add_secondary(primary=p, name='Recovery-Stress')
    p = add_primary('Tethered-Client')
    add_secondary(primary=p, name='Win-MAC')
    add_secondary(primary=p, name='All')
    add_secondary(primary=p, name='Win-MAC-Repair')
    add_secondary(primary=p, name='MDM')
    
    # Print out what we have added to the db
    for p in Primarydomain.objects.all():
        for s in Secondarydomain.objects.filter(primary=p):
                print "- {0} - {1}".format(str(p), str(s))
    
def add_primary(name):
    p = Primarydomain.objects.get_or_create(name=name)[0]
    return p

def add_secondary(primary, name):
    s = Secondarydomain.objects.get_or_create(primary=primary, name=name)[0]
    return s

def add_component(secondary, name):
    c = Component.objects.get_or_create(secondary=secondary, name=name)
    return c

if __name__ == '__main__':
    print "Starting Domain population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testhub2.settings')
    from testbrowser.models import Primarydomain, Secondarydomain, Component
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    populate()