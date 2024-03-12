# Usage Instructions for Algolia Integration with Odoo 16 Community Edition

## Getting Started

Before you begin, ensure you have administrator access to your Odoo 16 Community Edition ecommerce website and the necessary credentials from Algolia.

## Installation

1. Navigate to the Odoo Apps dashboard.
2. Click on "Import Module" and select the `algolia_integration.zip` file.
3. Once the module is installed, activate it by clicking on the "Install" button.

## Configuration

### Setting up Algolia Credentials

1. Go to `Settings` > `Algolia Integration`.
2. Enter your `ALGOLIA_APP_ID` and `ALGOLIA_API_KEY` in the respective fields.
3. Set the `ALGOLIA_INDEX_NAME` to the name of the index you wish to use.

### Configuring Indexing Rules

1. In the Algolia Integration settings, configure the indexing rules, synonyms, and ranking criteria according to your preferences.
2. Save the settings to apply the changes.

## Indexing Product Data

1. To index your products, go to `Inventory` > `Products`.
2. Select the products you want to index and click on "Action".
3. Choose "Index in Algolia" to send the product data to your Algolia index.

## Using the Search Features

### Faceted Search

Faceted search allows users to filter products based on attributes and categories. This feature is automatically enabled once the Algolia integration is configured.

### Typo Tolerance and Fuzzy Matching

Algolia's typo tolerance and fuzzy matching are enabled by default to improve search accuracy.

### Autocomplete Suggestions

As users type in the search bar (`#algolia-search-input`), autocomplete suggestions will appear based on their input.

## Displaying Search Results

Search results will be automatically displayed in the `#algolia-search-results` container with enhanced product listings, including ratings and reviews.

## Sorting and Filtering

Users can sort and filter search results using the options provided in the search results page.

## Maintenance and Support

For ongoing support and maintenance, please contact the developer or refer to the `README.md` and `setup_guide.md` for troubleshooting and additional information.

## Conclusion

With the Algolia integration addon installed and configured, your Odoo ecommerce website now has an enhanced search experience that should lead to increased product discoverability and conversion rates.