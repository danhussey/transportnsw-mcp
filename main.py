from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
# get api key from env

# Configure API key authorization: APIKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = os.getenv('OPEN_TRANSPORT_API_KEY')
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
configuration.api_key_prefix['Authorization'] = 'apikey'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
output_format = 'rapidJSON' # str | Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the `outputFormat` value to `rapidJSON` is required to enable JSON output. 
filter_date_valid = '18-03-2025' # str | This parameter allows you to filter the returned items that are only valid on the specified date. The format of this field is `DD-MM-YYYY`. For example, 12 September 2016 would be represented by `12-09-2016`.  (optional) (default to 01-10-2016)
filter_mot_type = 56 # int | This parameter allows you to filter the returned items by the modes of transport they affected. Available modes include:  * `1`: Train * `2`: Metro * `4`: Light Rail * `5`: Bus * `7`: Coach * `9`: Ferry * `11`: School Bus  To search for more than one mode, include the parameter multiple times.  (optional)
filter_publication_status = 'filter_publication_status_example' # str | This field can be used so only current alerts are returned, and not historic alerts.  (optional)
itd_l_pxx_sel_stop = 'itd_l_pxx_sel_stop_example' # str | This parameter allows you to filter the returned items by its stop ID or global stop ID. For example, to retrieve items that are only relevant to Central Station, you would set this value to `10111010` (stop ID) or `200060` (global stop ID). You can use the `stop_finder` API call to determine the ID for a particular stop.  (optional)
itd_l_pxx_sel_line = 'itd_l_pxx_sel_line_example' # str | This parameter allows you to filter the returned items by line number. For example, `020T1`. You can use this parameter multiple times if you want to search for more than one line number.  (optional)
itd_l_pxx_sel_operator = 'itd_l_pxx_sel_operator_example' # str | This parameter allows you to filter the returned items by operator ID. You can use this parameter multiple times if you want to search for more than one line number.  (optional)
filter_pn_line_dir = 'filter_pn_line_dir_example' # str | This parameter allows you to filter the returned items by specific routes. The route is provided in the format `NNN:LLLLL:D`, (NNN: subnet, LLLLL: Route number, D: direction `H`/`R`). You can use this parameter multiple times if you want to search for more than one line number.  (optional)
filter_pn_line_sub = 'filter_pn_line_sub_example' # str | This parameter allows you to filter the returned items by specific routes. The route is provided in the format `NNN:LLLLL:E`, (NNN: subnet, LLLLL: Route number, E: supplement). You can use this parameter multiple times if you want to search for more than one line number.  (optional)
version = '10.2.1.42' # str | Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  (optional) (default to 10.2.1.42)

try:
    # Provides capability to display all public transport service status and incident information (as published from the Service Alert Messaging System).
    # api_response = api_instance.tfnsw_addinfo_request(output_format, filter_date_valid=filter_date_valid, filter_mot_type=filter_mot_type, filter_publication_status=filter_publication_status, itd_l_pxx_sel_stop=itd_l_pxx_sel_stop, itd_l_pxx_sel_line=itd_l_pxx_sel_line, itd_l_pxx_sel_operator=itd_l_pxx_sel_operator, filter_pn_line_dir=filter_pn_line_dir, filter_pn_line_sub=filter_pn_line_sub, version=version)
    
    # Example api response with only date filter
    # api_response = api_instance.tfnsw_addinfo_request(output_format, filter_date_valid=filter_date_valid)

    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tfnsw_addinfo_request: %s\n" % e)

# Demo function that gets all alerts for a specific date
def demo(date: str):
    api_response = api_instance.tfnsw_addinfo_request(output_format, filter_date_valid=date)
    return api_response


print(demo('18-03-2025'))