# Copyright 2017 Laslabs Inc.
# Copyright 2018 Savoir-faire Linux
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Calendar Resources",
    "summary": "New features to facilitate resource management with meetings.",
    "version": "11.0.1.0.0",
    "category": "Calendar",
    "website": "https://github.com/OCA/calendar",
    "author": "Savoir-faire Linux, LasLabs, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "resource",
        "calendar",
    ],
    "data": [
        "security/resource_security.xml",
        "security/ir.model.access.csv",
        "views/calendar_event_view.xml",
        "views/resource_resource_view.xml",
        "views/calendar_menu.xml",
    ],
    "demo": [
        "demo/resource_calendar.xml",
        "demo/resource_calendar_attendance.xml",
    ],
}
