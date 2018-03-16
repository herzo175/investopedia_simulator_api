# Investopedia Simulator API

## Endpoint: [https://investopedia-simulator-api.herokuapp.com/](https://investopedia-simulator-api.herokuapp.com/)

### REST API for communicating with the investopedia simulator
### Based on [investopedia-trading-api](https://github.com/kirkthaker/investopedia-trading-api) by [kirkthaker](https://github.com/kirkthaker)

### Example Requests (using python requests library) (all POST JSON body to '\' endpoint):

```python
import requests


def investopedia(body):
    # convert python dictionary to JSON to send to api
    data = json.dumps(body)
    endpoint = 'https://investopedia-simulator-api.herokuapp.com/'

    # Response will be in json form, under the key 'result'
    return requests.post(endpoint, data=data).json()['result'])


# Get Quote:
quote = investopedia({
    'function': 'get_quote',
    'symbol': s
})

# Get portfolio status
portfolio_status = investopedia({
    'function': 'get_portfolio_status',
    'email': INVESTOPEDIA_USERNAME,
    'password': INVESTOPEDIA_PASSWORD
})

# Get current securities
current_securities = investopedia({
    'function': 'get_current_securities',
    'email': INVESTOPEDIA_USERNAME,
    'password': INVESTOPEDIA_PASSWORD
})

# Get open trades
open_trades = investopedia({
    'function': 'get_open_trades',
    'email': INVESTOPEDIA_USERNAME,
    'password': INVESTOPEDIA_PASSWORD
})

# Trade (orderType can be 'buy', 'sell', 'short', or 'cover')
investopedia({
    'function': 'trade',
    'email': INVESTOPEDIA_USERNAME,
    'password': INVESTOPEDIA_PASSWORD,
    'orderType': 'buy',
    'symbol': s,
    'quantity': int(num_shares)
})
```