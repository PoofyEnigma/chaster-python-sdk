import datetime
import dateutil.parser
import functools
import warnings


def datetime_to_chaster_format(d: datetime.datetime) -> str:
    d.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
    return d.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-len('000')] + 'Z'


def safe_dump_time(src, key, out):
    if key in src.__dict__ and src.__dict__[key] is not None:
        out[key] = datetime_to_chaster_format(src.__dict__[key])


def safe_dump_parameter(src, key, out):
    if key in src.__dict__ and src.__dict__[key] is not None:
        out[key] = src.__dict__[key].dump()


def safe_update_parameter(src, key, out, update):
    if key in src.__dict__ and src.__dict__[key] is not None:
        out.__dict__[key] = update(src.__dict__[key])


def safe_update_time(src, key, out):
    return safe_update_parameter(src, key, out, dateutil.parser.isoparse)


def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.simplefilter('always', DeprecationWarning)  # turn off filter
        warnings.warn("Call to deprecated function {}.".format(func.__name__),
                      category=DeprecationWarning,
                      stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)  # reset filter
        return func(*args, **kwargs)

    return new_func
