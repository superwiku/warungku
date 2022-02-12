# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'warungku.supplier'
    _description = 'Pemasok barang warungku'

    name = fields.Char(string='Nama Perusahaan')
    cp = fields.Char(string='Contact Person')
    no_telp = fields.Char(string='Nomor Telepon')
    alamat = fields.Char(string='Alamat Perusahaan')
    barang_ids = fields.One2many(comodel_name='warungku.barang', 
                                 inverse_name='pemasok', 
                                 string='Barangnya')
    
   
    
    
    
    
