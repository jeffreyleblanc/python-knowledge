# Serialization Libraries

## Motivation and What I Did

I wanted a place to define message protocols, do basic type casting and validation, and have usable dataclass like instances.

I ended up just writing ~80 lines of code around stdlib dataclasses to do this for now.


## Some Options

* [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
    * [Quickstart](https://marshmallow.readthedocs.io/en/stable/quickstart.html)
    * [Github](https://github.com/marshmallow-code/marshmallow)
    * API: [Fields](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html)
    * Extension: [Dataclass helpers](https://github.com/lovasoa/marshmallow_dataclass)

Overall I like Marshmallow, but alone it's just (de)serializing to dicts, and though there is dataclass help library,
it just struck me as a little cumbersome. Worth another look though. I have few examples in the `_raw` folder here.

* [Pydantic](https://docs.pydantic.dev/latest/)

This looks widely used, but again felt a touch cumbersome for what I was trying to do. See `_raw` folder.

* [Attrs](https://www.attrs.org/en/stable/)
    * [Quickstart](https://www.attrs.org/en/stable/examples.html)

Looks interesting.


