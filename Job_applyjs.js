function updateChildTableView(frm) {
    // Get the selected role from the form
    var role = frm.doc.role;
    
    // Clear existing rows in the child table
    frm.clear_table('details');
    
    // Depending on the selected role, add rows to the child table
    if (role === 'Developer') {
        addDeveloperRows(frm);
    } else if (role === 'QA') {
        addQARows(frm);
    } else if (role === 'Graphic Designer') {
        addGraphicDesignerRows(frm);
    }
}

function addDeveloperRows(frm) {
    // Add rows for Developer role
    frm.add_child('details', {
        language: 'Python',
        framework: 'Django',
        language: "JavaScript",
        framework: "React Native",
        language: "PHP",
        framework: "Laravel",
        // Add other fields as necessary
    });
    // Refresh the child table to reflect changes
    frm.refresh_field('details');
}

function addQARows(frm) {
    // Add rows for QA role
    frm.add_child('details', {
        testing_tools: 'Selenium',
        bug_tracking_system: 'Jira',
        // Add other fields as necessary
    });
    // Refresh the child table to reflect changes
    frm.refresh_field('details');
}

function addGraphicDesignerRows(frm) {
    // Add rows for Graphic Designer role
    frm.add_child('details', {
        design_tools: 'Adobe Photoshop',
        design_style: 'Modern',
        // Add other fields as necessary
    });
    // Refresh the child table to reflect changes
    frm.refresh_field('details');
}frappe.ui.form.on('Job Apply', {
    role: function (frm) {
        // Trigger function to update child table list view based on selected role
        updateChildTableView(frm);
    }
});

