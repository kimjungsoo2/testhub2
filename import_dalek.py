#!/usr/bin/env python
import os, datetime

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testhub2.settings')
    from populate_dalek import PopulateDalek
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    #TestExecution.objects.all().delete()
    #quit()
    print "\nRUN TIME:", datetime.datetime.now(), "\n"
    pop = PopulateDalek()
    pop.populate_testcases()
    pop.populate_testexecutions()