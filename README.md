# Mono-Python
A simple python wrapper for MonoAPI (https://mono.co)


## Installation

Register on Mono  website and get your Authorization key.

Still in Development Phase

# Built with 
- Python 3.x
   


```python
     pip install  ??
```

```python
  usage

  from pymono import Mono
  mono=Mono('MONO-CONNECT-ID')

# Authenticate Mono api key  and use mono conncet id 
  data=mono.Auth()
  mono.SetUserId(data.get('id'))

# return  the account of a user id gotten from mono
  mono.GetAccount()

  ........
```

## Todo
- complete unit test
- Travis integration
- publish to pypi
- Test with API access from Mono 
- Support Webhook
