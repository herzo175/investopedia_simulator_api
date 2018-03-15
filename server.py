from flask import Flask, request, Response, json
from InvestopediaApi import ita

app = Flask(__name__)


def get_action(req_body):
    # login if email and password are provided
    email, password = (
        req_body.get('email', None), req_body.get('password', None))

    if email is not None and password is not None:
        client = ita.Account(email, password)

    # set default values if not specified and enums
    if (
        req_body['function'] == 'trade' or
            req_body['function'] == 'trade_option'):
        req_body['orderType'] = {
            'buy': ita.Action.buy,
            'sell': ita.Action.sell,
            'short': ita.Action.short,
            'cover': ita.Action.cover
        }[req_body['orderType']]

        req_body['priceType'] = req_body.get('priceType', 'Market')

        try:
            req_body['price'] = float(req_body['price'])
        except KeyError:
            req_body['price'] = False

        req_body['duration'] = {
            'day_order': ita.Duration.day_order,
            'good_cancel': ita.Duration.good_cancel
        }[req_body.get('duration', 'good_cancel')]

    # return closure for function being called
    return {
        'get_quote': lambda: ita.get_quote(req_body['symbol']),
        'get_portfolio_status': lambda: client.get_portfolio_status(),
        'get_current_securities': lambda: client.get_current_securities(),
        'get_open_trades': lambda: client.get_open_trades(),
        'trade': lambda: (
            client.trade(
                req_body['symbol'],
                req_body['orderType'],
                int(req_body['quantity']),
                req_body['priceType'],
                req_body['price'],
                req_body['duration']
            )
        ),
        'trade_option': lambda: (
            client.trade_option(
                req_body['symbol'],
                req_body['optionType'],
                float(req_body['strikePrice']),
                int(req_body['expire_date']),
                int(req_body['quantity']),
                req_body['priceType'],
                req_body['price'],
                req_body['duration']
            )
        )
    }[req_body['function']]


@app.route('/', methods=['POST'])
def api():
    if request.method == 'POST':
        try:
            d = json.loads(request.data)

            return json.dumps({'result': get_action(d)()})
        except Exception as exc:
            return json.dumps({'error': str(exc)})
    else:
        return Response('Method Not Allowed', 405)
