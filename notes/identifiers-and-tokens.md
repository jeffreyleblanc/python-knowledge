
## PK/Tokens Types

* `int` that increments
* `uuid`
    * generally uuid4
    * string format being `uuid.hex`
* base36 token: `EEEE-EEEE`
    * name it `tk8b36`
* base58 token: `EEEE-EEEE-EEEE`
    * name it `tk12b58`
* others
    * `Path` which is a posix file path
    * `tag` which for things like tags, are just the string value

```python
>>> 36**8
2821109907456
>>> 58**8
128063081718016
>>> 36**12
4738381338321616896
>>> 58**12
1449225352009601191936
```

Questions:

* Why padding in things like base64?

## Some Kinds of Indentifiers

Typical

* standard incrementing `int`
* `uuid`
    * <https://en.wikipedia.org/wiki/Universally_unique_identifier>
    * different kinds
        * uuid1 => random but uses machine info
        * uuid4 => random
        * uuid3 => based on MD5 of namespace identifier (UUID) and a name (string)
        * uuid5 => based on SHA1 of namespace identifier (UUID) and a name (string)
    * Also see for more uuid and links to other approaches: <https://www.ietf.org/archive/id/draft-peabody-dispatch-new-uuid-format-01.html>
* ULID
    * <https://github.com/ulid/spec>
    * <https://github.com/ahawker/ulid>
    * <https://github.com/ulid/javascript>
* snowflake id
    * <https://en.wikipedia.org/wiki/Snowflake_ID>
    * <https://github.com/vd2org/snowflake>

Typical bases

* hex (base16)
* base36 (A-Z + 0-9)
* base32 crockford
* base62 (A-Z + a-z + 0-9)
* base58
* base64

Custom identifiers:

* base36 with 8 entries: XXXX-XXXX
* base58 with 12 entries: XXXX-XXXX-XXXX

## Some Notes on UUID

```python
>>> u1 = uuid.uuid4()
>>> u1
UUID('b25cf5f8-657e-4248-b9eb-80aa5e7a0adb')
>>> str(u1)
'b25cf5f8-657e-4248-b9eb-80aa5e7a0adb'
>>> len(str(u1))
36
>>> u1.hex
'b25cf5f8657e4248b9eb80aa5e7a0adb'
>>> len(u1.hex)
32
>>> u1.urn
'urn:uuid:b25cf5f8-657e-4248-b9eb-80aa5e7a0adb'
>>> len(u1.urn)
45
>>> u1hex = u1.hex
>>> u1hex
'b25cf5f8657e4248b9eb80aa5e7a0adb'
>>> u_clone = uuid.UUID(u1hex)
>>> u_clone
UUID('b25cf5f8-657e-4248-b9eb-80aa5e7a0adb')
>>> u_clone == u1
True
```
