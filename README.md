# Odoo Algolia Search Integration

This Odoo addon integrates Algolia Search Engine with Odoo 16 Community Edition ecommerce websites, providing advanced search capabilities and an enhanced user experience.

## Features

- Secure API connection with Algolia.
- Automatic indexing of product data including titles, descriptions, attributes, and categories.
- Real-time index updates on product data changes.
- Faceted search, typo tolerance, fuzzy matching, and autocomplete suggestions.
- Enhanced search result display with product information, ratings, and reviews.
- Sorting and filtering of search results.

## Installation

1. Copy the addon to your Odoo addons directory.
2. Update the Odoo app list by navigating to Apps > Update Apps List.
3. Install the addon by searching for 'Algolia Search Integration' in the apps list.

## Configuration

1. Navigate to the Algolia settings in the Odoo backend.
2. Enter your `ALGOLIA_API_KEY`, `ALGOLIA_APP_ID`, and `ALGOLIA_INDEX_NAME`.
3. Configure indexing rules, synonyms, and ranking criteria as needed.

Refer to `doc/setup_guide.md` for detailed setup instructions.

## Usage

Once installed and configured, the Algolia search features are automatically enabled on your ecommerce website.

For frontend customization, refer to `static/src/js/algolia_autocomplete.js` and `static/src/css/algolia_styles.css`.

For backend settings, see `views/algolia_settings_views.xml`.

Refer to `doc/usage_instructions.md` for detailed usage instructions.

## Security

Ensure that your API keys and credentials are stored securely. Follow the Odoo best practices for addon development to maintain code security.

## Support

For ongoing support and maintenance, please contact the addon developer or refer to the `doc/` directory for documentation.

## Testing

Run the tests provided in `tests/test_algolia_integration.py` to ensure the addon's functionality and quality.

## Dependencies

- Odoo 16 Community Edition
- Algolia account with valid API credentials

## Additional Information

This addon is designed to be compatible with future Odoo version updates. Existing Odoo libraries and modules for Algolia integration should be leveraged where possible.

## License

This software is licensed under the MIT License. See `__manifest__.py` for full license details.