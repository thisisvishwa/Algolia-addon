# Algolia Integration Addon Setup Guide

## Introduction
This guide provides instructions for installing and configuring the Algolia Integration Addon for Odoo 16 Community Edition. By following these steps, you will enhance your ecommerce website's search capabilities using Algolia's powerful search engine.

## Prerequisites
- Odoo 16 Community Edition installed and running
- Administrative access to your Odoo instance
- Algolia account with API Key and Application ID

## Installation

1. Download the addon files from the repository or source provided.
2. Place the addon folder into your Odoo addons directory. The path is typically `/odoo/addons/`.
3. Restart your Odoo server to recognize the new addon. You can do this by running the following command:
   ```
   service odoo-server restart
   ```

## Configuration

### Setting Up Algolia

1. Log in to your Algolia account and obtain your `ALGOLIA_API_KEY` and `ALGOLIA_APP_ID`.
2. Create an index in Algolia Dashboard and note the `ALGOLIA_INDEX_NAME`.

### Configuring Odoo

1. Activate the developer mode in Odoo by going to `Settings` > `Activate the developer mode`.
2. Go to `Apps` and update the app list by clicking on `Update Apps List`.
3. Search for `Algolia Integration Addon` and install it by clicking the `Install` button.
4. After installation, navigate to `Algolia Integration` > `Settings` in the Odoo backend.
5. Enter your `ALGOLIA_API_KEY`, `ALGOLIA_APP_ID`, and `ALGOLIA_INDEX_NAME` in the respective fields.
6. Save the settings to establish the connection between Odoo and Algolia.

## Indexing Products

1. To index your products, go to `Algolia Integration` > `Index Management`.
2. Click on `Index Products` to start the indexing process. This will send your product data to the specified Algolia index.
3. Set up a cron job or use the provided scheduler to automate the indexing process.

## Testing

1. Once the products are indexed, test the search functionality on your ecommerce website.
2. Type a query into the search bar with the ID `#algolia-search-input` and verify that the results are displayed in the container with the ID `#algolia-search-results`.
3. Check the autocomplete suggestions by typing in the search bar and observing the suggestions rendered using the template with the ID `#algolia-autocomplete-template`.

## Troubleshooting

If you encounter any issues during the setup, please refer to the `README.md` and `doc/usage_instructions.md` for further guidance. Additionally, check the logs for any error messages that can provide insight into the problem.

## Support

For ongoing support and maintenance, please contact the addon developer or the support team provided with your addon purchase.

Congratulations! You have successfully set up the Algolia Integration Addon for your Odoo 16 Community Edition ecommerce website. Enjoy the enhanced search capabilities and improved user experience.