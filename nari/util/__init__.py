from datetime import datetime

# Date is in the format of: YYYY-MM-DDTHH:MM:SS.MSZ
# e.g., 2020-05-18T20:12:06.1940000-05:00
DEFAULT_DATE_FORMAT='%Y-%m-%dT%H:%M:%S.%f%z'


def timestamp_from_datestr(datestr: str) -> datetime:
    # TODO: Act uses a funky sub-second format. Work it out.
    # return datetime.strptime(datestr, DEFAULT_DATE_FORMAT)
    # Yes, I know this is wrong
    return datestr