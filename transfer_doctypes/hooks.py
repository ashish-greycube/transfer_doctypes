# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "transfer_doctypes"
app_title = "Transfer Doctypes"
app_publisher = "GreyCube Technologies"
app_description = "App to help transfer doctypes and related documents"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/transfer_doctypes/css/transfer_doctypes.css"
# app_include_js = "/assets/transfer_doctypes/js/transfer_doctypes.js"

# include js, css files in header of web template
# web_include_css = "/assets/transfer_doctypes/css/transfer_doctypes.css"
# web_include_js = "/assets/transfer_doctypes/js/transfer_doctypes.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "transfer_doctypes.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "transfer_doctypes.install.before_install"
# after_install = "transfer_doctypes.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "transfer_doctypes.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"transfer_doctypes.tasks.all"
# 	],
# 	"daily": [
# 		"transfer_doctypes.tasks.daily"
# 	],
# 	"hourly": [
# 		"transfer_doctypes.tasks.hourly"
# 	],
# 	"weekly": [
# 		"transfer_doctypes.tasks.weekly"
# 	]
# 	"monthly": [
# 		"transfer_doctypes.tasks.monthly"
# 	]
# }

# Testing
# -------
fixtures = [
      {
        "dt": "Project",
        "filters": [["name", "in", ["Test"]]]
      },
      {
        "dt": "Task",
        "filters": [["name", "in", ["TASK-2020-00001"]]]
      },  
      {
        "dt": "Activity Log",
        "filters": [["name", "in", ["5f4b0612b1"]]]
      },   
      {
        "dt": "Comment",
        "filters": [["name", "in", ["caf64c94f2","296158b74f","19281d62f2","1595f109ac"]]]
      },              

]
# before_tests = "transfer_doctypes.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "transfer_doctypes.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "transfer_doctypes.task.get_dashboard_data"
# }

