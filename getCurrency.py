from docopt import docopt
import json
import requests
import re

def convert_currency(input_currency, output_currency, amount):
    r = requests.get('https://www.google.com/finance/converter?a={}&from={}&to={}'.format(amount, input_currency, output_currency))
    if r.status_code == 200:
        data = r.content
        try:
            fetch_result = re.findall ('<span class=bld>(.*?) '+output_currency+'</span>', data, re.DOTALL )
            conversion_result = float("".join(fetch_result).replace('\n',' '))
            return conversion_result
        except:
            return 'enter another output currency'
    else:
        return 'try again later'