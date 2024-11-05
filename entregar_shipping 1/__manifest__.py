{
    'name': 'Entrega Integración Logística',
    'version': '1.0',
    'summary': 'Integración de métodos de envío con Entregar API',
    'description': 'Módulo personalizado para integrar los métodos de envío de Entregar en Odoo 17.',
    'author': 'Sebastián Díaz',
    'depends': ['base', 'delivery', 'sale'],
    'data': [
        'views/delivery_carrier_views.xml',  # Archivos XML necesario
    ],
    'installable': True,
    'application': False,
    'auto_install': False,  # No se instalará automáticamente con otros módulos dependientes
}
