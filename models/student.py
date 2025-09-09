# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning
import re
from datetime import datetime

class student(models.Model):
    _name = 'school_module.student'
    _description = 'Modelo de estudiante'

    name = fields.Char('Nombre Completo', required=True)
    age = fields.Integer('Edad', required=True)
    photo = fields.Binary('Foto de perfil')
    card = fields.Char('Carnet', readonly=True)
    email = fields.Char('Email', required=True)
    
    grade = fields.Selection([('1p', '1ro primaria'), ('2p', '2do primaria'), ('3p', '3ro primaria'),('4p', '4to primaria'), ('5p', '5to primaria'), ('6p', '6to primaria'),
                              ('1b', '1ro basico'), ('2b', '2do basico'), ('3b', '3ro basico'), 
                              ('1d', '1ro diversificado'), ('2d', '2do diversificado'),('3d', '3ro diversificado'), 
                              ], 'Grado', required=True)
    
    section = fields.Selection([('A', 'A'), ('B', 'B'), ('C', 'C')], 'Seccion', required=True)
    
    subject_ids = fields.Many2many(
        'school_module.subject',
        'student_subject_rel',
        'student_id', 'subject_id',
        string='Materias'
    )
    
    user_id = fields.Many2one('res.users', 'Usuario Odoo', help='Usuario vinculado con Odoo')
    
    _sql_constraints = [
        ('student_card_unique', 'unique(card)', 'El carnet debe ser único.'),
        ('student_email_unique', 'unique(email)', 'El email ya está en uso.'),
    ]
    
    @api.constrains('email')
    def validateEmail(self):
        emailValidation = re.compile(r'^[^@]+@[^@]+\.[^@]+$')
        for rec in self:
            if rec.email and not emailValidation.match(rec.email):
                raise Warning(_("El correo debe ser válido (ej. usuario@dominio.com)."))
            
    @api.constrains('age')
    def validateAge(self):
        for rec in self:
            if rec.age < 7 or rec.age > 19:
                raise Warning(_("Edad ingresada no válida."))

    @api.model
    def create(self, vals):
        if not vals.get('card'):
            sequence = self.env['ir.sequence'].next_by_code('student.seq') or '1'
            sequence_string = str(sequence).zfill(3)
            year = datetime.now().year
            vals['card'] = "%s%s" % (year, sequence_string)
            
        if vals.get('email') and not vals.get('user_id'):
            try:
                user_odoo = self.env['res.users'].create({
                    'name': vals.get('name'),
                    'login': vals.get('email'),
                    'password': 'temporal',
                })
                vals['user_id'] = user_odoo.id
            except Exception:
                pass

        return super(student, self).create(vals)
