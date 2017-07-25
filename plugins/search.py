"""
This plugin provides a full text regex search command.
"""

import re

_HOOKS=None

def cmd_search(args):
	"""Search all issues"""

	issues = (_HOOKS.be_load_issue(guid) for guid in _HOOKS.be_all_guids())

	if not args:
		_HOOKS.print_issues(issues)
		return

	searchterms = args

	matched_issues = []
	for issue in issues:
		text = issue.msg

		# remove if you want search to search message text only
		text += "\n" + "\n".join([key + ': ' + issue.properties[key] for key in issue.properties])

		# all search terms must match
		didmatch = True
		for searchterm in searchterms:
			if not (re.search(searchterm, text, re.I)):
				didmatch = False
				break
		if didmatch:
			matched_issues.append(issue)
	
	_HOOKS.print_issues(matched_issues)

def plugin_init(hooks):
	global _HOOKS
	hooks["cmd_search"] = cmd_search
	_HOOKS = hooks


