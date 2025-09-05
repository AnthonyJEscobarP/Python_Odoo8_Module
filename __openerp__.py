{
  'name': 'Modulo de administracion estudiantil',
  'version': '1.0',
  'author': 'Anthony Escobar / AE-Solutions',
  'category': 'Education',
  'depends': ['base','web'],
  'data': [
    'security/ir.model.access.csv',
    'views/classroom_view.xml',
    'views/course_view.xml',
    'views/student_view.xml',
    'views/inscription_view.xml',
    'data/demo_data.xml',
  ],
  'demo': ['demo/demo_data.xml'],
  'installable': True,
  'application': True,
}
