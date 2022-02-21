from django.core.exceptions import ValidationError

def file_size(value,size=1):
    limit=size* 1024 * 1024
    if value.size > limit:
        raise ValidationError(f"File is too large, should not excced {size}MB")

from dateutil.relativedelta import relativedelta
from datetime import datetime

def yearsago(years, from_date=None):
    # if from_date is None:
    #     from_date = datetime.now().date()
    # return from_date - relativedelta(years=years)
    pass