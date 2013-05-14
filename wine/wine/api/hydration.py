from decorators import hydrate_once

@hydrate_once
def hydrate_price(field, bundle):
    """ When the price is sent to the server, create the integer representation
        that the database will store """
    if field in bundle.data:
        price = int(bundle.data[field] * 100.0)
        bundle.data[field] = price
    return bundle

def dehydrate_price(field, bundle):
    """ When returning the price to the client, return the floating point value
        that represents the correct price"""
    if getattr(bundle.obj, field):
        price = float(getattr(bundle.obj, field)) / 100.0
        bundle.data[field] = price
    return bundle
