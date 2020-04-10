# ------------------------------------------------------------------------------
# import packages --------------------------------------------------------------
# ------------------------------------------------------------------------------

import base64
import webbrowser
import json
import sys
import pandas as pd
import numpy as np


# ------------------------------------------------------------------------------
# settings ---------------------------------------------------------------------
# ------------------------------------------------------------------------------

# ---- find your Qualtrics IDs
# https://www.qualtrics.com/support/integrations/api-integration/finding-qualtrics-ids/

qualtrics_data_center = 'YOUR DATA CENTER' # example: duke.qualtrics.com
survey_id = 'YOUR SURVEY ID' # example: SV_eBvCXzEVA9KoIPr


# ------------------------------------------------------------------------------
# inputs -----------------------------------------------------------------------
# ------------------------------------------------------------------------------

sub_id = sys.argv[1]
experimental_condition = sys.argv[2]
food1 = sys.argv[3]
food2 = sys.argv[4]


# ------------------------------------------------------------------------------
# format data for URL (needs to be flat) ---------------------------------------
# ------------------------------------------------------------------------------

# ---- IMPORTANT: in order for variables to get passed to Qualtrics, you must
# ---- define them as embedded variables. In my example, subject_id, experimental_condition,
# ---- food1, and food2 are all defined in the survey.
# ---- https://www.qualtrics.com/support/survey-platform/survey-module/survey-flow/standard-elements/embedded-data/

# create a flat series
json_payload = pd.Series({'subject_id': sub_id,
                          'experimental_condition': experimental_condition,
                          'food1': food1,
                          'food2': food2})


# ------------------------------------------------------------------------------
# create link from data --------------------------------------------------------
# ------------------------------------------------------------------------------

# ---- encode the json file to be added to the URL
encoded_payload = base64.b64encode(bytes(json_payload.to_json(), 'utf-8')).decode('utf-8')
# ---- concatenate strings to generate a final link (as a str)
link = 'https://' + qualtrics_data_center + '/jfe/form/' +\
        survey_id + '?Q_EED=' + encoded_payload
# ---- open link in browser
webbrowser.open_new(link)
