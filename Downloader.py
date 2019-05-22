import json
import yaml
from pynubank.nubank import Nubank


class Downloader:

    def get_config(self):
        with open('config.yml', 'r') as f:
            doc = yaml.load(f)
        return doc

    def __init__(self, uuid):
        self.config = self.get_config()

        if self.config['develop'] == True:
            print(uuid)
            return

        self.cpf = self.config['cpf']
        self.password = self.config['password']

        self.nu = Nubank()
        self.nu.authenticate_with_qr_code(self.cpf, self.password, uuid)

    def download_account_data(self):
        if self.config['develop'] == True:
            f = open("account_statements.json", "r")
            data = f.read()
            f.close()
            return json.loads(data)

        account_statements = self.nu.get_account_statements()

        app_json = json.dumps(account_statements)
        f = open("account_statements.json", "w+")
        f.write(app_json)
        f.close()

        return account_statements

    def download_credit_card_data(self):
        if self.config['develop'] == True:
            f = open("card_statements.json", "r")
            data = f.read()
            f.close()
            return json.loads(data)

        card_statements = self.nu.get_card_statements()

        app_json = json.dumps(card_statements)
        f = open("card_statements.json", "w+")
        f.write(app_json)
        f.close()

        return card_statements
