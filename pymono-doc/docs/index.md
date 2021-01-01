# Welcome to PyMono

Py-mono is the python API wrapper  for mono.co


## 

## Getting Started

* Register on <a href="https://mono.co"> Mono </a>  website and get your Authorization key.
* Setup your mono connect with your mono public key
* Set Your "MONO-SEC-KEY" 


## Installing
```python
   pip install  py-mono
```

## Environment Key
```
os.environ['MONO-SEC-KEY'] = " "
```

## Usage 
##### Import

```python
   from pymono import Mono
```

##### Exchange Key or Authenticaton

```python
   mono= Mono('mono-code')
   data,status = mono.Auth()
```
### User Id
> set the user id to get other function working
```python
   mono.SetUserId(data.get('id))
```
#### Statement

> The user statement of account is returned

| params      | example
| :---        | :----:   
| month       | last6month,last12month   
| output      | json, pdf

```python
   mono.getStatement()  
```


#### Account

> The user account details is returned


```python
   mono.getAccount()
```

#### Transactions


>  return user transaction all transactions without filter  return all the  

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

```python
   mono.getStatement()
   #p
     
```


#### Credits

```python
   mono.getCredits()
   #p
     
```


#### Debits

```python
   mono.getDebits()
   #p
     
```

#### Identity

```python
   mono.getIdentity()
   #p
     
```

#### BVN Lookup

```python
   mono.bvn_lookup()
   #p
     
```