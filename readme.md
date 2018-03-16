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
    'symbol': 'NFLX'
})

"""
Response:
{"result": 321.09}
"""

# Get portfolio status
portfolio_status = investopedia({
    'function': 'get_portfolio_status',
    'email': INVESTOPEDIA_USERNAME,
    'password': INVESTOPEDIA_PASSWORD
})

"""
Response:
{
    "result": [102057.5, 51101.88, 146.27, 5.26]
}
"""

# Get current securities
current_securities = investopedia({
    'function': 'get_current_securities',
    'email': INVESTOPEDIA_USERNAME,
    'password': INVESTOPEDIA_PASSWORD
})

"""
Response:
{
    "result": [
        [
            ["MU", "MICRON TECHNOLOGY, INC.", 348, 58.75, 58.84, 20476.32],
            ["INTC", "INTEL CORPORATION", 399, 51.18, 50.88, 20301.12],
            ["ORCL", "ORACLE CORPORATION", 390, 52.51, 52.37, 20424.3],
            ["STX", "SEAGATE TECHNOLOGY PLC", 341, 59.9, 59.57, 20313.37],
            ["SAP", "SAP SE SPONSORED ADR", 188, 108.61, 108.49, 20396.12]
        ],
        [],
        []
    ]
}
"""

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
    'symbol': 'GOOG',
    'quantity': 20
})

"""
Response:
{"result": "True"}
"""
```