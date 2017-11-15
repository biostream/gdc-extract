#!/usr/bin/env python

import os
import sys
import json
import argparse

import requests
from pprint import pformat, pprint

URL_BASE="https://gdc-api.nci.nih.gov/v0/"


WORKFLOW_MAP = {
    "fpkm" : "HTSeq - FPKM"
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_type")
    parser.add_argument("project_id")
    parser.add_argument("output_name")
    args = parser.parse_args()
    
    query = {
        "op":"and",
        "content" : [
            {
                "op":"=",
                "content":{
                    "field":"analysis.workflow_type",
                    "value":[
                        WORKFLOW_MAP[args.data_type]
                    ]
                }
            },
            {
                "op":"=",
                "content":{
                    "field":"cases.project.project_id",
                    "value":[
                        args.project_id
                    ]
                }            
            }
        ]
    }   
    
    id_list = []
    params = {}
    params['filters'] = json.dumps(query)
    while 'size' not in params or data['pagination']['page'] < data['pagination']['pages']:
        params['size'] = 1000
        req = requests.get(URL_BASE + "files", params=params)
        data = req.json()['data']
        for i in data['hits']:
            id_list.append( i['id'] )
        params['from'] = data['pagination']['from'] + data['pagination']['count']
    
    file_name = "test.tar.gz"
    print('downloading')
    headers = {'Content-type': 'application/json'}
    r = requests.post(URL_BASE + 'data', data=json.dumps({"ids" : id_list}), headers=headers, stream=True)
    with open(args.output_name, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
        

