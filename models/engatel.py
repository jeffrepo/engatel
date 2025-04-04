# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class EngatelEstado(models.Model):
    _name = 'engatel.estado'

    name=fields.Char("Nombre")

class EngatelTipoPapel(models.Model):
    _name = 'engatel.tipo_papel'

    name=fields.Char("Nombre")

class EngatelParteProduccionCortadoras(models.Model):
    _name = 'engatel.parte_produccion_cortadoras'

    orden_trabajo_id = fields.Many2one("mrp.production", "No. OT")
    sub_orten_trabajo = fields.Char("No. SUB OT")
    ancho_materia_prima = fields.Float("ANCHO MAT. PRIMA")
    estado_id = fields.Many2one("engatel.estado", "Estado")
    hora = fields.Char("Hora")
    cantidad_producida = fields.Float("CANT. PRODUCIDA")
    vbo_supervisor_mecanico = fields.Char("Vo.Bo. SUPERVISOR o MECANICO ")
    kilos_bobina_picada = fields.Float("KILOS BOBINA PICADA")
    tipo_papel = fields.Many2one("engatel.tipo_papel","Tipo papel")
    gramaje = fields.Char("Gramaje")
    rollos_caja = fields.Float("Rollos por caja")
    firma_pallet = fields.Signature(string='Firma por pallet'))