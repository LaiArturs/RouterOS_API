# RouterOS API

Python API for RouterOS. Super light, easy to use and modify.

#### Features:
* Easy to use;
* Standard RouterOS API syntax;
* SSL;
* Verbose.

## Usage:

#### Default configuration:

*Python code:*
```python
from routeros_api import Api

router = Api('192.168.88.1')
r = router.talk('/system/identity/print')
print(r)
```

*Output:*
```
[{'name': 'MikroTik'}]
```

#### Username, password, port:

*Python code:*
```python
from routeros_api import Api

router = Api('10.21.0.100', user='Bob', password='St4ong0nE', port=15811)
r = router.talk('/ip/address/print')
print(r)
```

*Output:*
```
[{'.id': '*5', 'address': '10.21.0.100/24', 'network': '10.21.0.0','interface': 'ether1',
'actual-interface': 'ether1', 'invalid': 'false', 'dynamic': 'false', 'disabled': 'false'}]

```

#### SSL and verbose:

On RouterOS router create **certificate** and assign it to **api-ssl** service.

*RouterOS:*
```
/certificate
add name=ca-template common-name=myCa key-usage=key-cert-sign,crl-sign
add name=server-template common-name=server                           
sign ca-template ca-crl-host=10.21.0.100 name=myCa                         
sign server-template ca=myCa name=server

/ip service
set [find name=api-ssl] certificate=server
```
More info: [MikroTik Wiki](https://wiki.mikrotik.com/wiki/Manual:Create_Certificates).

*Python code:*
```python
from routeros_api import Api

router = Api('10.21.0.100', user='SysAdmin', password='Meeseeks', verbose=True, use_ssl=True)
r = router.talk('/interface/wireless/enable\n=numbers=0')
print(r)
```

*Output:*
```
>>>  /login
>>>  =name=SysAdmin
>>>  =password=Meeseeks

<<<  !done

>>>  /interface/wireless/enable
>>>  =numbers=0

<<<  !done

[]
```

## How it works:
Python3 module *routeros_api.py* contains class *Api*. 
#### \_\_init__()
By initialising this class it creates socket, connects and logs in.
*Api* class *\_\_init__()* arguments:

Argument  | Description
----------|------------
`address` | `str` of IP address or host of RouterOS router on which it can be reached.
`user`    | `str` of username on router, *default='admin'*.
`password`| `str` of password of user on router, *default=''*.
`use_ssl` | `bool` whether to use SSL, *default=False*.
`port`    | `int` on which port to connect to router, *default=8728*, *ssl default=8729*.
`verbose` | `bool` whether to print conversation with router, *default=False*.
`context` | `ssl instance` for creating ssl connection, default is created, but it can be adjusted.

*Python code:*
```python
router = Api(address='192.168.10.1', user='Juri', password='L0vE$aun@', 
             use_ssl=True, port=8730, verbose=False, context=ctx)
```

#### talk()

To send commands to router use *talk()* method of *Api* class. *talk()* take one argument - message:

Argument  | Description
----------|------------
`message` | `str`, `tuple` or `list` of strings or tuples. It is possible to send multiple commands bundled in a list.

*Python code:*
```python
message = [('/system/note/set', '=note=Multi line\nnote for the Router!'), '/system/note/print']
r = router.talk(message)
print(r)
```
*Output:*
```
[[], [{'show-at-login': 'true', 'note': 'Multi line\nnote for the Router!'}]]
```

If property values you want to send to router contains spaces or linebreaks, sentence must be divided in words and then
passed to talk() as `tuple`. Otherwise you can send sentences as strings and it will be divided in words where there is 
space or linebreak.

Method *talk()* returns `list` containing replies from router. In this case there are two replies, because *message* 
contained two sentences. Actions like *set*, *add*, *enable* etc. usually returns empty list, however, *print*, *monitor*
and others returns `list` with `dict` inside containing reply from router.

Messages use RouterOS API syntax. More info: [MikroTik Wiki](https://wiki.mikrotik.com/wiki/Manual:API).

## Conclusion

During the creation of this project I learned about:
* Sockets
* SSL
* RouterOS API