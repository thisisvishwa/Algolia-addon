from odoo import http
from odoo.http import request

class AlgoliaSearchController(http.Controller):

    @http.route('/algolia/search', type='json', auth='public', website=True)
    def algolia_search(self, search_term, **kwargs):
        algolia_client = request.env['algolia.integration'].get_algolia_client()
        index = algolia_client.init_index(request.env['ir.config_parameter'].sudo().get_param('ALGOLIA_INDEX_NAME'))
        
        # Perform the search on Algolia
        search_results = index.search(search_term, {
            'hitsPerPage': kwargs.get('hitsPerPage', 20),
            'page': kwargs.get('page', 0),
            'facets': '*',
            'facetFilters': kwargs.get('facetFilters')
        })
        
        return search_results

    @http.route('/algolia/autocomplete', type='json', auth='public', website=True)
    def algolia_autocomplete(self, search_term, **kwargs):
        algolia_client = request.env['algolia.integration'].get_algolia_client()
        index = algolia_client.init_index(request.env['ir.config_parameter'].sudo().get_param('ALGOLIA_INDEX_NAME'))
        
        # Get autocomplete suggestions from Algolia
        autocomplete_results = index.search_for_facet_values(
            'name',  # Assuming 'name' is the facet for product names
            search_term,
            {
                'hitsPerPage': kwargs.get('hitsPerPage', 10),
                'facetFilters': kwargs.get('facetFilters')
            }
        )
        
        return autocomplete_results

    @http.route('/algolia/config', type='json', auth='user', website=True)
    def get_algolia_config(self):
        algolia_settings = request.env['algolia.integration'].get_algolia_settings()
        return {
            'ALGOLIA_APP_ID': algolia_settings.get('ALGOLIA_APP_ID'),
            'ALGOLIA_SEARCH_ONLY_API_KEY': algolia_settings.get('ALGOLIA_SEARCH_ONLY_API_KEY'),
            'ALGOLIA_INDEX_NAME': algolia_settings.get('ALGOLIA_INDEX_NAME')
        }