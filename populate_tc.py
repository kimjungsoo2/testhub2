#!/usr/bin/env python
import os

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testhub2.settings')
    from populate_dalek import PopulateDalek
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    #TestExecution.objects.all().delete()
    #quit()
    pop = PopulateDalek()    
    pop.populate_testcases()