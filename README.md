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

## Environment Key
```
os.environ['MONO-SEC-KEY'] = " "
```

## Usage 
#### Import

```python
   from pymono import Mono
```

#### Exchange Key or Authenticaton
> Set your mono-code accpeted from mono-connect widget.

```python
   mono= Mono('mono-code')
   (data,status) = mono.Auth()
```
#### User Id
> set the user id to get other function working
```python
   mono.SetUserId(data.get("id"))
```



#### Account

> The user account details is returned


```python
   mono.getAccount()
```

#### Transactions

>    

| params      | example
| :---        |    :----:   
| start       | "1-10-2020"
| end         |  "7-11-2020"   
|narration    | uber etc
|types        | debit, credit
| paginate    | true ,false
```python
   
   #Get all the transactions without filter
   mono.getTransactions()
     
   #Parameter accepted  to  filter  Transaction  
   mono.getTransactions(start="",end=" ",narration="",types="",paginate="")
```


#### Statement

> <p>The user statement of account is returned</p>
> </p>It accept parameter to filter statement</p>


| params      | example
| :---        | :----:   
| month       | last6month,last12month   
| output      | json, pdf

```python
   mono.getStatement()  
   # statement with filter
   mono.getStatement("last12month","pdf")
```

#### Credits
> <p> get credits details if user</p>
```python
   mono.getCredits()     
```


#### Debits

```python
   mono.getDebits()
```

#### Identity

```python
   mono.getIdentity()     
```

#### BVN Lookup
| params      | example
| :---        | :----:   
| bvn         | 2256244 

```python
   mono.bvn_lookup(bvn)
```

## Sanbox to test  mono-connect
<!-- - React js   <a href="https://codesandbox.io/s/laughing-wildflower-0te1o?file=/src/App.js">sandbox</a> from Mono -->
  
<!-- ## Documentation 
* <a href="https://hamzzy.github.io/Mono-Python/">Pymono Doc</a> -->



## LICENSE
<a href="LICENSE.MD">MIT LICENSE</a> 

# Contribution  guides

## Todo

- [ ] Webhook Support


