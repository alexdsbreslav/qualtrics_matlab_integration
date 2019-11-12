# ------------------------------------------------------------------------------
# import packages --------------------------------------------------------------
# ------------------------------------------------------------------------------

import os
import requests
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
api_token = 'YOUR API TOKEN' # example: NEeEIn2Pr7CKsMOKPq5ecgXXxpWJkljPuJeJAYnF
survey_id = 'YOUR SURVEY ID' # example: SV_eBvCXzEVA9KoIPr


# ------------------------------------------------------------------------------
# inputs -----------------------------------------------------------------------
# ------------------------------------------------------------------------------

qualtrics_response_id = sys.argv[1]


# ------------------------------------------------------------------------------
# call Qualtrics API -----------------------------------------------------------
# ------------------------------------------------------------------------------

# ---- define url for request call
url = 'https://' + qualtrics_data_center + '/API/v3/surveys/' +\
        survey_id + '/responses/' + str(qualtrics_response_id)
# ---- get data from API
response = requests.get(url, headers={'X-API-TOKEN': api_token}).text


# ------------------------------------------------------------------------------
# reformat data ----------------------------------------------------------------
# ------------------------------------------------------------------------------

# ---- convert text string dictionary
response = json.loads(response)
# ---- get past the metadata/move down into the survey results (flattens dictionary)
response = response['result']['values']
# ---- convert flat dictionary into pandas Series
response = pd.Series(response)
# ---- get the question responses + ID variables
subject_id = response['subject_id']
experimental_condition = response['experimental_condition']
ratings = response[['QID1_' + str(i) for i in range(1,6)]]
# ---- replace qualtrics question IDs with meaningful ones
ratings.index = ['Apples', 'Gummies', 'KitKats', 'PopChips', 'Beets']
# ---- reformat so it is easy for readtable to work in MatLab
output = pd.DataFrame({'subject_id': subject_id,
                       'experimental_condition': experimental_condition,
                       'foods': ratings.index,
                       'ratings': ratings}).set_index('subject_id')


# ------------------------------------------------------------------------------
# export data ------------------------------------------------------------------
# ------------------------------------------------------------------------------

# ---- get the directory one level up from the current file
directory = os.path.dirname(os.path.abspath(''))
# ---- get the filepath for the current subject's raw data
export_path = os.path.join(directory, 'raw_data', 'sub'+str(response.subject_id))
# ---- create a csv so matlab can read it
output.to_csv(os.path.join(export_path, 'food_ratings.csv'))
