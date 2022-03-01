from odoo import api, fields, models


class Barang(models.Model):
    _name = 'warungku.barang'
    _description = 'New Description'

    name = fields.Char(string='Nama Barang')
    harga = fields.Integer(string='Harga Barang')
    pemasok = fields.Many2one(comodel_name='warungku.supplier', string='Pemasok')
    harga_jual = fields.Integer(string='Harga Jual')    
    stok = fields.Integer(string='Stok')
    kategori = fields.Selection(
        string='Kategori Barang', 
        selection=[('bahan makanan','Bahan Makanan'),('makanan','Makanan'),('sabun','Sabun'),('pakaian','Pakaian')])
    
    laba = fields.Char(compute='_compute_laba', string='laba')
    
    @api.depends('harga','harga_jual')
    def _compute_laba(self):
        for record in self:
            record.laba=record.harga_jual-record.harga
    
    
    
    
