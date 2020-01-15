# Integrating Qualtrics With Your Behavioral Experiment.
This is an explanation and toy example for how to integrate Qualtrics with you behavioral experiment. My behavioral experiment is written in MATLAB; however, this is relevant (and honestly easier) for those using Psychopy or other Python based experiment tools.

**See "slides_integrating_qualtrics_MATLAB" for:**
- A more in depth explanation of use cases.
- The workflow for how to go through the example.

**Requirements:** 
- MATLAB 9.4
- MATLAB Toolbox: Statistics and Machine Learning Toolbox 11.3
- A Qualtrics account
- Python 3 with pandas and numpy

**Before trying to run through the example:**
- Import the two surveys into your Qualtrics survey library [[click here for directions]](https://www.qualtrics.com/support/survey-platform/my-projects/creating-a-project/#CreatingFromAFile)
- Update the settings in:
  - In participant_log.xlsx, update: your survey_link
  - In matlab_to_qualtrics.py, update: your qualtrics_data_center, your survey_id
  - In qualtrics_to_matlab.py, update: your qualtrics_data_center, your api_token, your survey_id
  - In start.m, update: your python path
  
If you would like to get a closer look at what the python scripts are doing, I have also provided them as Jupyter Notebooks.


Please reach out with any questions, concerns, or suggestions!
**alexander.breslav@duke.edu**
