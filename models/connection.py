# -*- coding: utf-8 -*-

from datetime import datetime

from odoo import models,fields,api, _

class NewConnections(models.Model):
    _name = 'ftth.connection'
    _inherit = 'mail.thread'
    my_seq = fields.Char(string="sequence", default=lambda self: _('New'))
    client_id = fields.Many2one(comodel_name="customer.details", string="Client Name", required=False, )
    circuit_id = fields.Char(string="Circuit ID", required=True, )
    crq = fields.Char(string="CRQ", required=True, )
    assigned_eng = fields.Many2one(comodel_name="hr.employee", string="Assigned Engineer", required=True, )
    check_in_date = fields.Datetime(string="DateTime Opened", required=False,)
    check_out_date = fields.Datetime(string="DateTime Closed", required=False,)
    phone = fields.Char(string="Phone", required=False)
    noc_eng = fields.Many2one(comodel_name="hr.employee",string="NOC Engineer", required=False)
    time_diff = fields.Float(string="Duration(Hours)",  required=False )
    text_sla = fields.Text( string="Notes", required=False, )
    sla_state = fields.Selection(string="SLA", selection=[('past_sla', 'Past SLA'), ('within_sla', 'Within SLA'), ], required=False, )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('check_in', 'DateTime Opened'),
        ('check_out', 'DateTime Closed'),
        ('cancel', 'Cancelled'),
    ], track_visibility='onchange', default='draft')

    @api.model
    def create(self, vals):
        if vals:
            vals['my_seq'] = self.env['ir.sequence'].next_by_code('ftth.connection') or _('New')
            result = super(NewConnections, self).create(vals)
            return result


    @api.one
    def action_cancel(self):
        self.state = "cancel"

    @api.one
    def action_check_in(self):
        self.state = "check_in"
        self.check_in_date = datetime.now()

    @api.multi
    def action_check_out(self):
        self.state = "check_out"
        self.check_out_date = datetime.now()

    @api.onchange('client_id')
    def client_details(self):
        if self.client_id:
            if self.client_id.crq:
                self.crq = self.client_id.crq
        if self.client_id:
            if self.client_id.circuit_id:
                self.circuit_id = self.client_id.circuit_id
        if self.client_id:
            if self.client_id.phone:
                self.phone = self.client_id.phone

    @api.onchange('check_in_date', 'check_out_date','time_diff')
    def calculate_date(self):
        if self.check_in_date and self.check_out_date:
            print "++++++++++++++++++++++++++++++++++++++++++++++++++"
            print "++++++++++++++++++++++++++++++++++++++++++++++++++"
            t1 = datetime.strptime(str(self.check_in_date), '%Y-%m-%d %H:%M:%S')
            t2 = datetime.strptime(str(self.check_out_date), '%Y-%m-%d %H:%M:%S')
            t3 = t2 - t1
            days =t3.days
            days_to_hours=days*24
            diff_btw_two_times=(t3.seconds)/3600
            overall_hours = days_to_hours +diff_btw_two_times
            self.time_diff = str(overall_hours)
            print "++++++++++++++++++++++++++++++++++++++++++++++++++"
            print "++++++++++++++++++++++++++++++++++++++++++++++++++"


    @api.onchange('time_diff')
    def get_time_diff(self):
        if self.time_diff >= 24:
            self.sla_state == 'Past SLA'
        else:
            self.sla_state == 'Within SLA'
