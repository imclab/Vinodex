def hydrate_once(hydrate_function):
    """ Ensures that the given field hydration function is only
       every applied once to the given object. This is necessary to ensure
       that the prices are properly converted to the correct format when
       being sent between the client and the server """

    def wrapper(*args, **kwargs):
        """ Assumes that the first argument passed is the field, and the 
            second argument passed in is the bundle """
        field, bundle = args

        # If the field has not already been hydrated, set the hydration flag
        # for that field and run the hydration function
        if not hasattr(bundle, field+"_hydrated"):
            setattr(bundle, field + "_hydrated", True)
            return hydrate_function(*args, **kwargs)

        # Otherwise just return the original bundle
        return bundle

    return wrapper
