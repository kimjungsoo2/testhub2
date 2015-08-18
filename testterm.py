#!/usr/bin/env python
import os, sys, traceback
from testbrowser.dalekapis import DalekAPI

def func():
    
    key = "CST-5005"
    where = "project = 10700 and issuenum = " + key[key.index('-')+1:]
    
    print where
    fields = []
    result = DalekAPI().query(where, fields)
    json_result = json.loads(result)
    
    print json_result[0]['Summary']

if __name__ == '__main__':
    import os
    
    print "Starting testing..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testhub2.settings')
    from testbrowser.models import Primarydomain, Secondarydomain, Component, Testcase, TestExecution
    from testbrowser.dalekapis import DalekAPI, json, itemgetter
    from testbrowser.views import add_value_to_dict
    from django.db.models import Count
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    func()