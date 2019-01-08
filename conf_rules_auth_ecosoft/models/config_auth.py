from odoo import models, api, fields, _




class OrgStructure(models.Model):
    _name = "rules.org.structure"
    _order = 'name'
    name = fields.Char(string='Estructura Organizacional', required=True)
    users_ids = fields.Many2many('res.users')
    
class Plaza(models.Model):
    _name = "rules.plazas"
    _order = 'name'
    name = fields.Char(string='Plaza', required=True)
    org_structure_ids = fields.Many2many('rules.org.structure',  string='Estructuras Organizacionales')
    users_ids = fields.Many2many('res.users')

class Users(models.Model):    
    _inherit = "res.users"
    plazas_ids = fields.Many2many('rules.plazas', string='Plazas')
    org_structure_ids = fields.Many2many('rules.org.structure',  string='Estructuras Organizacionales')

    
class Rule(models.Model):
    _name = "rules.rule"    
    name = fields.Char(string='Nombre', required=True)   
    org_structure_id = fields.Many2one('rules.org.structure', string='Estructura Organizacional', index=True)
    plaza_id = fields.Many2one('rules.plazas', string='Plaza', index=True)    
    rule_line_ids = fields.One2many('rules.rule.line', 'rule_id', string='Rule Lines', copy=True, auto_join=True)

class RuleLine(models.Model):
    _name = "rules.rule.line"        
    name = fields.Text(string='Descripción', required=True)
    users_ids = fields.Many2many('res.users', string='Usuarios que autorizan')
    rule_id = fields.Many2one('rules.rule', string='Rule Reference', required=True, ondelete='cascade', index=True, copy=False)
    amount_max = fields.Float('Monto máximo', required=True, default=0.0)
    amount_min = fields.Float('Monto mínimo', required=True, default=0.0)
    


