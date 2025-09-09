from openerp import models, fields, _

class Classroom(models.Model):
    _name = 'schoolModule.classroom'
    _description = 'Modelo de Aulas'

    name = fields.Char('Aula', required=True)
    capacity = fields.Integer('Capacidad', required=True)
    
    subject_ids = fields.One2many(
        'schoolModule.subject',
        'classroom_id', 
        string='Materias',
    )
 
    _sql_constraints = [
        ('valid_capacity', 'CHECK (capacity > 0)', 'La capacidad debe ser mayor a cero.'),
        ('classroom_name_unique', 'unique(name)', 'Ya existe un aula con ese nombre.'),
    ]