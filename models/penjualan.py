from odoo import api, fields, models


class Penjualan_detail(models.Model):
    _name = 'warungku.penjualan_detail'
    _description = 'Detail Penjualan'

    name = fields.Char(string='Kode Order')
    tanggal = fields.Datetime(string='Tanggal Penjualan',default=fields.Datetime.now)
    
    barangdetail_ids = fields.One2many(
        comodel_name='warungku.barang_detail', 
        inverse_name='order_id', 
        string='Detail Barang')
    
    potong = fields.Boolean(string='Potong Stok', default=False)
    
    
    total_penjualan = fields.Integer(
        compute='_compute_total_penjualan', 
        string='Total Penjualan')
    
    @api.model
    def _compute_total_penjualan(self):
        for record in self:
            total=sum(self.env['warungku.barang_detail'].search([('order_id','=',record.id)]).mapped('jml_harga'))
            record.total_penjualan=total
            
    def invoice(self):
        invoices = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.name,
            'invoice_date': self.tanggal,
            'invoice_line_ids': [(0, 0, {
                'product_id': 0,
                'quantity': 1,
                'price_unit': self.total_penjualan,
                'price_subtotal': self.total_penjualan,
            
            })]
        })       
        return invoices
            
class Barang_detail(models.Model):
    _name = 'warungku.barang_detail'
    _description = 'Detail Barang'

    name = fields.Char(string='Kode Order')
    
    barang_id = fields.Many2one(
        comodel_name='warungku.barang', 
        string='List Barang',
        domain=[('stok','>','20')])
    
    order_id = fields.Many2one(comodel_name='warungku.penjualan_detail', string='Order')
    
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    
    @api.depends('barang_id')
    def _compute_harga(self):
        for record in self:
            record.harga=record.barang_id.harga
    
    qty = fields.Integer(string='Quantity')
    jml_harga = fields.Integer(compute='_compute_jml_harga', string='Jumlah Harga')
    
    @api.depends('qty','harga')
    def _compute_jml_harga(self):
        for record in self:
            record.jml_harga=record.qty*record.harga        
   
    @api.model
    def create(self,vals):
        record = super(Barang_detail, self).create(vals) 
        if record.qty:
            self.env['warungku.barang'].search([('id','=',record.barang_id.id)]).write({'stok':record.barang_id.stok-record.qty})
            return record
            
          
               
   

    
                
    
