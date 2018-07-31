# -*- coding: utf-8 -*-
from odoo import models, fields, api


class VisitorDetails(models.Model):
    _name = 'customer.details'

    name = fields.Char(string="Name", required=True)
    circuit_id = fields.Char(string="Circuit ID", required=True, )
    crq = fields.Char(string="CRQ", required=True, )
    assigned_eng = fields.Many2one(comodel_name="hr.employee", string="Assigned Engineer", required=True, )
    estate_name = fields.Char(string="Estate Name", required=False, )
    region_name = fields.Char(string="Region", required=False, )
    house_number = fields.Char(string="House Number", required=False, )
    phone = fields.Char(string="Phone", required=False)
    email = fields.Char(string="Email", required=False)
    text_field = fields.Text(string="Notes", required=False, )
    #company_info = fields.Many2one('res.partner', string="Company", help='Visiting persons company details')
    #visit_count = fields.Integer(compute='_no_visit_count', string='# Visits')

    #_sql_constraints = [
    #    ('field_uniq_email_and_id_proof', 'unique (email,id_proof)', "Please give the correct data !"),
    #]






