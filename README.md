# PyMono
pymono is a python wrapper for <a href="https://mono.co"> Mono </a>

- Account
- Transactions
- Statements
- Credits
- Debits
- Bvn Lookup


## Getting Started

- Register on <a href="https://mono.co"> Mono </a>  website and get your Authorization key.
- Setup your mono connect with your mono public key
- Set Your "MONO-SEC-KEY" env


## Installing
```python
   pip install  Py-mono
```


# Usage
```python

    os.environ['MONO-SEC-KEY'] = " "

    from pymono import Mono
    mono=Mono('MONO-CONNECT-ID')

    # Authenticate Mono api key  and use mono conncet id
    data,status=mono.Auth()
    #set user id
    mono.SetUserId(data.get('id'))
    # return  status and json data
    mono.getAccount()

```

## Sanbox to test  mono-connect
<!-- - React js   <a href="https://codesandbox.io/s/laughing-wildflower-0te1o?file=/src/App.js">sandbox</a> from Mono -->
  
## check documentation <a href=""> </a>

## Sanbox to test  mono-connect
<!-- - React js   <a href="https://codesandbox.io/s/laughing-wildflower-0te1o?file=/src/App.js">sandbox</a> from Mono -->


## LICENSE
<a href="LICENSE.MD">MIT LICENSE</a> 
  
## Todo
- publish to pypi
- Support Webhook
