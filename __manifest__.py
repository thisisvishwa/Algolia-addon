{
    'name': 'Algolia Search Engine Integration',
    'version': '1.0',
    'summary': 'Integrates Algolia Search Engine with Odoo 16 Community Edition Ecommerce',
    'category': 'Website',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': ['website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/algolia_settings_views.xml',
        'views/product_template_views.xml',
        'data/algolia_data.xml',
        'controllers/main.py',
        'static/src/xml/algolia_templates.xml',
    ],
    'demo': [],
    'qweb': [
        'static/src/xml/algolia_templates.xml',
    ],
    'js': [
        'static/src/js/algolia_autocomplete.js',
    ],
    'css': [
        'static/src/css/algolia_styles.css',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'external_dependencies': {
        'python': [],
    },
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'pre_init_hook': 'pre_init_hook',
    'test': [
        'tests/test_algolia_integration.py',
    ],
    'images': [],
    'description': """
Integration of Algolia Search Engine with Odoo 16 Community Edition Ecommerce Website
======================================================================================
This module integrates Algolia Search Engine with Odoo 16 Community Edition Ecommerce Website to enhance the search experience.
    """,
    'maintainer': 'Your Company Support',
    'support': 'support@yourcompany.com',
}