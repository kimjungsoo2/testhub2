#!/usr/bin/env python

from populate_dalek import PopulateDalek
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
#TestExecution.objects.all().delete()
#quit()
pop = PopulateDalek()
pop.populate_testcases()