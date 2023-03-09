from odoo import api, fields, models


class Partner(models.Model):
    _name = 'warungku.partner'
    _description = 'human description'

    name = fields.Char(string='Name')
    alamat = fields.Char(string='Alamat')
    

class Pegawai(models.Model):
    _inherit = 'warungku.partner'
    _name = 'warungku.pegawai'
    
    jabatan = fields.Char(string='Jabatan')
    jml_anak = fields.Integer(string='Jumlah Anak')
    
    