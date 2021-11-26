from odoo import models, fields


class Test(models.Model):
    _name = 'test'
    _description = 'Test'

    data = fields.Char()
    pincode = fields.Integer()


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'

    name = fields.Char()


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string="Property Name", default="Unknown", required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=lambda self: fields.Datetime.now(), copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False, readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([('north', 'North'),
                                           ('south', 'South'),
                                           ('east', 'East'),
                                           ('west', 'West'), ])
    active = fields.Boolean(default=True)
    image = fields.Image()
    property_type_id = fields.Many2one('estate.property.type')
    salesman_id = fields.Many2one('res.users')
    buyer_id = fields.Many2one('res.partner')
    test_id=fields.Many2one('test')
