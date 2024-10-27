import frappe

@frappe.whitelist(allow_guest=True)
def getAssignTo():
    myUser = frappe.get_doc("User", frappe.session.user)
    users = []

    if len(myUser.companies) > 0 and myUser.name != "Administrator":
        userDocs = frappe.db.sql("""
            SELECT name, parent FROM `tabCompanies` WHERE company = %s AND parenttype = %s
        """, (myUser.companies[0].company, "User"), as_dict=True)
        #     "Companies",
        #     filters= {
        #         "company": f"%{myUser.companies[0].company}%",
        #         "parenttype": "User"
        #     },
        #     fields= ["name", "parent"],
        # )
        for u in userDocs:
            users.append(u.parent)
    else:
        userDocs = frappe.get_all("User")
        for u in userDocs:
            users.append(u.name)

    return users