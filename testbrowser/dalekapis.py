#!/usr/bin/env python

import sys, urllib2
import json
from operator import itemgetter
from datetime import datetime

class DalekAPI(object):
    # This class handles with requesting to Dalek through web jsql.
    # jsql_data: jsql data string to be passed to curl command
    
    jsonout = ''
    userdata = 'cstaccess'
    #userdata = 'appcst'
    
    def __init__(self):
        self.https_request = 'http://jsql.mot.com/rest/query/cstaccess/cstaccess'
        #self.https_request = 'https://rsgw.motorola.com/API_Bug2Go_JSQL_Query-Prod/rest/query/appcst:@testhub'
        
    # if you don't have any custom fields to retrieve, pass []
    def query(self, where_clause, custom_fields):
        
        # make jsql string
        if len(custom_fields) > 0:
            jsql = "{\"real_time\":1, \"jira\":\"dalek\", \"where\":\"" + where_clause + "\", \"custom_fields\":\"" + ",".join(custom_fields) + "\"}"
        else:
            jsql = "{\"real_time\":1, \"jira\":\"dalek\", \"where\":\"" + where_clause + "\"}"
            
        # make the request and return the results
        return self.request(jsql)
    
    def request(self, jsql_str):
        # create a new Urllib2 request object
        req = urllib2.Request(self.https_request)
        
        # add any additional headers
        req.add_header('Accept', 'application/json')
        req.add_header("Content-type", "application/x-www-form-urlencoded")
        
        # add authentication header, required
        req.add_header('Authorization', self.userdata)
        
        # add data with jsql string
        req.add_data(jsql_str)
            
        # make the request and return the results
        res = urllib2.urlopen(req)
        self.jsonout = res.read()
        
        # close the result
        res.close()
        
        return self.jsonout
    
    def create_tc_dictionary_by_group(self, group):
        # query all SME Approved test cases and make test case dictionary
        where = "project = 10700 and issuetype = 6 and issuestatus = 10006"
        fields = ['Regression Level', 'Requirements Traceability', 'Secondary domain', 'Primary domain']
        result = self.query(where, fields)
        list_result = json.loads(result)
        
        dictionary = {}
        
        for item in list_result:
            
            # we need to separate the group names ex. Component/s
            if item[group] != None:
                if len(item[group]) == 0:
                    item[group] = 'None'
                
                if group == 'Labels':
                    group_list = item[group].split(' ')
                else:
                    group_list = item[group].split(",")
            else:
                group_list = [item[group]]
            
            for g_item in group_list:
                if g_item in dictionary.keys():
                    dictionary[g_item].append(item)
                else:
                    dictionary[g_item] = [item]
    
        return dictionary
    
    
    def create_tc_dictionary(self):
        # query all SME Approved test cases and make test case dictionary
        #where = "project = 10700 and issuetype = 6 and issuestatus = 10006"
        where = "project = 10700 and issuetype = 6"
        fields = ['Regression Level', 'Requirements Traceability', 'Secondary domain', 'Primary domain']
        result = self.query(where, fields)
        list_result = json.loads(result)
        
        dictionary = {}
        
        for item in list_result:
            dictionary[item['Key']] = item
    
        return dictionary
    
    def create_test_history_dictionary(self, groupby):
        # query not cancelled test executions and make the dictionary by test case
        where = "project = 10700 and issuetype = 9 and not (issuestatus = 6 and resolution = 8)"
        fields = ['Test Plan CR', 'Test Case ID', 'Test Results', 'Remote Defect CR']
        result = self.query(where, fields)
        list_result = json.loads(result)
        
        dictionary = {}
        
        for item in list_result:
            if item[groupby] in dictionary.keys():
                dictionary[item[groupby]].append(item)
            else:
                dictionary[item[groupby]] = [item]
            
        return dictionary
    
    def get_test_executions(self, testplan_key):
        te_list = self.create_test_history_dictionary('Test Plan CR')
        try:
            return te_list[testplan_key]
        except KeyError:
            return []
    
    def get_testplan_detail(self, key):
        # make custom fields to retrieve
        custom_fields = [
            'End Date',
            'HW Revision',
            'Primary Software',
            'Primary purpose',
            'Start Date',
            'TestCases In TestPlan'
        ]
        
        # query not cancelled test executions and make the dictionary by test case
        jsql = "{\"real_time\":1, \"jira\":\"dalek\", \"issue_keys\":\"" + key + "\", \"custom_fields\":\"" + ",".join(custom_fields) + "\"}"
        result = self.request(jsql)
        dictionary = json.loads(result)
            
        return dictionary[0]
    
    """
    def create_te_dictionary(self, key1, key2):
        # query not cancelled test executions and make the dictionary
        query = "project = 10700 and issuetype = 9 and not (issuestatus = 6 and resolution = 8)"
        fields = ['Test Plan CR', 'Test Case ID', 'Test Results']
        result = self.request(query, fields)
        list_result = json.loads(result)
        
        dictionary = {}
        
        for item in list_result:
            if item[key1] in dictionary.keys():
                exists = 0
                
                # check if sub dictionary contains the key2
                for sub_dictionary in dictionary[item[key1]]:
                    if item[key2] in sub_dictionary.keys():
                        sub_dictionary[item[key2]].append(item)
                        exists = 1
                        break
                    
                # if not found, add new sub_dictionary
                if exists == 0:
                    dictionary[item[key1]].append({item[key2]: [item]})
            else:
                dictionary[item[key1]] = [{item[key2]: [item]}]
        
        return dictionary
        """