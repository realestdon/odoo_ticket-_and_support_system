# -*- coding: utf-8 -*-
import datetime

from odoo import models,fields,api

class NewIncidents(models.Model):
    _name = 'ftth.incident'
    client_id = fields.Many2one(comodel_name="customer.details", string="Client Name", required=False, )
    circuit_id = fields.Char(string="Circuit ID", required=True, )
    incident_no = fields.Char(string="Incident No.", required=False, )
    phone = fields.Char(string="Phone", required=False)
    assigned_eng = fields.Many2one(comodel_name="hr.employee", string="Assigned Engineer", required=True, )
    opened_field = fields.Datetime(string="DateTime Opened", required=False, )
    closed_field = fields.Datetime(string="DateTime Closed", required=False, )
    noc_eng = fields.Many2one(comodel_name="hr.employee", string="NOC Engineer", required=True, )
    time_diff = fields.Char(string="Time Difference", required=False, )
    text_sla = fields.Text(string="Notes", required=False, )
    sla_state = fields.Selection(string="SLA", selection=[('past sla', 'Past SLA'), ('within sla', 'Within SLA'), ], required=False, )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('check_in', 'DateTime Opened'),
        ('check_out', 'DateTime Closed'),
        ('cancel', 'Cancelled'),
    ], track_visibility='onchange', default='draft')

    @api.one
    def action_check_in(self):
        self.state = "check_in"
        self.check_in_date = datetime.datetime.now()

    @api.multi
    def action_check_out(self):
        self.state = "check_out"
        self.check_out_date = datetime.datetime.now()

    @api.onchange('client_id')
    def visitor_details(self):
        if self.client_id:
            if self.client_id.circuit_id:
                self.circuit_id = self.client_id.circuit_id
        if self.client_id:
            if self.client_id.phone:
                self.phone = self.client_id.phone



