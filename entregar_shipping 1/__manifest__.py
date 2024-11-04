{
    'name': 'Entrega Integracion Logistica',
    'version': '1.0',
    'summary': 'Integración de métodos de envío con Entregar API',
    'description': 'Módulo personalizado para integrar los métodos de envío de Entregar en Odoo 17.',
    'author': 'Sebastián Díaz',
    'depends': ['base', 'delivery', 'sale'],
    'data': [
        'views/entregar_shipping_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}
