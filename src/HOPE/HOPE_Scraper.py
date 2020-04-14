# Standard Imports
from urllib.request import Request, urlopen
# Third Party Imports
# Local Imports
from HOPE_Logger import log_a_string, Log_Cats


class HOPE_Scraper:
    """
        PURPOSE - Request, parse, and read a URL
    """

    def __init__(self, target_url, user_agent=None):
        """
            PURPOSE - HOPE_Scraper constructor
            PARAMETERS
                target_url - URL to contact
                user_agent - Non-empty string to use as the user agent
        """
        # ATTRIBUTES
        self._url = target_url         # URL to contact
        self._user_agent = user_agent  # Request(headers={'User-Agent':self._user_agent})
        self._request = None           # urllib.request.Request object
        self._response = None          # urllib.request.urlopen response
        self._char_set = None          # Determine the character set from self._response
        self._content_bytes = None     # Byte string holding page content
        self._content_string = None    # String holding decoded page content

    def do_it(self):
        # VALIDATE
        self._validate_attributes()

        # DO IT
        # Request the URL
        self._request_the_url()
        # Determine the character set
        self._determine_charset()
        # Read response content
        self._read_response_content()
        # Decode response content
        self._decode_response_content()

    def _validate_attributes(self):
        # INPUT VALIDATION
        # self._url
        if not isinstance(self._url, str):
            raise TypeError('The user_agent parameter must be a string instead of '
                            f'{type(self._url)}')
        elif not self._url:
            raise ValueError('The target_url parameter may not be empty')
        # self._user_agent
        if self._user_agent:
            if not isinstance(self._user_agent, str):
                raise TypeError('The user_agent parameter must be a string instead of '
                                f'{type(self._user_agent)}')
            elif not self._user_agent:
                raise ValueError('The user_agent parameter may not be empty')

    def _request_the_url(self):
        """
            PURPOSE - Open a URL
            SETS _request with a urllib.request.Request object
            NOTES
                - Does not perform input validation
        """
        # LOCAL VARIABLES
        defined_headers = {}

        # REQUEST IT
        # Setup headers
        if self._user_agent:
            defined_headers['User-Agent'] = self._user_agent
        # Send request
        log_a_string(f'Sending request to {self._url}', Log_Cats.DEBUG)
        self._request = Request(self._url, headers=defined_headers)
        # print(self._request)  # DEBUGGING
        # print(self._request.headers)  # DEBUGGING
        # Check request
        if not self._request:
            raise RuntimeError('Request failed to return an object without raising an Exception')

        # GET IT
        log_a_string(f'Fetching response from {self._url}', Log_Cats.DEBUG)
        self._response = urlopen(self._request)
        # Check request
        if not self._response:
            raise RuntimeError('urlopen failed to return a response without raising an Exception')
        # print(self._response)  # DEBUGGING
        # print(self._response.headers)  # DEBUGGING
        # print(dir(self._response))  # DEBUGGING

    def _determine_charset(self):
        """
            PURPOSE - Determine the character set web content was encoded in
            SETS _char_set
            NOTES
                - Defaults to UTF-8
        """
        # LOCAL VARIABLES
        temp_char_set = None
        # print(self._response.headers)  # DEBUGGING
        content_type = self._response.getheader('Content-Type')

        # DETERMINE CHARSET OF PAGE
        log_a_string(f'Determining character set of {self._url}', Log_Cats.DEBUG)
        # print(content_type)  # DEBUGGING
        if content_type.find('=') < 0 or content_type.find('charset') < 0:
            self._char_set = 'UTF-8'
        else:
            content_type = content_type[content_type.find('charset'):]
            temp_char_set = content_type[content_type.find('=') + 1:]
            temp_char_set = temp_char_set.replace(' ','')
            self._char_set = temp_char_set
        # print(self._char_set)  # DEBUGGING

    def _read_response_content(self):
        log_a_string(f'Reading content of {self._url}', Log_Cats.DEBUG)
        self._content_bytes = self._response.read()
        # Check content
        if not self._content_bytes:
            raise RuntimeError(f'Failed to read byte content from {self._url}')
        # print(self._content_bytes)  # DEBUGGING

    def _decode_response_content(self):
        log_a_string(f'Decoding content as the {self._char_set} character set', Log_Cats.DEBUG)
        self._content_string = self._content_bytes.decode(self._char_set)
        # print(self._content_string)  # DEBUGGING
