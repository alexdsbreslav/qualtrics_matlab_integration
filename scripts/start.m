function start(subject_id, qualtrics_response_id)
    if ismac == 0
        disp(['WARNING: This script was written on a Mac and is not currently compatible with PCs. ' ...
        'You will need to update the file path conventions and possible other settings.'])
        return;
    end

    % --------------------------------------------------------------------------
    % settings -----------------------------------------------------------------
    % --------------------------------------------------------------------------

    % ---- python path;
    python_path = 'YOUR PYTHON PATH HERE';
    % I use Anaconda to run Python + Jupyter Notebook, so my python path looks like:
    % python_path = '/Users/the_username_on_my_mac/anaconda3/envs/my_environment_name/bin/python'


    % ---- if the python path has spaces in it, add ""
    if sum(isspace(python_path)) > 0
        python_path = ['"' python_path '"'];
    end


    % --------------------------------------------------------------------------
    % create a file directory --------------------------------------------------
    % --------------------------------------------------------------------------

    % ---- get file path
    directory = fileparts(pwd);
    file_root = [directory '/raw_data'];

    % ---- create subject folder in the raw data folder
    filename_subnum = pad(num2str(subject_id), 4, 'left', '0');
    data_file_path = [file_root '/sub' filename_subnum];
    mkdir(data_file_path);


    % --------------------------------------------------------------------------
    % run the python script-----------------------------------------------------
    % --------------------------------------------------------------------------

    % ---- run the script in the terminal
    script_path = [directory '/scripts/qualtrics_to_matlab.py'];

    % ---- if the script path has spaces in it, add ""
    if sum(isspace(script_path)) > 0
        script_path = ['"' script_path '"'];
    end

    cmd_string = [python_path ' ' script_path ' ' qualtrics_response_id];
    system(cmd_string);

    % ---- read the results into MatLab
    food_ratings = readtable([data_file_path '/food_ratings.csv']);


    % --------------------------------------------------------------------------
    % do whatever you need to do in matlab--------------------------------------
    % --------------------------------------------------------------------------

    experimental_condition = food_ratings.experimental_condition{1};

    pick_two_foods = randsample(food_ratings.foods,2);
    food1 = pick_two_foods{1};
    food2 = pick_two_foods{2};


    % --------------------------------------------------------------------------
    % send information back out to Qualtrics------------------------------------
    % --------------------------------------------------------------------------

    script_path = [directory '/scripts/matlab_to_qualtrics.py'];

    % ---- if the script path has spaces in it, add ""
    if sum(isspace(script_path)) > 0
        script_path = ['"' script_path '"'];
    end

    cmd_string = [python_path ' ' script_path ' ' ...
                  subject_id ' ' experimental_condition ' ' food1 ' ' food2];
    system(cmd_string);
