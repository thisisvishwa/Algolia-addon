odoo.define('algolia_ecommerce.algolia_autocomplete', function(require) {
    "use strict";

    var publicWidget = require('web.public.widget');
    var algoliasearch = require('algolia_ecommerce.algoliasearch');

    publicWidget.registry.AlgoliaAutocomplete = publicWidget.Widget.extend({
        selector: '#algolia-search-input',
        events: {
            'input': '_onInput',
        },

        start: function() {
            this._super.apply(this, arguments);
            this.client = algoliasearch(ALGOLIA_APP_ID, ALGOLIA_API_KEY);
            this.index = this.client.initIndex(ALGOLIA_INDEX_NAME);
        },

        _onInput: function(ev) {
            var self = this;
            var query = $(ev.currentTarget).val();

            if (query.length > 0) {
                this.index.search(query, {
                    hitsPerPage: 5,
                    facets: '*',
                    facetFilters: []
                }).then(function(responses) {
                    self._renderSuggestions(responses.hits);
                }).catch(function(err) {
                    self._handleSearchError(err);
                });
            }
        },

        _renderSuggestions: function(suggestions) {
            var $autocompleteContainer = $('#algolia-autocomplete-template').html();
            var compiledTemplate = _.template($autocompleteContainer);
            var $searchResults = $('#algolia-search-results');

            $searchResults.html(compiledTemplate({ suggestions: suggestions }));
        },

        _handleSearchError: function(error) {
            console.error(ALGOLIA_SEARCH_FAILURE, error);
            var $searchResults = $('#algolia-search-results');
            $searchResults.empty();
        }
    });

    return {
        AlgoliaAutocomplete: publicWidget.registry.AlgoliaAutocomplete
    };
});