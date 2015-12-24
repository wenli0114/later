"""
This plugin exports data from later to json, with support of revisions from revision plugin.

The following format is used:
{
    "issues":{
        "guid1":{
            "properties":{},
            "summ":"",
            "full":""
        },
        "guid2":{
            "properties":{},
            "summ":"",
            "full":""
        },
    },
    "revisions":[
        {
            "rev": "rev1",
            "reported":["guid1", "guid2"],
            "confirmed":["guid3", "guid4"],
            "closed:["guid5", "guid6"]
        },
        {
            "rev": "rev2",
            "reported":["guid1", "guid2"],
            "confiremd":["guid3", "guid4"],
            "closed:["guid5", "guid6"]
        }
    ]
}
"""

import json

_HOOKS=None

def export_json(issues, revisions=[], be=0):
    issues = [extract_obj(iss) for iss in issues]    
    
    revs = {}
    revisions = [""]+revisions  # Add blank revision
    for rev in revisions:
        revs[rev] = dict(rev=rev)
    
    isss = {}
    for iss in issues:
        isss[iss['guid']] = iss

        props = iss['properties']
        rev = props.get('revision', '')
        sta = props.get('status', '')
        
        ### add into revision
        if not revs[rev].get(sta):
            revs[rev][sta] = []
        revs[rev][sta].append(iss['guid'])
    
    obj = dict(
        issues = isss,
        revisions = []
    )

    for rev in revisions:
        obj['revisions'].append(revs[rev])
    
    if be: return obj

    obj_json = json.dumps(obj)
    print obj_json

def extract_obj(issue):
    return dict(
        guid = issue.guid,
        summ = issue.msg.split('\n')[0],
        full = issue.longString(),
        properties = issue.properties
    )

def cmd_export(args):
    """
Export data to json format.
Usage: later export > output.json
    
The following format is used:
{
    "issues":{
        "guid1":{
            "properties":{},
            "summ":"",
            "full":""
        }
    },
    "revisions":[
        {
            "rev": "rev1",
            "reported":["guid1", "guid2"],
            "confiremd":["guid3", "guid4"],
            "closed:["guid5", "guid6"]
        }
    ]
}
    """

    revs = _HOOKS.cmd_revision(['list', 'be'])
    issues = (_HOOKS.be_load_issue(g) for g in _HOOKS.be_all_guids()) 
    return export_json(issues, revs, be=len(args))

def plugin_init(hooks):
	global _HOOKS
	hooks["cmd_export"] = cmd_export
	_HOOKS = hooks

