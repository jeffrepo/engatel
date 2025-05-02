# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _get_tipos(self):
        return [
            ('papel', 'Papel'),
            ('caja', 'Caja'),
        ]
    
    gramaje = fields.Float("Gramaje")
    buje = fields.Float("Buje")
    unidad_caja = fields.Float("Unidad x caja")
    ancho_mmpp = fields.Float("Ancho mmpp")
    tipo_producto = fields.Selection(_get_tipos, string="Tipo de producto Engatel")
    fig_en_flcha = fields.Integer("FIG EN FLCHA")


    @api.onchange('x_studio_ancho','ancho_mmpp')
    def _onchange_fig(self):
        for product in self:
            fig_en_flcha = 0
            if product.x_studio_ancho > 0:
                fig_en_flcha = product.ancho_mmpp / product.x_studio_ancho
            product.fig_en_flcha = fig_en_flcha
            