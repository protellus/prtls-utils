from datetime import datetime, date
from typing import Union

def format_date(input_date: Union[str, date], output_format: str = "%Y-%m-%d") -> str:
    """
    Converts a date input (string or date object) to a specified string format.

    Args:
        input_date (Union[str, date]): The input date to process. If a string is provided,
                                       it must be in the 'YYYY-MM-DD' format.
        output_format (str): The desired output date format, specified using
                             `strftime` format codes (default is '%Y-%m-%d').

    Returns:
        str: The date formatted as a string according to `output_format`.

    Raises:
        ValueError: If `input_date` is a string not in 'YYYY-MM-DD' format or if
                    `output_format` is invalid.
        TypeError: If `input_date` is neither a string nor a date object.

    Examples:
        >>> format_date('2025-03-09', '%B %d, %Y')
        'March 09, 2025'

        >>> format_date(date(2025, 3, 9), '%A, %d %B %Y')
        'Sunday, 09 March 2025'

        >>> format_date('09-03-2025')
        Traceback (most recent call last):
            ...
        ValueError: Invalid date format. Expected YYYY-MM-DD.

        >>> format_date(12345)
        Traceback (most recent call last):
            ...
        TypeError: Invalid type for input_date. Expected string or date object.
    """
    if isinstance(input_date, (date, datetime)):
        try:
            return input_date.strftime(output_format)
        except ValueError as e:
            raise ValueError(f"Invalid output_format: {e}")

    elif isinstance(input_date, str):
        try:
            parsed_date = datetime.strptime(input_date, "%Y-%m-%d")
            try:
                return parsed_date.strftime(output_format)
            except ValueError as e:
                raise ValueError(f"Invalid output_format: {e}")
        except ValueError:
            raise ValueError("Invalid date format. Expected YYYY-MM-DD.")

    else:
        raise TypeError("Invalid type for input_date. Expected string or date object.")
