from flask import Flask, request, Response, json
from InvestopediaApi import ita

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        try:
            actions = {
                'get_quote': lambda: ita.get_quote(
                    request.args.get('symbol'))
            }

            return json.dumps(
                {'result': actions[request.args.get('function')]()})
        except Exception as exc:
            return json.dumps({'error': str(exc)})
    elif request.method == 'POST':
        try:
            d = json.loads(request.data)
            email, password, func = d['email'], d['password'], d['function']

            if d['function'] == 'trade' or d['function'] == 'trade_option':
                order_type = {
                    'buy': ita.Action.buy,
                    'sell': ita.Action.sell,
                    'short': ita.Action.short,
                    'cover': ita.Action.cover
                }[d['orderType']]

                try:
                    price_type = d['priceType'],
                except KeyError:
                    price_type = 'Market'

                try:
                    price = float(d['price'])
                except KeyError:
                    price = False

                try:
                    duration = {
                        'day_order': ita.Duration.day_order,
                        'good_cancel': ita.Duration.good_cancel
                    }[d['duration']]
                except KeyError:
                    duration = ita.Duration.good_cancel

            def trade():
                return client.trade(
                    d['symbol'],
                    order_type,
                    int(d['quantity']),
                    price_type,
                    price,
                    duration)

            def trade_option():
                return client.trade_option(
                    d['symbol'],
                    order_type,
                    d['optionType'],
                    float(d['strikePrice']),
                    int(d['expire_date']),
                    int(d['quantity']),
                    price_type,
                    price,
                    duration
                )

            client = ita.Account(email, password)
            actions = {
                'get_portfolio_status': lambda: client.get_portfolio_status(),
                'get_current_securities': (
                    lambda: client.get_current_securities()),
                'get_open_trades': lambda: client.get_current_trades(),
                'trade': trade,
                'trade_option': trade_option
            }

            return json.dumps({'result': actions[func]()})
        except Exception as exc:
            return json.dumps({'error': str(exc)})
    else:
        return Response('Method Not Allowed', 405)
