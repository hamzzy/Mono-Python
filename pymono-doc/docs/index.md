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
    mono.Auth()
```

