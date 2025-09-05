from openerp import models, fields, api, _
from openerp.exceptions import Warning

class student(models.Model):
    _name = 'student.student'
    _description = 'Estudiante'

    name = fields.Char('Nombre', required=True)
    carnet = fields.Char('Carnet', required=True)
    email = fields.Char('Email')
    birthdate = fields.Date('Fecha de nacimiento')
    inscription_id = fields.Many2one('inscription.inscription', 'Inscripción')

    @api.model
    def create(self, vals):
        if not vals.get('student_id'):
            seq = self.env['ir.sequence'].next_by_code('student.seq') or '/'
            vals['student_id'] = seq
        return super(student, self).create(vals)
