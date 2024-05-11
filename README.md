# Client_Script-Assignment-2


Parent DocType: Job Apply


Role: Select field with options Developer, QA, Graphic Designer.


Child Table: Details

The child table "Details" contains role-specific fields for each type of job application.

Fields for Developer Role

Language: Select field with options Python, JavaScript, PHP.

Framework: Read-only field dynamically populated based on the selected language.

IDEs: Select field with options VS Code, IntelliJ IDEA, etc.

Applied Date: Read-only Date field populated automatically when IDEs field is filled.

Initials: Data field populated automatically with user's full name and applied date.

Fields for QA Role

Testing Tools: Select field with options Selenium, Appium, JUnit, etc.

Bug Tracking System: Select field with options Jira, Bugzilla, etc.

Automation Experience: Int field.

Test Environments: Data field.

Applied Date: Read-only Date field populated automatically when Test Environments field is filled.

Initials: Data field populated automatically with user's full name and applied date.

Fields for Graphic Designer Role

Design Tools: Select field with options Adobe Photoshop, Adobe Illustrator, Sketch, etc.

Design Style: Data field.

Color Theory Knowledge: Data field.

Typography Skills: Data field.

UI/UX Experience: Int field.

Applied Date: Read-only Date field populated automatically when Design Style field is filled.

Initials: Data field populated automatically with user's full name and applied date.

Implementation Steps

1. Create Job Apply DocType
2. 
Create a new DocType named "Job Apply" with a field named "Role" as a Select field with options Developer, QA, Graphic Designer.

4. Add Details Child Table
5. 
Add a child table named "Details" to the "Job Apply" DocType with the specified fields for each role.

7. Implement Real-Time Update
8. 
Use JavaScript to listen for changes in the "Role" field of the "Job Apply" DocType.

Trigger a function to update the child table "Details" list view dynamically based on the selected role.

Conclusion

Following these steps will enable you to create and manage job applications effectively within ERPNext, with real-time updates reflecting role-specific details in the child table. Adjust the implementation as per your specific requirements and ERPNext setup.
