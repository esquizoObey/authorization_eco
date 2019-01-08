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

from odoo import models, fields, api, _
from odoo.exceptions import except_orm
import logging
_logger = logging.getLogger(__name__)


class account_payment(models.Model):
    _inherit ="account.payment"

    state = fields.Selection([('draft', 'Draft'), ('posted', 'Posted'), ('por_autorizar', 'Por autorizar'), ('autorizado', 'Autorizado'), ('no_autorizado', 'No autorizado'),
                              ('sent', 'Sent'), ('reconciled', 'Reconciled'),('cancelled', 'Cancelled')], readonly=True, default='draft', copy=False, string="Status")
    aprobacion_turno= fields.Integer(string='Usuario a confirmar')


    # def prueba(self):
    #     _logger.debug('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    #     _logger.debug(self)
    #     _logger.debug('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    #     res= {
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'wizard.prueba',
    #         'views': [(False, 'form')],
    #         'res_id': 70965,
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'target': 'new',
    #     }
    #
    #   return res

    @api.multi
    def autorizar(self):
        _logger.debug('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        _logger.debug(self)
        _logger.debug('AUTORIZAMOS..................................')
        _logger.debug(self.env.context)
        _logger.debug('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

        for aux in self:
            if aux.state!='por_autorizar':
                raise except_orm(('Error'),
                                 ('Solo puedes autorizar despues de realizar una solicitud'))

        #obj_validacion_pagos= self.env['validacion.pago'].search([('pago_id','=',self.id)])



        return