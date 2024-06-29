from odoo import api, fields, models, _


class Book(models.Model):
    _name = 'library.book'
    _rec_name = 'name'
    _description = 'Library Book'

    name = fields.Char(string='Book Name', required=True)
    publication_date = fields.Date(string='Publication Date')
    author = fields.Char(string='Author', required=True)