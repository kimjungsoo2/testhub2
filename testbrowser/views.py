from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from testbrowser.models import Primarydomain, Secondarydomain, Component, Testcase, TestExecution
from dalekapis import DalekAPI, json, itemgetter
import collections

# Create your views here.

def decode_url(url):
    return url.replace('_', ' ')

def encode_url(url):
    return url.replace(' ', '_')

def list_domains(request):
    context = RequestContext(request)
    context_dict = {}
    
    # get all primary domains
    p = Primarydomain.objects.all().order_by('name')
    
    # get all secondary domains
    s = Secondarydomain.objects.filter(primary=p[0]).order_by('name')
    
    context_dict = {
        'primaries': p,
        'secondaries': s
    }
    
    #return render_to_response('testbrowser/pri_domain_list.html', context_dict, context)
    return render_to_response('testbrowser/nav_menu.html', context_dict, context)

def list_secondary_domains(request):
    context = RequestContext(request)
    
    primary_domain = None
    secondary_domains = None
    secondaries = []
    
    # get selected primary domain text
    if request.method == 'GET':
        domain_name = request.GET['sel_domain']
        p = Primarydomain.objects.get(name=domain_name)
        
        secondary_domains = Secondarydomain.objects.filter(primary=p).order_by('name')
        
        for s in secondary_domains:
            secondaries.append({
                'name': str(s),
                'url': encode_url(str(s))
            })
        
    return render_to_response(
        'testbrowser/sec_domain_list.html',
        {
            'secondaries': secondaries
        },
        context
    )

def list_testcases(request):
    context = RequestContext(request)
    dalek = DalekAPI()
    
    testcases = []
    
    filter_dict = {
        'reglevel': [],
        'priority': [],
        'requirement': [],
        'component': [],
        'secondary_domain': [],
        'labels': []
    }
    
    if request.method == 'GET':
        primary = request.GET['primary'].strip()
        
    #tc_dict = dict((item.Key, item) for item in Testcase.objects.filter(Primary_domain_name=primary).order_by('-Num').reverse())

    for item in Testcase.objects.filter(Primary_domain_name=primary).order_by('-Num').reverse():
        # build filter dictionary
        add_value_to_dict(filter_dict, 'reglevel', item.Regression_Level)
        add_value_to_dict(filter_dict, 'priority', item.Priority)
        
        if item.Requirements_Traceability:
            for req in item.Requirements_Traceability.split(','):
                add_value_to_dict(filter_dict, 'requirement', req)
                
        if item.Components:
            for c in item.Components.split(','):
                add_value_to_dict(filter_dict, 'component', c)
                
        if item.Labels:
            for c in item.Labels.split(' '):
                # check for the prefix type and feature
                if c.startswith('FTR-'):
                    add_value_to_dict(filter_dict, 'feature', c.replace('FTR-', ''))
                elif c.startswith('TYPE-'):
                    add_value_to_dict(filter_dict, 'test_type', c.replace('TYPE-', ''))
                else:
                    add_value_to_dict(filter_dict, 'labels', c)
                
        if item.Secondary_domain_name:
            for secondary in item.Secondary_domain_name.split(','):
                add_value_to_dict(filter_dict, 'secondary_domain', secondary)
                
        # add test execution history
        test_report = {}
        test_history = []
        test_executions = TestExecution.objects.filter(Test_Case_ID=item.Key).order_by('-Updated')
        test_results = TestExecution.objects.filter(Test_Case_ID=item.Key).values('Test_Results').annotate(dcount=Count('Test_Results'))
        
        for r in test_results:
            test_report[r['Test_Results']] = "{:.0%}".format(float(int(r['dcount'])) / float(len(test_executions)))
        
        for te in test_executions:
            te_dict = {
                'Test_Results': str(te.Test_Results),
                'Updated': str(te.Updated),
                'Test_Plan_CR': te.Test_Plan_CR,
                'Tester': te.Assignee,
                'Remote_Defect_CR': te.Remote_Defect_CR,
                'Key': te.Key
            }
            
            test_history.append(te_dict)
        
        testcases.append({
            'ID': item.Num,
            'Key': item.Key,
            'Summary': item.Summary,
            'Regression_Level': item.Regression_Level,
            'Priority': item.Priority,
            'Requirement': item.Requirements_Traceability,
            'Components': item.Components,
            'Secondary_domain_name': item.Secondary_domain_name,
            'TestHistory': test_history,
            'TestReport': test_report,
            'Labels': item.Labels
        })
        
    # sorting the list of filters
    filter_dict['reglevel'].sort()
    filter_dict['priority'].sort()
    filter_dict['requirement'].sort()
    filter_dict['component'].sort()
    filter_dict['secondary_domain'].sort()
    filter_dict['labels'].sort()
    
    if filter_dict.has_key('feature'):
        filter_dict['feature'].sort()
        
    if filter_dict.has_key('test_type'):
        filter_dict['test_type'].sort()
    
    return render_to_response(
        'testbrowser/testcase_list.html',
        {
            'primary': primary,
            'testcases': testcases,
            'filters': filter_dict
        },
        context
    )

def add_value_to_dict(dictionary, key, value):
    try:
        s = set(dictionary[key])
        if not value in s:
            dictionary[key].append(value)
    except KeyError:
        dictionary[key] = [value]


def list_testplans(request):
    context = RequestContext(request)
    dalek = DalekAPI()
    
    testplans = []
    secondaries = []
    
    if request.method == 'GET':
        primary = request.GET['primary'].strip()
        #secondary = request.GET['secondary'].strip()
        p = Primarydomain.objects.get(name=primary)
        secondary_domains = Secondarydomain.objects.filter(primary=p).order_by('name')
        
    if secondary_domains:
        for s in secondary_domains:
            secondaries.append({
                'name': str(s),
                'url': encode_url(str(s))
            })
        
    # query not closed test plans
    where = "project = 10700 and issuetype = 7 and not (issuestatus = 6 and resolution = 8)"
    fields = ['TestCases In TestPlan', 'Primary domain', 'Secondary domain', 'Primary Software']
    result = dalek.query(where, fields)
    resultjson = json.loads(result)
    
    tc_dict = dict((item.Key, item) for item in Testcase.objects.filter(Primary_domain_name=primary))
    
    for tp in sorted(resultjson, key=lambda k: int(k['Key'][k['Key'].index('-') + 1:])):
        if tp['Primary domain'] == primary:
            testcases = []
        
            # get test executions by each test plan
            te_dict = dict((item.Test_Case_ID, item) for item in TestExecution.objects.filter(Test_Plan_CR=tp['Key']))
            
            if tp['TestCases In TestPlan']:
                for tc in tp['TestCases In TestPlan'].split(','):
                    testcase = {}
                    
                    if tc_dict.has_key(tc):
                        testcase['ID'] = tc_dict[tc].Num
                        testcase['Key'] = tc_dict[tc].Key
                        testcase['Summary'] = tc_dict[tc].Summary
                        testcase['Regression_Level'] = tc_dict[tc].Regression_Level
                        testcase['Priority'] = tc_dict[tc].Priority
                        testcase['Requirement'] = tc_dict[tc].Requirements_Traceability
                        testcase['Components'] = tc_dict[tc].Components
                        testcase['Secondary_domain'] = tc_dict[tc].Secondary_domain_name
                        testcase['Labels'] = tc_dict[tc].Labels
                        
                        if te_dict.has_key(tc):
                            testcase['Result'] = te_dict[tc].Test_Results
                            testcase['Result_Key'] = te_dict[tc].Key
                            testcase['Remote_Defect_CR'] = te_dict[tc].Remote_Defect_CR
                    else:
                        testcase['ID'] = int(tc.split('-')[1])
                        testcase['Key'] = tc 
                        
                    testcases.append(testcase)
            
            testplans.append(
                {
                    'Primary_Software': tp['Primary Software'].split('\r\n'),
                    'Resolution': tp['Resolution'],
                    'Priority': tp['Priority'],
                    'Secondary_domain': tp['Secondary domain'],
                    'Status': tp['Status'],
                    'Updated': tp['Updated'],
                    'Primary_domain': tp['Primary domain'],
                    'Description': tp['Description'],
                    'Key': tp['Key'],
                    'Created': tp['Created'],
                    'Summary': tp['Summary'],
                    'TestCases_In_TestPlan': sorted(testcases, key = itemgetter('ID'))
                }
            )
        
    
    return render_to_response(
        'testbrowser/testplan_list.html',
        {
            'primary': primary,
            'secondaries': secondaries,
            'testplans': testplans
        },
        context
    )

def generate_report(request, key):
#def generate_report(request):
    '''
    if request.method == 'GET':
        key = request.GET['key'].strip()
    '''
    
    test_executions = TestExecution.objects.filter(Test_Plan_CR=key).order_by('-Updated')
    test_results = list(TestExecution.objects.filter(Test_Plan_CR=key).values('Test_Results').annotate(dcount=Count('Test_Results')))
    defects = list(TestExecution.objects.filter(Test_Plan_CR=key).values('Remote_Defect_CR').annotate(dcount=Count('Remote_Defect_CR')))
    
    # get test plan summary
    where = "project = 10700 and issuenum = " + key[key.index('-')+1:]
    fields = []
    result = DalekAPI().query(where, fields)
    json_result = json.loads(result)
    
    #for d in defects:
    #    d.update((k, 'None') for k, v in d.iteritems() if v == None)
        
    test_summary = {}
    ncount = len(test_executions)

    for r in test_results:
        if r['Test_Results']:
            test_summary[r['Test_Results']] = r['dcount']
            ncount = ncount - int(r['dcount'])
        else:
            test_summary['None'] = 0
            
    test_summary['None'] = ncount
    
    dict_components = {}
    dict_labels = {}
    
    # components list
    for te in test_executions:
        if te.Components:
            components = te.Components.split(',')
        else:
            components = ['None']
            
        if te.Labels:
            labels = te.Labels.split(',')
        else:
            labels = ['None']

        for c in components:
            try:
                dict_components[c].append(te.Key)
            except KeyError:
                dict_components[c] = [te.Key]
                
        for l in labels:
            try:
                dict_labels[l].append(te.Key)
            except KeyError:
                dict_labels[l] = [te.Key]
    
    return render_to_response(
        'testbrowser/testreport.html', {
            'key': key,
            'testplansummary': json_result[0]['Summary'],
            'testexecutions': test_executions,
            'testsummary': json.dumps(test_summary),
            'totalexecutions': len(test_executions),
            'defects': json.dumps(defects),
            'components': json.dumps(dict_components),
            'category': json.dumps(dict_labels)
        }
    )
    
    '''
    test_results.append({
        'dcount': ncount,
        'Test_Results': 'None'
    })
    
    test_results.insert(0, {
        'dcount': len(test_executions),
        'Test_Results': 'Total'
    })
    
    test_results[:] = [d for d in test_results if d.get('Test_Results') != None]

    return HttpResponse(json.dumps(response_data), content_type="application/json")
    '''
