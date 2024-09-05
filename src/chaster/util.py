import datetime
import dateutil.parser


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


class Country:
    def __init__(self):
        self.countryName: str = ''
        self.countryShortCode: str = ''

    def update(self, obj):
        self.countryName = obj.countryName
        self.countryShortCode = obj.countryShortCode
        return self

    def dump(self):
        return self.__dict__.copy()

    @staticmethod
    def update_array(obj):
        out = []
        for item in obj:
            out.append(Country().update(item))
        return out


class Region:
    def __init__(self):
        self.name: str = ''
        self.shortCode: str = ''

    def update(self, obj):
        self.name = obj.name
        self.shortCode = obj.shortCode
        return self

    def dump(self):
        return self.__dict__.copy()

    @staticmethod
    def update_array(obj):
        out = []
        for item in obj:
            out.append(Region().update(item))
        return out

    @staticmethod
    def dump_array(arr):
        out = []
        for item in arr:
            out.append(item.dump())
        return out


class CountryRegions(Country):
    def __init__(self):
        super().__init__()
        self.regions: list[Region] = []

    def update(self, obj):
        self.__dict__ = obj.__dict__.copy()
        if 'regions' in obj.__dict__:
            self.regions = Region.update_array(obj.regions)
        return self

    def dump(self):
        out = self.__dict__.copy()
        out['regions'] = Region.dump_array(self.regions)
        return out
