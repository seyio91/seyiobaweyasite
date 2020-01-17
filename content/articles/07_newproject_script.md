Title: New Project Script
Date: 2020-01-17 10:20
Category: Bash_Automation
Tags: bash, git
Slug: new-project-script
Author: Seyi Obaweya

One of the plans for 2020 is working on more projects and putting them on Github to share as well as act as a portofolio for prospective employers. i decided to reduce the barriers to achieving this goal by working on Tools to make my day to day tasks more efficient, Hence the newproject script.  
This tool aims to automate the process of starting a new project as well as forcing me to upload all my projects on github.  
  
##### The manual Process of Starting a Project is :  
- Navigate to your project folder and create new folder  
- Initialize GIT Repo in new Directory  
- Create a ReadMe file  
- Stage ReadMe File  
- Create First Commit  

##### on the Github Page  
- Create New Repo  
- Copy Origin Address  
- Add remote Origin to your project Directory  
  
  
I decided to automate this process using a bash script due to Linux being my preferred dev environment (Ubuntu WSL2). I however intend to later port the script to a python script to enable it work on numerous platforms. 

### New Project Script
This is a fairly easy script to understand, i will walk you through some of the snippets which could be useful for creating your own scripts  
To Skip to script usage click here <a href="#usage">here</a>  
GitHub Link to project is <a href="https://github.com/seyio91/newprojectscript" target="_blank">Here</a>
  
**Creating a Repo with the Github API**

    :::bash
    curl -u "${GITHUB_USERNAME}:${GITHUB_TOKEN}" https://api.github.com/user/repos -d '{"name":"'$REPO_NAME'"}' > /dev/null 2>&1
the curl command takes the url which consists of the github username, personal access token and repo name as the data to create the new repository
the output is passed to /dev/null so it is not displayed on the script as some json object is returned on success.  
  
**Setting Default Variables**    
  
    :::python  
    PROJECT_DIR=${PROJECT_DIR:-$DEFAULT_DIR}

this is used to set a default value to a variable, if the variable is not defined, it takes the 2nd value as its new value. A default_dir is hardcoded, if the Project_dir variable is not passed in to the script, the project_Dir variable takes the values of the default dir.

**Bash Functions**  
  
Bash functions work almost the same way as every other scripting language, it is used in the script to define repetitive tasks. 
An example is coloring functions for my error and success messages. The process of getting a colored text is below  

    :::bash
    normal="\033[0m"
    greentext="\033[32m"

    echo -e $greentext"this color should be displayed as green to signify success"$normal

This quickly becomes stressful if you have to do it a couple of times.  
Defining a function which takes in an argument of message can be used to improve this.
note bash does take in arguments in the name definitions, this can be passed into the function using the `$1` arguments.   
Also the `local` keyword is used to make the variable local to the function so it does not change variables having the same name outside the function scope  

    :::bash
    success (){
        local msg=$1
        echo -e $greentext"$msg"$normal
    }

    success "this color should be displayed as green to signify success"

##### Other functions that were created are  
- `usage` : function to display error and how the script should be used. this is called at every conditions where the script will exit  
- `cleanup` : this is used to clean up files that were created if an error occurs after folders have been created in the script.  
- `nameCheck` : function to check if repo name meets the required conventions using regex.  
  
**Parsing Commandline Arguments**  
  
This is popular in most linux commands e.g cp -r source destination. the Minus sign are commandline arguments which are used to alter the default behavior of the script. Parsing of this argument is done through getopts.  

    :::bash
    while getopts "d:u:t:f:ih" option; do
        case "$option" in

        i ) INTERACTIVE=1;;
        d ) PROJECT_DIR=$OPTARG;;
        f ) REPO_FOLDER=$OPTARG;;
        u ) GITHUB_USERNAME=$OPTARG;;
        t ) GITHUB_TOKEN=$OPTARG;;
        h ) HELP=1;;
        \? ) usage
            ;;
        esac
    done
    shift $((OPTIND -1))

getopts will take a list of characters that it will accept, `"d:u:tf"`, each character that is followed by a `":"` will be accepting an argument, while others act as flags.  
example  

    :::bash
    newproject -d argumentforD -i  
`argumentforD` is passed as the argument for `d`, while `i` does not need any argument passed to it. The argument for D is stored in the `OPTARG` variable which can then be reassigned to your defined variable.
  
`$option` is the variable used to store the current character the while loop is on from the list of arguments. e.g it stores `-d` as d, which can then be checked in the case statement to carry out the corresponding action i.e set the variable in my case

case statement works the same way as every other language, the only difference here is the `\?` which is used to specify everyother character that i did not define in my case statement. my usage function is passed to trigger an error when an invalid character is passed  
  
the last part of the getopts is the `shift $((OPTIND -1))` statement. this helps in processing the arguments by shifting the current character that has been processed. e.g in example, after `-d` is processed, `-f` should be processed.  
  
    
for more info about the getopts command: <a href="https://www.shellscript.sh/tips/getopts/" target="_blank" >Here</a>


**Tests**  
Various Tests were used all through the script. the basic syntax for the tests is  
  
**if** 

    :::bash
    if [[ sometest ]]; then
        some action
    fi

**if else statement**

    :::bash
    if [[ sometest ]]; then
        some action
    else
        some other action
    fi

**if elseif**

    :::bash
    if [[ sometest ]]; then
        some action
    elif
        some other action
    fi

**Test Conditions**  
  
`[[ -n *$VARIABLE ]]` # if a variable is set. `! -n $VARIABLE` is for the reverse case. not set  
  
`[[ -d $VARIABLE ]]` check if $value is a folder  
  
`[[ -e $VARIABLE ]]` check if folder/file exist  
  

`[[ $VARIABLE = "somevalue" ]]` if specific condition is met  
bash uses "=" rather than the double equal sign in most languages.  
  

`[[ $VARIABLE =~ [$someregexvariable] ]]` to check if value does not match regex.  
  
  
**Reading file input**  
  
this is used to drive the interactive part of the script.  
the read command is used to read input and pass to the variable passed to the command  

    :::bash
    echo -n "Enter Project Folder: (somedefault) : "
    read PROJECT_DIR
    echo $PROJECT_DIR
    
    "Enter Project Folder: (somedefault) : /home/seyi/projectfolder" 
    "/home/seyi/projectfolder"

<div id="usage"></div>   
  
### Dependencies  
 **Github personal access token** is required to create repo as well as making commits. Link on Creating your Personal Access Token is <a href="https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line" target="_blank">Here</a>.  
**JQ Program** for parsing responses from the git api. This checks if there is an existing repo with the same name on users github page   
    
**Installing JQ Dependency**  
  
for debian  

    :::python
    sudo apt-get install jq  
  
for redhat

    :::bash
    sudo yum install jq  
  
    
### Usage  

    :::python
    "Usage: newproject [ -i | -d | -f | -u | -t | -h ] repo_name"  
    "-i : Interactive Prompt"   
    "-d : Projects Directory" 
    "-f : Folder for Storing Repo"  
    "-u : Github Username"  
    "-t : Github Personal Access Token"  
    "-h : Help"  

**Basic Usage**  

    :::bash
    newproject reponame  
newproject script will create folder with the reponame in the directory set in the DEFAULT_DIR variable.  
  
    :::bash
    newproject -d /home/system/opt -f newfolder reponame  
Project folder "newfolder" will be created in the directory passed to -d flag.  
  
    :::bash
    newproject -u seyio91 -t dummy_token reponame  
username and token will overwrite the variables exported to shell environment during setup  
  

    :::bash
    newproject -i reponame  
Starts the interactive session

    :::bash
    newproject -i reponame
    "Enter project Default Folder: (/home/seyi/projects)"  
    "Enter project Folder- Repo name will be used if no default:  ()"  
    "Enter Git Username:  (seyio91)"  
    "Enter Git Token:  (dummy_token)"  
  
To view help options  

    :::bash 
    newproject -h   
  

### Planned Improvements.  
- Specific Project Types. Ability to specify the type of project and create directory structure by project e.g creating virtual env for python or dockerfiles for docker projects  
- Add Testing


GitHub Link to project is <a href="https://github.com/seyio91/newprojectscript" target="_blank">Here</a>