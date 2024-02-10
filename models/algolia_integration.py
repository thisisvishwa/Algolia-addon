from odoo import models, fields, api
from odoo.exceptions import UserError
import algoliasearch
import logging

_logger = logging.getLogger(__name__)

class AlgoliaIntegrationSettings(models.Model):
    _name = 'algolia.integration.settings'
    _description = 'Algolia Integration Settings'

    algolia_api_key = fields.Char(string='Algolia API Key', required=True)
    algolia_app_id = fields.Char(string='Algolia App ID', required=True)
    algolia_index_name = fields.Char(string='Algolia Index Name', required=True)

    @api.model
    def get_algolia_client(self):
        settings = self.env['algolia.integration.settings'].search([], limit=1)
        if not settings:
            raise UserError("Algolia settings have not been configured.")
        return algoliasearch.SearchClient.create(settings.algolia_app_id, settings.algolia_api_key)

    @api.model
    def get_algolia_index(self):
        client = self.get_algolia_client()
        settings = self.env['algolia.integration.settings'].search([], limit=1)
        return client.init_index(settings.algolia_index_name)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _prepare_algolia_index_data(self):
        return {
            'objectID': self.id,
            'name': self.name,
            'description': self.description_sale,
            'price': self.list_price,
            'categories': [c.name for c in self.categ_id],
            'attributes': {a.attribute_id.name: a.name for a in self.attribute_line_ids},
        }

    def index_product_data(self):
        index = self.env['algolia.integration.settings'].get_algolia_index()
        for record in self:
            data = record._prepare_algolia_index_data()
            index.save_object(data)
            _logger.info("Indexed product %s to Algolia", record.name)

    @api.model
    def create(self, vals):
        product = super(ProductTemplate, self).create(vals)
        product.index_product_data()
        return product

    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        if 'name' in vals or 'description_sale' in vals or 'list_price' in vals or 'categ_id' in vals or 'attribute_line_ids' in vals:
            self.index_product_data()
        return res

    def unlink(self):
        index = self.env['algolia.integration.settings'].get_algolia_index()
        for record in self:
            index.delete_object(record.id)
            _logger.info("Removed product %s from Algolia index", record.name)
        return super(ProductTemplate, self).unlink()