import json
import yaml
from pynubank.nubank import Nubank


# from Nubank import Nubank


class Downloader:

    def get_config(self):
        with open('config.yml', 'r') as f:
            doc = yaml.load(f)
        return doc

    def __init__(self, uuid):
        config = self.get_config()

        self.cpf = config['cpf']
        self.password = config['password']

        self.nu = Nubank()
        self.nu.authenticate_with_qr_code(self.cpf, self.password, uuid)

    def download_account_data(self):
        account_statements = self.nu.get_account_statements()

        app_json = json.dumps(account_statements)
        f = open("account_statements.json", "w+")
        f.write(app_json)
        f.close()

        return account_statements

    def download_credit_card_data(self):
        card_statements = self.nu.get_card_statements()

        app_json = json.dumps(card_statements)
        f = open("card_statements.json", "w+")
        f.write(app_json)
        f.close()

        return card_statements

    #
    # def download_account_data(self):
    #     f = open("account_statements.json", "r")
    #     adsf = f.read()
    #     f.close()
    #     return json.loads(adsf)
    #
    # def download_credit_card_data(self):
    #     f = open("card_statements.json", "r")
    #     adsf = f.read()
    #     f.close()
    #     return json.loads(adsf)
