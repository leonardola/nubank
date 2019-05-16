from Downloader import Downloader
from Entity.Movement import Movement
from Entity.Movement_has_Category import Movement_has_Category
from datetime import datetime

class Importer:

    def __init__(self, uuid):
        Movement_has_Category.delete().execute()
        Movement.delete().execute()

        downloader = Downloader(uuid)
        account_statements = downloader.download_account_data()

        for statement in account_statements:
            date = datetime.strptime(statement['postDate'], '%Y-%m-%d')

            if statement['__typename'] == 'BarcodePaymentEvent':
                type = 'OUTCOME'
                original_name = statement['title'] + " " + statement['detail']
            elif statement['__typename'] == 'TransferOutEvent':
                type = 'OUTCOME'
                original_name = statement['title'] + " " + statement['destinationAccount']['name']
            elif statement['__typename'] == 'TransferInEvent':
                original_name = statement['title']

                if statement['originAccount']:
                    original_name = original_name + " " + statement['originAccount']['name']

                type = 'INCOME'

            if statement['__typename'] == 'TransferOutReversalEvent':
                value = float(statement['detail'].split('R$ ', 1)[1].replace('.', '').replace(',', '.'))
                type = 'REVERSAL'
            else:
                value = statement['amount']

            Movement.create(
                original_name=original_name,
                date=date,
                value=value,
                status='SHOW',
                type=type,
                hash=statement['id']
            )

        card_statements = downloader.download_credit_card_data()

        for statement in card_statements:
            rest = statement['time'].split('T', 1)[0]  # todo Haw ficou de corrigir para a data iso

            date = datetime.strptime(rest, '%Y-%m-%d')
            Movement.create(
                original_name=statement['description'],
                date=date,
                value=statement['amount'] / 100,
                status='SHOW',
                type='OUTCOME'
            )
