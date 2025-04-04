# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class EngatelEstado(models.Model):
    _name = 'engatel.estado'

    name=fields.Char("Nombre")

class EngatelTipoPapel(models.Model):
    _name = 'engatel.tipo_papel'

    name=fields.Char("Nombre")

class EngatelMaquina(models.Model):
    _name = 'engatel.maquina'

    name=fields.Char("Nombre")

class EngatelParteProduccionCortadoras(models.Model):
    _name = 'engatel.parte_produccion_cortadoras'

    def _get_turnos(self):
        return [
            ('dia', 'Día'),
            ('noche', 'Noche'),
        ]

    fecha_hora_inicio = fields.Datetime("Fecha y hora inicio")
    fecha_hora_fin = fields.Datetime("Fecha y hora fin")
    turno = fields.Selection(_get_turnos, string="Turno")
    maquina_id = fields.Many2one("engatel.maquina","Maquina")
    operador_id = fields.Many2one("res.partner","Operador")
    linea_ids = fields.One2many("engatel.parte_produccion_cortadoras_lineas","ppc_id", string="Lineas")
    digitado = fields.Char("Digitado por")
    firma_operador = fields.Binary("Firma operador")
    firma_supervisor = fields.Binary("Firma supervisor")

class EngatelParteProduccionCortadorasLineas(models.Model):
    _name = 'engatel.parte_produccion_cortadoras_lineas'

    ppc_id = fields.Many2one("engatel.parte_produccion_cortadoras","Parte produccion cortadoras")
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
    firma_pallet = fields.Binary(string='Firma por pallet')