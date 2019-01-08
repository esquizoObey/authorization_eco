# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from odoo import fields, models, api
import logging

from odoo.exceptions import except_orm

_logger = logging.getLogger(__name__)
import json

class wizard_enviar_autorizar_pago(models.TransientModel):
    _name='wizard.autorizacion.pago'
    _description='wizard autorizacion de pagos'

    plaza_id = fields.Many2one('rules.plazas', string='Plazas', required=True )
    persona1 = fields.Many2one('res.users', string='Persona 1', required=False, domain="[('org_structure_ids.categoria','=',1)]")#SE FILTRA LOS USUARIOS DEACUERDO A SU CATEGORIA
    firma1 = fields.Boolean(string='Firma 1')                                                                                   #ESTE ATRIBUTO SE ENCUENTRA EN EL MODELO DE ESTRUCTURA ORGANIZACIONAL
    persona2 = fields.Many2one('res.users', string='Persona 2', required=False, domain="[('org_structure_ids.categoria','=',2)]")#QUE TIENE RELACION CON RES.USERS, POR LO CUAL SE PUDO
    firma2 = fields.Boolean(string='Firma 2')                                                                                    #ACCEDER A EL.
    persona3 = fields.Many2one('res.users', string='Persona 3', required=False, domain="[('org_structure_ids.categoria','=',3)]")
    firma3 = fields.Boolean(string='Firma 3')
    persona4 = fields.Many2one('res.users', string='Persona 4', required=False, domain="[('org_structure_ids.categoria','=',4)]")
    firma4 = fields.Boolean(string='Firma 4')
    persona5 = fields.Many2one('res.users', string='Persona 5', required=False, domain="[('org_structure_ids.categoria','=',5)]")
    firma5 = fields.Boolean(string='Firma 5')

    @api.onchange('plaza_id')
    def _onchange_plaza(self):
        filtro=[('id','=',self.plaza_id.id)]
        obj= self.env['rules.plazas'].search(filtro)


        #SE VINCULARON LOS CAMPOS CHECK DE FIRMA DEL WIZAR CON LOS DEL MODELO DE PLAZAS, PARA QUE DE ESTA MANERA DEPENDIENDO
        #DE LA CONFIGURACION QUE TENGA LA PLAZA SEA LAS AUTORIZACIONES QUE SOLICITE EL FORMULARIO.
        self.firma1=obj.firma1
        self.firma2=obj.firma2
        self.firma3=obj.firma3
        self.firma4=obj.firma4
        self.firma5=obj.firma5

        #SE VALIDA QUE CAMBIE DINAMICAMENTE LAS PERSONAS QUE VALIDARAN LA SOLICITUD DE AUTORIZACION DE LOS PAGOS
        #ES DECIR, EL FORMULARIO SE LIMPIA EN AUTOMATICO DEPENDIENDO DE LA CONFIGURACION QUE TENGA POR PLAZA
        #EN LA PESTAÑA DE, CONFIGURACION > PAGOS > AUTORIZACION DE PAGO
        if self.firma1==False:
            self.persona1=False
        if self.firma2==False:
            self.persona2=False
        if self.firma3==False:
            self.persona3=False
        if self.firma4==False:
            self.persona4=False
        if self.firma5==False:
            self.persona5=False

        return

    # @api.model
    # def create(self, vals):
    #
    #     _logger.debug('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
    #     _logger.debug(vals)
    #     _logger.debug('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
    #     return super(wizard_enviar_autorizar_pago, self).create(vals)


    def enviar_autorizacion(self):
        _logger.debug('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        _logger.debug(self.persona1)
        _logger.debug(self.persona2)
        _logger.debug(self.persona3)
        _logger.debug(self.persona4)
        _logger.debug(self.persona5)
        _logger.debug('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

        lista_pagos= self.env.context['active_ids']
        obj_autorizar= self.env['validacion.pago']
        obj = self.env['account.payment'].browse(lista_pagos)
        aprobacion_turno=0
        primer_correo=''
        lista_json=[]

        #SE VALIDA QUE LOS PAGOS ESTEN VALIDADOS
        for aux in obj:
            if aux.state!='posted':
                raise except_orm(('Error'),
                                 ('Solo se pueden mandar autorizar los pagos que esten validados'))

        #SE BUSCA EL EL PRIMER USUARIO QUE AUTORIZARA LA SOLICITUD
        if self.persona1.id!=False:
            _logger.debug('PASO PERSONA 1')
            aprobacion_turno=self.persona1.id
            primer_correo=self.persona1.login

        elif self.persona2.id!=False:
            _logger.debug('PASO PERSONA 2')
            aprobacion_turno = self.persona2.id
            primer_correo = self.persona2.login

        elif self.persona3.id!=False:
            _logger.debug('PASO PERSONA 3')
            aprobacion_turno = self.persona3.id
            primer_correo = self.persona3.login

        elif self.persona4.id!=False:
            _logger.debug('PASO PERSONA 4')
            aprobacion_turno = self.persona4.id
            primer_correo = self.persona4.login

        elif self.persona5.id!=False:
            _logger.debug('PASO PERSONA 5')
            aprobacion_turno = self.persona5.id
            primer_correo = self.persona5.login


        for aux_pagos in lista_pagos:

            datos={
                "pago_id":aux_pagos,
                "persona1":{"id_persona":self.persona1.id,
                            "estatus1":"False",
                            "comentario1":"NULL"},
                "persona2":{"id_persona":self.persona2.id,
                            "estatus2":"False",
                            "comentario2":"NULL"},
                "persona3": {"id_persona": self.persona3.id,
                             "estatus3": "False",
                             "comentario3": "NULL"},
                "persona4": {"id_persona": self.persona4.id,
                             "estatus4": "False",
                             "comentario4": "NULL"},
                "persona5": {"id_persona": self.persona5.id,
                             "estatus5": "False",
                             "comentario5": "NULL"},
            }
            lista_json.append(datos)

        for aux_datos in lista_json:

            # LO FORMATEA PARA CONVERTIRLO EN JSON
            aux_datos_json=json.dumps(aux_datos)

           # SE REGISTRAN DATOS EN .LA TABLA DE VALIDACIONES
            pago_id= aux_datos['pago_id']
            obj_autorizar.create({'pago_id':pago_id,'datos':aux_datos_json})

        obj.write({'state': 'por_autorizar', 'aprobacion_turno':aprobacion_turno})

        # SE LLAMA EL METODO DEL CORREO ELECTRONICO
        self.envio_correo(primer_correo)

        _logger.debug('TERMINO EL PROCESO..............................................................')
        return


    def envio_correo(self, correo):
        _logger.debug('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        _logger.debug('SE ENVIA EL CORREO....')
        _logger.debug(self)
        _logger.debug(self.env.context)
        _logger.debug('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

        lista_pagos = self.env.context['active_ids']
        nueva_lisa=''

        #SE CONSTRUYE LA LISTA DE LOS PAGOS QUE SE PONDRA EN EL MENSAJE DEL CORREO ELECTRONICO
        for aux in lista_pagos:
            pago="http://localhost:8069/web#id={}&view_type=form&model=account.payment&action=126&menu_id=83 <br/>".format(aux)
            nueva_lisa=nueva_lisa + pago

        # credenciales del correo que se usara para generar el correo
        user = 'ehernandez@ecosoft.com.mx'
        passw = 'AR79CD@1'

        remitente = "ehernandez@ecosoft.com.mx"
        destinatario = correo
        asunto = "PAGOS POR AUTORIZAR"
        mensaje = """
            Se solicita la autorizacion de los siguientes pagos: <br/> <br/>       
            {}
        """.format(nueva_lisa)

        # host y puerto
        gmail = smtplib.SMTP('smtp.gmail.com: 587')

        # protocolo utilizado por gmail
        gmail.starttls()

        # credenciales
        gmail.login(user, passw)

        # se crea la instancia del objeto del mensaje
        header = MIMEMultipart()

        # se crea la cabecera del correo
        header['Subject'] = asunto
        header['From'] = remitente
        header['To'] = destinatario

        # formato o tipo del mensaje, en este caso es HTML
        mensaje = MIMEText(mensaje, 'html')  # Content-type:text/html
        header.attach(mensaje)

        # Enviar email
        gmail.sendmail(header['From'], header['To'], header.as_string())

        # Cerrar la conexion SMTP
        gmail.quit()

        _logger.debug('DEBERIA DE HABER ENVIADO EL CORREO')
        _logger.debug(correo)

        return