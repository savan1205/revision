# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Revision tasks',
    'version' : '1.2',
    'summary': 'Revision tasks',
    'sequence': 10,
    'description': """
Revision tasks
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'depends' : ['sale_management','website'],
    'data': [ 
        'security/security.xml',      
        'security/revision_tasks_security.xml',      
        'security/ir.model.access.csv',      
        
        'data/custom_snipet.xml',      
        'data/server_so_create.xml',      
        'data/sequence.xml',
        'data/data_views.xml',
        'data/sale_order_server_action.xml',

        'report/report_card.xml',      
        'report/report_template.xml',      
        
        'wizard/wizard_configure_view.xml',      
        'wizard/so_product_fill_views.xml',      
        
        'views/res_config_views.xml',      
        'views/menu_inherit.xml',      
        'views/website_view.xml',      
        'views/company_view.xml',      
        'views/date_task_view.xml',      
        'views/sale_order_view.xml',      
        'views/res_partner_views.xml',      
    ],
    
   
    'installable': True,
    'application': True,
    'auto_install': False,
    
        
    'license': 'LGPL-3',

    'assets':{
        'web.assets_frontend':[
            'revision_tasks/static/src/css/web_style.css'
        ]

    }
}
