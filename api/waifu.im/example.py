from requests_oauthlib import OAuth1
from xml.etree import ElementTree
import datetime
import requests
import json

from URLs import *

class AllyAPI:
    def __init__(self, oauth_secret, oauth_token, client_key,
                response_format="json"):
        self.format = response_format
        self.url = URLs(response_format=response_format)

        self.oauth_secret = oauth_secret
        self.oauth_token = oauth_token
        self.client_key = client_key
        self.client_secret = client_key

        self.auth_time = None
        self.auth = None
        self.valid_auth_dt = datetime.timedelta(seconds=10)

    def __create_auth(self):
        """A private method to create the OAuth1 object, if necessary."""
        now = datetime.datetime.now()

        if self.auth == None or self.auth_time + self.valid_auth_dt < now:
            self.auth_time = now
            self.auth = OAuth1(self.client_key, self.client_secret, self.oauth_token,
                          self.oauth_secret, signature_type='auth_header')

    def __get_symbol_string(self, symbols):
        if not isinstance(symbols, str): # list
            symbols = ",".join(symbols)
        return symbols

    def __to_format(self, response):
        if self.format == "json":
            return response.json()
        else:
            return ElementTree.fromstring(response.content)

    def __get_data(self, url):
        self.__create_auth()
        return self.__to_format(requests.get(url, auth=self.auth))

    def __submit_post(self, url, data):
        self.__create_auth()
        return self.__to_format(requests.post(url, data=data, auth=self.auth))

    def get_accounts(self):
        """Returns all of the user's accounts."""
        return self.__get_data(self.url.accounts_url())

    def get_accounts_balances(self):
        """Returns the balances of all of the user's accounts."""
        return self.__get_data(self.url.accounts_balances_url())

    def get_account(self, id):
        """Returns a specific account provided the account ID (account number)
        """
        return self.__get_data(self.url.account_url().format(id=str(id)))

    def get_account_balances(self, id):
        """Returns the balances of a specific account (ID = account number)
        """
        return self.__get_data(self.url.account_balances_url().format(id=str(id)))

    def get_account_history(self, id):
        """Returns the history of a specific account (ID = account number)
        """
        return self.__get_data(self.url.account_history_url().format(id=str(id)))

    def get_account_holdings(self, id):
        """Returns the holdings of a specific account (ID = account number)"""
        return self.__get_data(self.url.account_holdings_url().format(id=str(id)))

    def get_market_clock(self):
        """Returns the state of the market, the time until next state change, and current server timestamp."""
        return self.__get_data(self.url.clock_url())

    def get_quote(self, symbols):
        """Returns quote information for a single ticker or list of tickers. Note: this function does not implement selecting customer FIDs as described in the API documentation. These can be filtered from the return if need be."""
        url = self.url.quote_url()+"?symbols={symbols}"
        symbols = self.__get_symbol_string(symbols)
        return self.__get_data(url.format(symbols=symbols))