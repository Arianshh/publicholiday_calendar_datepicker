# Copyright 2023 Arian Shariat <arian.shariat@gmail.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Public Holiday Calendar",
    "summary": "Public holidays color changes in datepicker and calendar.",
    "version": "15.0",
    "license": "LGPL-3",
    "category": "custom",
    "author": "Arian Shariat",
    "website": "https://github.com/Arianshh",
    "depends": ["hr_holidays"],
    "css": ['static/src/css/style.css'],
    "price": 19.99,
    'currency': 'USD',
    'images': ['static/description/calendar.png'],
    "data": [
        "data/data.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'publicholiday_calendar_datepicker/static/src/css/style.css',
        ],
        'web.assets_common': [
            "publicholiday_calendar_datepicker/static/src/legacy/js/libs/fullcalendar.js",
            "publicholiday_calendar_datepicker/static/lib/tempusdomainus.js/tempusdomainus.js",

        ],
    },

    "installable": True,
    "application": True,
}
