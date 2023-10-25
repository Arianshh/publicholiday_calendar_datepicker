# Copyright 2015 2011,2013 Michael Telahun Makonnen <mmakonnen@gmail.com>
# Copyright 2020 InitOS Gmbh
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Holidays Calendar",
    "version": "15.0.1.1.1",
    "license": "AGPL-3",
    "category": "Human Resources",
    "author": "Arian Shariat",
    "website": "https://github.com/OCA/hr-holidays",
    "depends": ["ds_time_off", "ds_persian_calendar"],
    'css': ['static/src/css/style.css'],
    "data": [
        "data/data.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'ds_publicholiday_calendar/static/src/css/style.css',
        ],
        'web.assets_common': [
            "ds_publicholiday_calendar/static/src/legacy/js/libs/fullcalendar.js",
            ('remove', 'web/static/lib/tempusdominus/tempusdominus.js'),
            "ds_publicholiday_calendar/static/lib/tempusdomainus.js/tempusdomainus.js",

        ],
    },

    "installable": True,
}
