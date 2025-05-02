# -*- encoding: utf-8 -*-

from odoo import api, fields, models, _

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    maquina_id = fields.Many2one("engatel.maquina", "Maquina")
    mts_lineal_fabricar = fields.Float("Metros lineales a fabricar")
    hrs_fabricar = fields.Float("HRS Fabricar")
    tiempo_setup = fields.Float("Setup")
    tiempo_reparacion = fields.Float("Tiempo reparacion")
    tiempo_produccion = fields.Float("Tiempo de producción")
    tiempo_detencion = fields.Float("Tiempo detencion")
    total = fields.Float("T total")

    def _get_moves_raw_values(self):
        moves = super()._get_moves_raw_values()
        for production in self:
            if moves:
                for line in moves:
                    cantidad = 0
                    product_id = self.env["product.template"].search([("id","=", line["product_id"])])
                    if product_id:
                        if product_id.tipo_producto == "papel":
                            cantidad = ((((production.product_id.ancho_mmpp * production.product_id.x_studio_largo) / production.product_id.fig_en_flcha) * production.product_id.gramaje)  / 1000000) * production.product_qty
                            line["product_uom_qty"] = cantidad
                        if product_id.tipo_producto == "caja":
                            cantidad = production.product_qty / production.product_id.unidad_caja
                            line["product_uom_qty"] = cantidad
        return moves