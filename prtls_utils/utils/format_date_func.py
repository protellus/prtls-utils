from datetime import datetime, date
from typing import Union, Dict

def format_date(input_date: Union[str, date], output_format: str = "%Y-%m-%d") -> Dict[str, str]:
    """
    Converts a date input (string or date object) to a specified string format.

    This function accepts a date in the form of a string (formatted as 'YYYY-MM-DD')
    or a `date`/`datetime` object and returns a dictionary containing either the
    formatted date string or an error message.

    Args:
        input_date (Union[str, date]): The input date to process. If a string is provided,
                                       it must be in the 'YYYY-MM-DD' format.
        output_format (str): The desired output date format, specified using
                             `strftime` format codes (default is '%Y-%m-%d').

    Returns:
        Dict[str, str]: A dictionary containing one of the following keys:
                        - 'formatted_date': The date formatted as a string according
                          to `output_format`.
                        - 'error': An error message indicating what went wrong.

    Examples:
        >>> format_date('2025-03-09', '%B %d, %Y')
        {'formatted_date': 'March 09, 2025'}

        >>> format_date(date(2025, 3, 9), '%A, %d %B %Y')
        {'formatted_date': 'Sunday, 09 March 2025'}

        >>> format_date('09-03-2025')
        {'error': 'Invalid date format. Expected YYYY-MM-DD.'}

        >>> format_date(12345)
        {'error': 'Invalid type for input_date. Expected string or date object.'}
    """
    if isinstance(input_date, (date, datetime)):
        try:
            formatted_date = input_date.strftime(output_format)
            return {"formatted_date": formatted_date}
        except ValueError as e:
            return {"error": f"Invalid output_format: {e}"}

    elif isinstance(input_date, str):
        try:
            parsed_date = datetime.strptime(input_date, "%Y-%m-%d")
            try:
                formatted_date = parsed_date.strftime(output_format)
                return {"formatted_date": formatted_date}
            except ValueError as e:
                return {"error": f"Invalid output_format: {e}"}
        except ValueError:
            return {"error": "Invalid date format. Expected YYYY-MM-DD."}

    else:
        return {"error": "Invalid type for input_date. Expected string or date object."}
