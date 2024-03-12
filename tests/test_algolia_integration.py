from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError

class TestAlgoliaIntegration(TransactionCase):

    def setUp(self):
        super(TestAlgoliaIntegration, self).setUp()
        # Setup test models, users, and records
        self.algolia_integration_model = self.env['algolia.integration']
        self.product_template_model = self.env['product.template']
        self.user_admin = self.env.ref('base.user_admin')
        self.user_demo = self.env.ref('base.user_demo')

        # Create a test Algolia settings record
        self.algolia_settings = self.algolia_integration_model.create({
            'algolia_api_key': 'test_api_key',
            'algolia_app_id': 'test_app_id',
            'algolia_index_name': 'test_index'
        })

        # Create a test product template
        self.product_template = self.product_template_model.create({
            'name': 'Test Product',
            'description_sale': 'Test Description',
            'list_price': 10.0
        })

    def test_initialize_algolia_client(self):
        # Test initialization of Algolia client
        algolia_client = self.algolia_integration_model._initialize_algolia_client()
        self.assertTrue(algolia_client, "Algolia client should be initialized")

    def test_index_product_data(self):
        # Test indexing of product data
        self.algolia_integration_model._index_product_data(self.product_template)
        # Check if the product data is indexed in Algolia
        # This would require mocking Algolia's API response
        # Assuming a mock function is available
        indexed_data = self.mock_get_indexed_data('test_index', self.product_template.id)
        self.assertEqual(indexed_data.get('name'), 'Test Product', "Product name should be indexed")

    def test_update_algolia_index(self):
        # Test updating Algolia index when product data changes
        self.product_template.write({'name': 'Updated Test Product'})
        self.algolia_integration_model._update_algolia_index(self.product_template)
        # Check if the product data is updated in Algolia
        # This would require mocking Algolia's API response
        updated_data = self.mock_get_indexed_data('test_index', self.product_template.id)
        self.assertEqual(updated_data.get('name'), 'Updated Test Product', "Product name should be updated in index")

    def test_security(self):
        # Test that regular users cannot access Algolia settings
        with self.assertRaises(AccessError):
            self.algolia_settings.with_user(self.user_demo).read()

    def test_search_performance(self):
        # Test that search results are returned quickly
        # This would require mocking Algolia's API response with timing
        search_time = self.mock_search_performance('Test Product')
        self.assertLess(search_time, 200, "Search results should be returned in less than 200ms")

    def tearDown(self):
        # Clean up test records and environment
        self.product_template.unlink()
        self.algolia_settings.unlink()
        super(TestAlgoliaIntegration, self).tearDown()

# Note: The mock functions `mock_get_indexed_data` and `mock_search_performance` are placeholders
# for actual mock implementations that would interact with a mocked version of the Algolia API.