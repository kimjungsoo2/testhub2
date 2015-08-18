#!/usr/bin/env python
import sys, traceback
from datetime import datetime
from testbrowser.dalekapis import DalekAPI, json
from testbrowser.models import Testcase, Primarydomain, Secondarydomain, TestExecution, Testplan

class PopulateDalek(object):

    def __init__(self):
        pass    
    
    def populate_testexecutions(self):
        print "Starting test executions population script..."
        
        #where = "project = 10700 and issuetype = 9 and not (issuestatus = 6 and resolution = 8)"
        where = "project = 10700 and issuetype = 9"
        fields = ['Test Plan CR', 'Test Case ID', 'Test Results', 'Remote Defect CR']
        result = DalekAPI().query(where, fields)
        json_result = json.loads(result)
        
        count = 1
        for item in json_result:
            if item['Test Plan CR'] == None:
                item['Test Plan CR'] = 'None';
                
            try:
                tp = Testplan.objects.get_or_create(name=item['Test Plan CR'])[0]
                self.add_testexecution(testplan=tp, te_dict=item)
            except Exception:
                print item
                traceback.print_exc(file=sys.stdout)
                quit()
                
            sys.stdout.write('\r')
            sys.stdout.write("Adding test executions..." + "{0:.0f}".format(float(count * 100 / len(json_result))) + '% - ' + str(count) + '/' + str(len(json_result)))
            sys.stdout.flush()
            count = count + 1
            
        print '\n'
        
        '''    
        print "Printing test executions"
        for tp in Testplan.objects.all():
            print "Test Plan -", tp
            for te in TestExecution.objects.filter(Test_Plan_Key=tp):
                print te.Key, te.Summary
        '''    
    
    
    def populate_testcases(self):
        print "Starting test cases population script..."
        
        where = "project = 10700 and issuetype = 6"
        fields = ['Regression Level', 'Requirements Traceability', 'Secondary domain', 'Primary domain']
        result = DalekAPI().query(where, fields)
        json_result = json.loads(result)
            
        count = 1
        for item in json_result:
            p = Primarydomain.objects.get_or_create(name=item['Primary domain'])[0]
            self.add_testcase(primary=p, tc_dict=item)
            
            sys.stdout.write('\r')
            sys.stdout.write("Adding test cases..." + "{0:.0f}".format(float(count * 100 / len(json_result))) + '% - ' + str(count) + '/' + str(len(json_result)))
            sys.stdout.flush()
            count = count + 1
            
        print '\n'
            
        """   
        print "Printing test cases..."
        for p in Primarydomain.objects.all():
            print p
            for t in Testcase.objects.filter(Primary_domain_key=p):
                print t.Key, t.Summary
        """
                
    def add_testexecution(self, testplan, te_dict):
        try:
            te = TestExecution.objects.get_or_create(Key = te_dict['Key'], Test_Plan_Key = testplan)[0]
            
            te.Test_Case_ID = te_dict['Test Case ID']
            te.Resolution_ID = te_dict['Resolution ID']
            te.Due = te_dict['Due']
            te.Priority = te_dict['Priority']
            te.Type = te_dict['Type']
            te.Status = te_dict['Status']
            te.Updated = datetime.strptime(te_dict['Updated'], "%Y-%m-%d %H:%M:%S") if te_dict['Updated'] else te_dict['Updated']
            #te.Component_ID = te_dict['Component ID']
            te.Description = te_dict['Description']
            te.Reporter = te_dict['Reporter']
            te.Project_Key = te_dict['Project Key']
            te.Status_ID = te_dict['Status ID']
            te.Test_Plan_CR = te_dict['Test Plan CR']
            te.Test_Plan_Key = testplan
            #Key = te_dict['Key'],
            te.Project_ID = te_dict['Project ID']
            te.Created = datetime.strptime(te_dict['Created'], "%Y-%m-%d %H:%M:%S") if te_dict['Created'] else te_dict['Created']
            te.Remote_Defect_CR = te_dict['Remote Defect CR']
            te.Summary = te_dict['Summary']
            te.TypeID = te_dict['Type ID']
            te.Resolution = te_dict['Resolution']
            te.Project = te_dict['Project']
            te.Labels = te_dict['Labels']
            te.Assignee = te_dict['Assignee']
            te.Components = te_dict['Component/s']
            te.Test_Results = te_dict['Test Results']
            
            te.save()
        except Exception:
            print te_dict
            traceback.print_exc(file=sys.stdout)
            quit()
    
        
    def add_testcase(self, primary, tc_dict):
        try:
            t = Testcase.objects.get_or_create(Key = tc_dict['Key'], Primary_domain_key=primary)[0]
            
            t.Resolution_ID = tc_dict['Resolution ID']
            t.Due = datetime.strptime(tc_dict['Due'], "%Y-%m-%d %H:%M:%S") if tc_dict['Due'] else tc_dict['Due']
            t.Priority = tc_dict['Priority']
            t.Type = tc_dict['Type']
            t.Secondary_domain_name = tc_dict['Secondary domain']
            t.Status = tc_dict['Status']
            t.Updated = datetime.strptime(tc_dict['Updated'], "%Y-%m-%d %H:%M:%S") if tc_dict['Updated'] else tc_dict['Updated']
            t.Primary_domain_name = tc_dict['Primary domain']
            t.Regression_Level = tc_dict['Regression Level']
            t.Reporter = tc_dict['Reporter']
            t.Project_Key = tc_dict['Project Key']
            t.Status_ID = tc_dict['Status ID']
            t.Num = int(tc_dict['Key'].split('-')[1])
            t.Project_ID = tc_dict['Project ID']
            t.Requirements_Traceability = tc_dict['Requirements Traceability']
            t.Created = datetime.strptime(tc_dict['Created'], "%Y-%m-%d %H:%M:%S") if tc_dict['Created'] else tc_dict['Created']
            t.Summary = tc_dict['Summary']
            t.Type_ID = tc_dict['Type ID']
            t.Component_ID = tc_dict['Component ID']
            t.Resolution = tc_dict['Resolution']
            t.Description = tc_dict['Description']
            t.Project = tc_dict['Project']
            t.Labels = tc_dict['Labels']
            t.Assignee = tc_dict['Assignee']
            t.Components = tc_dict['Component/s']
            
            t.save()
            
        except Exception:
            print tc_dict
            print Testcase.objects.filter(Key=tc_dict['Key'])
            traceback.print_exc(file=sys.stdout)
            quit()
        
        '''
        try:
            Testcase.objects.update_or_create(
                Resolution_ID = tc_dict['Resolution ID'],
                Due = datetime.strptime(tc_dict['Due'], "%Y-%m-%d %H:%M:%S") if tc_dict['Due'] else tc_dict['Due'],
                Priority = tc_dict['Priority'],
                Type = tc_dict['Type'],
                Secondary_domain_name = tc_dict['Secondary domain'],
                Status = tc_dict['Status'],
                Updated = datetime.strptime(tc_dict['Updated'], "%Y-%m-%d %H:%M:%S") if tc_dict['Updated'] else tc_dict['Updated'],
                Primary_domain_name = tc_dict['Primary domain'],
                Primary_domain_key = primary,
                Regression_Level = tc_dict['Regression Level'],
                Reporter = tc_dict['Reporter'],
                Project_Key = tc_dict['Project Key'],
                Status_ID = tc_dict['Status ID'],
                Key = tc_dict['Key'],
                Num = int(tc_dict['Key'].split('-')[1]),
                Project_ID = tc_dict['Project ID'],
                Requirements_Traceability = tc_dict['Requirements Traceability'],
                Created = datetime.strptime(tc_dict['Created'], "%Y-%m-%d %H:%M:%S") if tc_dict['Created'] else tc_dict['Created'],
                Summary = tc_dict['Summary'],
                Type_ID = tc_dict['Type ID'],
                Component_ID = tc_dict['Component ID'],
                Resolution = tc_dict['Resolution'],
                Description = tc_dict['Description'],
                Project = tc_dict['Project'],
                Labels = tc_dict['Labels'],
                Assignee = tc_dict['Assignee'],
                Components = tc_dict['Component/s']
            )[0]
        except Exception:
            print tc_dict
            print Testcase.objects.filter(Key=tc_dict['Key'])
            traceback.print_exc(file=sys.stdout)
            quit()
        '''
