# In your custom app's hooks.py

doc_events = {
    "Job Apply": {
        "validate": "nesto.nesto.validate_job_apply"
    }
}

# In your custom app's custom_module.py
from frappe import frappe

def validate_job_apply(doc, method):
    if doc.role == "Developer":
        # Update Details child table fields for Developer role
        update_child_table_for_developer(doc)
    elif doc.role == "QA":
        # Update Details child table fields for QA role
        update_child_table_for_qa(doc)
    elif doc.role == "Graphic Designer":
        # Update Details child table fields for Graphic Designer role
        update_child_table_for_graphic_designer(doc)
    else:
        frappe.throw(frappe._("Invalid role selected"))

def update_child_table_for_developer(doc):
    # Clear existing rows
    doc.clear_table("details")
    
    # Add rows for Developer role
    doc.append("details", {
        "language": "Python",
        "framework": "Django",
        "language": "JavaScript",
        "framework": "React Native",
        "language": "PHP",
        "framework": "Laravel",
        "ides": "VS Code",  # Default IDE for Developer
        "applied_date": frappe.utils.today(),
        "initials": frappe.session.user_fullname  # Populate with user's full name
    })

    # Refresh the child table to reflect changes
    doc.reload()  # or doc.refresh()


def update_child_table_for_qa(doc):
    # Clear existing rows
    doc.clear_table("details")
    
    # Add rows for QA role
    doc.append("details", {
        "testing_tools": "Selenium",
        "bug_tracking_system": "Jira",
        "automation_experience": 0,
        "test_environments": "",  # Set default value or retrieve from user input
        "applied_date": frappe.utils.today(),
        "initials": frappe.session.user_fullname  # Populate with user's full name
    })

def update_child_table_for_graphic_designer(doc):
    # Clear existing rows
    doc.clear_table("details")
    
    # Add rows for Graphic Designer role
    doc.append("details", {
        "design_tools": "Adobe Photoshop",
        "design_style": "",  # Set default value or retrieve from user input
        "color_theory_knowledge": "",  # Set default value or retrieve from user input
        "typography_skills": "",  # Set default value or retrieve from user input
        "ui_ux_experience": 0,
        "applied_date": frappe.utils.today(),
        "initials": frappe.session.user_fullname  # Populate with user's full name
    })
