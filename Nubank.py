class Nubank:
    def __init__(self, cpf, password, qrcode):
        return

    def get_account_statements(self):
        return [
            {
                "postDate":"2018-09-14",
                "title":"Transfer\u00eancia recebida",
                "detail":"R$ 3.000,00",
                "__typename":"TransferInEvent",
                "amount":3000.0,
                "id":"5b9b6a27-dee9-4217-a93e-09295bc58fa9"
            },
            {
                "postDate":"2018-09-13",
                "title":"Transfer\u00eancia enviada",
                "detail":"Leonardo Lopes De Albuquerque - R$ 3.000,00",
                "__typename":"TransferOutEvent",
                "amount":3000.0,
                "destinationAccount":{
                    "name":"Leonardo Lopes De Albuquerque"
                },
                "id":"5b9a7167-56fc-41d7-a20a-84a50ad37647"
            }
        ]
    def get_account_balance(self):
        return 5149.31

    def get_card_statements(self):
        return [
            {
                "category":"transaction",
                "description":"Farmacia Preco Popular",
                "title":"sa\u00fade",
                "amount":8157,
                "href":"nuapp://transaction/5ba2d086-456d-4c8d-ac5d-5ff7fd370232",
                "_links":{
                    "self":{
                        "href":"https://prod-s0-webapp-proxy.nubank.com.br/api/proxy/AJxL5LDOOBddn_UasbpmLuScg3281U3ePg.aHR0cHM6Ly9wcm9kLXMzLWZlZWQubnViYW5rLmNvbS5ici9hcGkvdHJhbnNhY3Rpb25zLzViYTJkMDg2LTQ1NmQtNGM4ZC1hYzVkLTVmZjdmZDM3MDIzMg"
                    }
                },
                "details":{
                    "subcategory":"card_present"
                },
                "time":"2018-09-19T22:41:10Z",
                "id":"5ba2d086-456d-4c8d-ac5d-5ff7fd370232"
            },
            {
                "category":"transaction",
                "description":"Farmacia Dias",
                "title":"sa\u00fade",
                "amount":2500,
                "href":"nuapp://transaction/5ba12803-9ac0-486a-b924-0fe34def5457",
                "_links":{
                    "self":{
                        "href":"https://prod-s0-webapp-proxy.nubank.com.br/api/proxy/AJxL5LAmmAXsnWeYoujqgSaUfRidQN9Heg.aHR0cHM6Ly9wcm9kLXMzLWZlZWQubnViYW5rLmNvbS5ici9hcGkvdHJhbnNhY3Rpb25zLzViYTEyODAzLTlhYzAtNDg2YS1iOTI0LTBmZTM0ZGVmNTQ1Nw"
                    }
                },
                "details":{
                    "subcategory":"card_present"
                },
                "time":"2018-09-18T16:29:54Z",
                "id":"5ba12803-9ac0-486a-b924-0fe34def5457"
            },
            {
                "category":"transaction",
                "description":"Giassi Su",
                "title":"supermercado",
                "amount":1628,
                "href":"nuapp://transaction/5ba03432-d8d8-4708-8ff4-0802f7b2c267",
                "_links":{
                    "self":{
                        "href":"https://prod-s0-webapp-proxy.nubank.com.br/api/proxy/AJxL5LDg6W-rWewSwRGOUW5vXbA5SC1ydw.aHR0cHM6Ly9wcm9kLXMzLWZlZWQubnViYW5rLmNvbS5ici9hcGkvdHJhbnNhY3Rpb25zLzViYTAzNDMyLWQ4ZDgtNDcwOC04ZmY0LTA4MDJmN2IyYzI2Nw"
                    }
                },
                "details":{
                    "subcategory":"card_present"
                },
                "time":"2018-09-17T23:09:38Z",
                "id":"5ba03432-d8d8-4708-8ff4-0802f7b2c267"
            }

        ]

    # def get_bills(self):
    #     return [
    #         {u'state': u'open', u'_links': {u'self': {u'href': u'https://prod-s0-webapp-proxy.nubank.com.br/api/proxy/AJxL5LBcMNseS9sw8yEzh_cPimQLZKRFuA.aHR0cHM6Ly9wcm9kLXMzLWJpbGxpbmcubnViYW5rLmNvbS5ici9hcGkvYWNjb3VudHMvNWI4MTk2YmEtOGQ0OS00YTg4LThmNGQtODViNWM4M2YzYWYzL2JpbGxzL29wZW4'}}, u'summary': {u'adjustments': u'0', u'tax': u'0', u'expenses': u'333.84', u'total_balance': 33384, u'close_date': u'2018-10-07', u'fees': u'0', u'minimum_payment': 0, u'interest_rate': u'0.14', u'total_international': u'0', u'total_cumulative': 33384, u'interest': 0, u'precise_total_balance': u'333.84', u'open_date': u'2018-08-25', u'total_accrued': u'0', u'due_date': u'2018-10-14', u'past_balance': 0, u'paid': 0, u'previous_bill_balance': u'0', u'total_national': u'333.84', u'interest_charge': u'0', u'effective_due_date': u'2018-10-15', u'total_payments': u'0', u'international_tax': u'0', u'total_credits': u'0', u'payments': u'0', u'precise_minimum_payment': u'0', u'total_financed': u'0', u'interest_reversal': u'0'}}]
    # def get_bill_details(self, bill):
    #     return [{u'bill':{u'payment_method': u'boleto', u'line_items': [{u'category': u'Servi\xe7os', u'index': 0, u'title': u'Pg *Flatout*Flatout', u'charges': 1, u'post_date': u'2018-09-12', u'amount': 2000, u'href': u'nuapp://transaction/5b97c3e6-f77f-4e23-8988-ae1ec41632f3', u'id': u'5b97c3e6-1cd5-46b6-a4aa-b049faf31a71'}, {u'category': u'Supermercado', u'index': 0, u'title': u'Giassi Su', u'charges': 1, u'post_date': u'2018-09-13', u'amount': 19099, u'href': u'nuapp://transaction/5b99b3a8-7237-44f4-9157-506ce3cc718c', u'id': u'5b99b3a8-41a6-4b4c-95b5-c8e14f400c30'}, {u'category': u'Supermercado', u'index': 0, u'title': u'Giassi Su', u'charges': 1, u'post_date': u'2018-09-18', u'amount': 1628, u'href': u'nuapp://transaction/5ba03432-d8d8-4708-8ff4-0802f7b2c267', u'id': u'5ba03432-be3a-4737-9262-4658ac26447a'}, {u'category': u'Sa\xfade', u'index': 0, u'title': u'Farmacia Dias', u'charges': 1, u'post_date': u'2018-09-19', u'amount': 2500, u'href': u'nuapp://transaction/5ba12803-9ac0-486a-b924-0fe34def5457', u'id': u'5ba12803-d1c5-4327-9c8f-90d8ac9fb6ca'}, {u'category': u'Sa\xfade', u'index': 0, u'title': u'Farmacia Preco Popular', u'charges': 1, u'post_date': u'2018-09-19', u'amount': 8157, u'href': u'nuapp://transaction/5ba2d086-456d-4c8d-ac5d-5ff7fd370232', u'id': u'5ba2d087-d629-40a4-bb6c-9ad713956cba'}], u'state': u'open', u'_links': {u'self': {u'href': u'https://prod-s0-webapp-proxy.nubank.com.br/api/proxy/AJxL5LBcMNseS9sw8yEzh_cPimQLZKRFuA.aHR0cHM6Ly9wcm9kLXMzLWJpbGxpbmcubnViYW5rLmNvbS5ici9hcGkvYWNjb3VudHMvNWI4MTk2YmEtOGQ0OS00YTg4LThmNGQtODViNWM4M2YzYWYzL2JpbGxzL29wZW4'}, u'barcode': {u'href': u'https://prod-s0-webapp-proxy.nubank.com.br/api/proxy/AJxL5LCggeR6yCl2ertfICg9_SNdnfk1XQ.aHR0cHM6Ly9wcm9kLXMzLWJpbGxpbmcubnViYW5rLmNvbS5ici9hcGkvYWNjb3VudHMvNWI4MTk2YmEtOGQ0OS00YTg4LThmNGQtODViNWM4M2YzYWYzL2JpbGxzL29wZW4vYm9sZXRvL2JhcmNvZGU'}, u'boleto_email': {u'href': u'https://prod-s0-webapp-proxy.nubank.com.br/api/proxy/AJxL5LAE1HcuQg36RvyWBAaieeuU0gjSbw.aHR0cHM6Ly9wcm9kLXMzLWJpbGxpbmcubnViYW5rLmNvbS5ici9hcGkvYWNjb3VudHMvNWI4MTk2YmEtOGQ0OS00YTg4LThmNGQtODViNWM4M2YzYWYzL2JpbGxzL29wZW4vYm9sZXRvL2VtYWls'}}, u'summary': {u'adjustments': u'0', u'tax': u'0', u'expenses': u'333.84', u'total_balance': 33384, u'close_date': u'2018-10-07', u'fees': u'0', u'minimum_payment': 0, u'interest_rate': u'0.14', u'total_international': u'0', u'precise_total_balance': u'333.84', u'interest': 0, u'total_cumulative': 33384, u'open_date': u'2018-08-25', u'total_accrued': u'0', u'due_date': u'2018-10-14', u'late_interest_rate': u'0.15', u'past_balance': 0, u'paid': 0, u'previous_bill_balance': u'0', u'late_fee': u'0.02', u'total_national': u'333.84', u'interest_charge': u'0', u'effective_due_date': u'2018-10-15', u'total_payments': u'0', u'international_tax': u'0', u'total_credits': u'0', u'payments': u'0', u'precise_minimum_payment': u'0', u'total_financed': u'0', u'interest_reversal': u'0'}}}]