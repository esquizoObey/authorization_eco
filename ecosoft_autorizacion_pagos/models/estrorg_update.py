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
from odoo.exceptions import ValidationError, except_orm
import logging
_logger = logging.getLogger(__name__)


class EstOrg(models.Model):
    _inherit = "rules.org.structure"


    categoria = fields.Selection([(1, 'Categoria 1'), (2, 'Categoria 2'), (3, 'Categoria 3'),
                                  (4, 'Categoria 4'), (5, 'Categoria 5')], string="Categoria")

    @api.model
    def create(self, vals):
        self.validacion_categoria(vals['categoria'])

        return super(EstOrg, self).create(vals)

    def write(self, vals):
        self.validacion_categoria(vals['categoria'])

        return super(EstOrg, self).write(vals)


    def validacion_categoria(self, categoria):

        filtro=[('categoria','=',categoria)]
        consulta= self.env['rules.org.structure'].search(filtro)

        if len(consulta) >=1:
            raise except_orm(_('Error'),
                       _('La estructura organizacional %s, ya cuenta con esa categoria favor de seleccionar otra !') % consulta.name)
        return