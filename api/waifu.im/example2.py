class URLs:
    def __init__(self, response_format="json"):
        self.format = response_format

        self.base_url = "https://api.tradeking.com/v1/"

        # account
        self.accounts = "accounts.{format}".format(format=self.format)
        self.accounts_balances = "accounts/balances.{format}".format(format=self.format)
        self.account = "accounts/{id}.{format}".format(format=self.format, id="{id}")
        self.account_balances = "accounts/{id}/balances.{format}".format(format=self.format, id="{id}")
        self.account_history = "accounts/{id}/history.{format}".format(format=self.format, id="{id}")
        self.account_holdings = "accounts/{id}/holdings.{format}".format(format=self.format, id="{id}")

        # market
        self.clock = "market/clock.{format}".format(format=self.format)
        self.quote = "market/ext/quotes{format}".format(format=self.format)

    def base_url(self):
        return self.base_url

    def accounts_url(self):
        return self.base_url + self.accounts

    def accounts_balances_url(self):
        return self.base_url + self.accounts_balances

    def account_url(self):
        return self.base_url + self.account

    def account_balances_url(self):
        return self.base_url + self.account_balances

    def account_history_url(self):
        return self.base_url + self.account_history

    def account_holdings_url(self):
        return self.base_url + self.account_holdings

    def clock_url(self):
        return self.base_url + self.clock

    def quote_url(self):
        return self.base_url + self.quote