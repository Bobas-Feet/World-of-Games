import requests
import random
from credentials import api_key


def get_money_interval():
    rng = random.randint(1, 100)
    curr_from = input('Please enter the currency from which you would like to convert: ').upper()
    curr_to = input('Please enter the currency to which you would like to convert: ').upper()
    amount = int(input('Please enter the amount you would like to convert: '))
    return curr_from, curr_to, amount

    # Get converted amount


def get_converted_amount(curr_from, curr_to, amount):
    #
    # url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{curr_from}/{curr_to}/{amount}'
    #     # Parse the result as JSON
    # data = requests.get(url).json()
    #     # Extract the converted amount
    # converted_amount = data['conversion_result']

    # return converted_amount
    return

def play():
    if __name__ == '__main__':
        curr_from, curr_to, amount = get_money_interval()
        converted_amount = get_converted_amount(curr_from, curr_to, amount)
        print(f'{amount} {curr_from} = {converted_amount} {curr_to}')
    get_converted_amount(curr_from=0, curr_to=0, amount=0)
    get_money_interval()


