# -*- encoding: utf-8 -*-
###############################################################################
#
#    Module Writen to OpenERP, Open Source Management Solution
#
#    All Rights Reserved.
###############Credits######################################################
#    Coded by: Edgar Gustavo ehernandez@ecosoft.com.mx
#    Planified by: Edgar Gustavo
#    Finance by: Ecosoft.
#    Audited by: Edgar Gustavo
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Ecosoft Autorizacion Pagos',

    'summary': """Modulo desarrollado para autorizar pagos""",

    'description': """
        Modulo desarrollado con la intencion de solicitar autorizacion para realizar pagos. 
    """,

    'author': 'Edgar Gustavo',

    "website" : "",

    'category': '',

    'version': '1.0',

    'depends': ['base', 'account', 'conf_rules_auth_ecosoft',],

    'data': [
            'wizard/wizard_autorizar_pagos.xml',
            'views/account_payment_view_update.xml',
            'views/user_update.xml',
            'views/payment_views_update.xml',
            'views/estructura_organizacional_view.xml',
            'security/security.xml',
            'views/ejemplo_accion.xml',
           ],

    'installable': True,

    'active': False,

    'certificate': '',

    'application':True,
}
