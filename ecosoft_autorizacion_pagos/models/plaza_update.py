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
from odoo import models, api, fields, _

class plaza_update(models.Model):
    _inherit = "rules.plazas"

    firma1 = fields.Boolean(string='Firma 1', required=False)
    firma2 = fields.Boolean(string='Firma 2', required=False)
    firma3 = fields.Boolean(string='Firma 3', required=False)
    firma4 = fields.Boolean(string='Firma 4', required=False)
    firma5 = fields.Boolean(string='Firma 5', required=False)