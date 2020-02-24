Title: Creating a Python Love Poem
Date: 2020-02-25 10:20
Category: Web_Development
Tags: python, cron, webscraping, api
Slug: python-love-poem
Author: Seyi Obaweya
Summary: We'll be writing a python script that sends messages to our loved ones every hour, reminding them how much they are loved. This will be done by scraping a website using the beautiful soup library, sending messages using the Twilio API, and the script is deployed on AWS lambda. 

<img src="/images/thumbnails/1000x400/valentine.jfif" alt="some alternate text">

# 
  
It's another Valentine's Day!!!. Lying down, thinking about doing something special for my loved one, being about 10000km away from her. After so much deliberation, sending a  WhatsApp reminder every hour, telling her how much I love her in different languages sounded like a fun and thoughtful idea.

# 

In this tutorial, we will be writing a script to sends a Whatsapp message every hour to a number and deploying our script on AWS lambda. This will be written in python as that is my preferred language, if you have an interest in getting a nodejs version, you can put that in the comments.

### Gettings Started!!  
  
   
The article is broken into 3 sections: 
# 
- **Automating Whatsapp Message sending using Python:** 
One option is to use Python's Selenium package to open the WhatsApp web interface on a browser and control using the selenium web driver. This introduces new challenges, as WhatsApp requires QR code scanning to use the web interface,  making automation impossible. The other option is using the Twilio WhatsApp API, which allows developers to build prototypes in a sandbox environment. The Sandbox uses by default, a shared number to send messages to recipients. Using a personal number requires an application to Whatsapp, which might take time to be approved. 
The script will be created using the Twilio API because it is best suited for our small scale project as it is easy to set up and can be automated

- **Creating Messages to send.** 
The aim is to send Love messages and also write `i love you` in different languages. A sequence of steps will be taken to accomplish this.  
1) Scraping Messages off the internet- Composing a lot of messages for the project would take a lot of time, so why not make use of the available resources all over the internet?. This is done by scraping a website using the python beautiful soup library  
2) Translating Messages to Random Languages - The Google Translate API will be used to get a random Language and translating our texts.

- **Deploying our app.**
We will be deploying our script to AWS lambda, which is a cloud computing service that runs small pieces of code functions without the need for a server. This will help reduce costs as it removes the need for provisioning and maintaining a server

- **Running the script periodically.**
This will be done using the Cron Utility on our development server, while AWS Lambda Triggers will be used after deployment.

<p align="center">
<img src="/images/twiliologo.png" alt="some alternate text">  
</p>

#  


### Sending Messages using the Twilio API  
The Twilio Whatsapp API is easy and quick to set up, using a shared phone number without waiting for a dedicated number to be approved by Whatsapp.
To get started with the Twilio API, visit the [twilio website](Twilio Website), Create a Free Twilio account and confirm your email and phone number  
# 

The only con to using this method is that the sandbox is pre-provision with a Whatsapp Number that is shared across all sandbox users.   
Also Note, Recipients have to go through a one-time permission process to receive messages. This works just fine for our small scale project. To activate the Twilio Sandbox. Navigate to Whatsapp Beta on the left side menu  
# 

<img src="/images/step5.PNG" alt="some alternate text">
<p style="text-align: center;"><b>Twilio Whatsapp Sandbox</b></p>

# 

A Phone Number and a Joining Message are provided, Save the number on your device and send the provided message from your device. This is a one time process for every Recipient using your script. 
  
  

<p align="center">  
<img src="/images/whatsappconfirmation.jpeg" alt="some alternate text">
<p style="text-align: center;"><b>Success Reply</b></p>
</p>
  
if successful, a reply is returned, The web interface also shows message received.  
screen shows received



**Creating the project**  

To view how the API works, visit the [API documentation to find the basic usage](https://www.twilio.com/docs/sms/whatsapp/api)


After logging into the Twilio Console, take note of your Account SID and Auth Token. The Account SID is a unique identifier for your account, while the Auth Token is a secret key that should never be shared or else anyone will have full access to your Twilio account.

<img src="/images/step7.PNG" alt="some alternate text">
<p style="text-align: center;"><b>Twilio DashBoard</b></p>

Copy both keys, as they will later be used for authenticating with the API in your script

**Create and activate a virtual environment for project isolation**

    :::bash

    $ python3 -m venv virtualenv
    $ cd virtualenv && . bin/activate

**Create a project folder and GitHub repository.**   

    :::bash

    $ mkdir twiliowhatsapp && cd twiliowhatsapp
    $ git init

OR
##  
**Automating the setup process using the [newproject script](somelink)**

    :::bash
    $ newproject twiliowhatsapp

**Install the Twilio python library**

    :::bash
    $ pip install Twilio

**Creating your project script**

    :::bash
    $ touch whatsappcode.py

**Copy and paste the code from the whatsapp API documentation**  
(Also replace the **sid** and **auth_token**, and **recipient phone number** with yours)

    :::bash

    from twilio.rest import Client
    account_sid = 'AC4bdca1b7084d0c29e62c381f60b8a041'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                from_='whatsapp:+14155238886',
                                body='Hello, there!',
                                to='whatsapp:<recipient-number>'
                            )

    print(message.sid)

You can test your script to get a message sent to the recipient number

    :::bash
    $ python whatsappcode.py

Voila!!!, a message is received on the recipient phone
  

### Securing our API keys on the development environment  

Hard coding the API keys to our script is bad practice because it exposes sensitive information to the public when committing your code to a public repository. A way to avoid this is to externalize the keys and read from the os environment at runtime.  
The Python dotenv package can be used to externalize our keys by searching for a .env file that will contain our keys, and exports the variables into our script. The .env file should also be added to a .gitignore file so it is ignored when uploading your code to the public repository.  
  
**Install the `python-dotenv` package**

    :::bash
    $ pip install python-dotenv

In the project folder, **create a .env file and add your sid and token**

    :::bash
    $ vi .env
    TWILIOSID=<your-sid>
    TWILIO_AUTH_TOKEN=<your-token>

**Add .env filename to the gitignore file** so that it ignored by git when you make your commit

    :::bash
    $ echo .env >> .gitignore

The next process is importing the variables into our code so we can remove the insecure keys. Add the following code to your script

    :::bash

    import os
    from dotenv import load_dotenv

    load_dotenv(override=True)
    # load_dotenv(override=True). Overwrites already set system environments.

    from twilio.rest import Client
    account_sid = os.environ.get('TWILIOSID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    ...

At this point, the key/value pairs in the .env file are now present as system environment variables and they can be conveniently accessed via os.environ.get() method.

**Run the script** again and you should get the message on WhatsApp if there are no errors.

Next verify your .env file is in the gitignore file, then commit your code to your repository

    :::bash
    $ git commit -m "Message Client Working"


### STEP 2 Composing your messages  
  

The next item on our list is getting the messages we want to send. This is divided into 3 parts
#  
-  Scraping the Page
- Getting a Random Language
- Translating your Text to the random Language
  
#### 1 Scraping the webpage
Even though most people think I am a romantic, composing multiple messages to send all through the day will be a tedious process. This led to the option of scraping messages off the tons of romantic messages online. For the script, we would be scraping off [serenea flowers](https://www.serenataflowers.com/pollennation/love-messages/) for their simple and thoughtful messages.

We will be using the BeautifulSoup python package to scrape the messages.  
# 
  
**Install the beautifulsoup and requests library** for making HTTP requests and scraping the page

    :::bash
    $ pip install bs4 requests

In your project folder,** create a new script for scraping the site and import the request and beautifulsoup library** into your file

    :::bash
    $ touch scraper.py && vi scraper.py

    from bs4 import BeautifulSoup as bs
    import requests

Next, make an HTTP request to the page we want to scrape and check for errors

    :::bash
    ...
    url = 'https://www.serenataflowers.com/pollennation/love-messages/'
    res = requests.get(url)
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        sys.exit(1)
    

If our request is successful, the HTML document is then passed to beautifulsoup to create a beautiful soup object which we can run the select and find methods on
    
    :::python

    soup = bs(res.text, features="html.parser")

We then select all the messages in the soup object. To do this, we need to first get the HTML element path of the messages. This can be done using the `inspect element` option in your web browser.  
# 

<img src="/images/step19.PNG" alt="some alternate text">  
<p style="text-align: center;"><b>Chrome Developer Tools</b></p>


# 

On viewing the developer console, the messages are nested inside a `<li>` tag within an `<ol>` tag with the class of `simple-list`. The HTML code for the message is represented in the following structure


    <ol class="simple-list">
        <li>Message we are trying to access 1</li>
        <li>Message we are trying to access 2</li>
        <li>Message we are trying to access 3</li>
        ...
    </ol>

To select all `<li>` tags within the **simple-list** class, we used the beautifulsoup `select()` method and save the list to a variable `listOfMessages`.

    :::bash
    listOfMessages = soup.select('.simple-list li') # the space is used to specify element exists inside the class

This returns a list of all `<li>` tags as beautifulsoup objects within the element.

    :::python
    print(listOfMessages)

    [<li>Message we are trying to access 1</li>, <li>Message we are trying to access 2</li>, <li>Message we are trying to access 3</li>]

To get the text in each element, the `text()` method is used to extract texts from the object

    :::python

    textMessages = [item.text for item in listOfMessages]

Now there is a list of messages to choose from. We only need a message from the list each time the script is run. this is where the python `random` module comes to our rescue. 

**Import the random library** at the beginning of the script, then use `random.choice()` method to get a random message from the list at each run.

    :::bash

    import random

    textMessages = [item.text for item in listOfMessages]
    randomQuote = random.choice(textMessages)

    print(randomQuote)

Our code can be converted into a function that can be imported into our main `whatsappcode.py` script. The final code should look like this

    :::bash
    from bs4 import BeautifulSoup as bs
    import requests, random

    def getMessage():
        url = 'https://www.serenataflowers.com/pollennation/love-messages/'
        res = requests.get(url)
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError:
            sys.exit(1)
        soup = bs(res.text, features="html.parser")
        listOfMessages = soup.select('.simple-list li')
        textMessages = [item.text for item in listOfMessages]
        return random.choice(textMessages)

    print(getMessage())


Every time we now run the script, a random message is generated. 


#### 2 Getting a Random Language
The second process in this step is getting a random language to be used in translating the words  "I love you". (i consider every other language to be much more romantic than English).  
The Google Translate API will be used in this step as I find it easy to use and free for our small scale project

To use the Google API, you'll have to sign up with Google Cloud and get a developer API key. [visit here for details](https://cloud.google.com/docs/authentication/api-keys)

**Add the key into the .env file** in your project folder to ensure the API key is not exposed in the script

    :::bash
    vi .env
    GOOGLEAPIKEY=<your-api-key>

The list of languages supported by Google Cloud can be accessed via the API `https://translation.googleapis.com/language/translate/v2/languages?key=<your-key>`


The request library will be used to access the API. This will return a JSON object, which will be parsed into a python dictionary using the JSON library.

    :::bash
    import your api key
    gApiKey = os.getenv('GOOGLEAPIKEY')
    langApiUrl = "https://translation.googleapis.com/language/translate/v2/languages"

The key is then passed as a parameter to the request

    :::bash
    langpayload = {'key': gApiKey}

    r = requests.get(langApiUrl, params=langpayload)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        print('Error: the Request failed.')
        sys.exit(1)
    
if the request is successful, a JSON object is returned which is then parsed using the `json.loads()` method

    :::bash
    response = json.loads(r.content.decode('utf-8-sig'))

we can then access the data from the converted python dictionary

    :::bash
    dest_language = random.choice(destResponse['data']['languages'])

    print(dest_language)

Every time the script is run, a different language should be displayed.


#### 3 Translating the text.
This is the same process as above, the only difference will be the URL and the parameters passed to requests library

    :::bash
    transUrl = 'https://translation.googleapis.com/language/translate/v2'

The translate API takes the following parameters
# 
- source language - English
- target - This will be the result of the random language generated above
- key - Your Google API key
- q - this will be the text we are translating

# 
    :::bash
    transPayload = {
            'source': 'en',
            'target': dest_language,
            'key': gtranslateApiKey,
            'q': urllib.parse.quote('I Love You')
    }

N.B. To pass the text into to the payload, the text has to be encoded as spaces have no corresponding character within the standard ASCII character set  `'q': urllib.parse.quote('I Love You')` 

The result of the earlier code block, generating the random language is passed as into the payload as the destination language for the API

    :::bash
    r = requests.get(transUrl, params=transPayload)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        print('Error: the Request failed.')
        sys.exit(1)
    transresponse = json.loads(r.content.decode('utf-8-sig'))

to get the translated text from the generated python dictionary

    :::bash
    msg = transResponse.get('data').get('translations')[0].get('translatedText')


On realizing there is a lot of repetition between the translated code and random language code block, a `_get_request` function, which takes in a URL and some parameters, will be created to handle the requests for both processes.

    :::bash
    def _get_request(url, payload):
        r = requests.get(url, params=payload)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            print('Error: the Request failed.')
            sys.exit(1)
        response = json.loads(r.content.decode('utf-8-sig'))
        return response
    
the `_get_request` function can then be used by adding the following to the script

    :::bash
    ...

    randomLangPayload = {'key': gtranslateApiKey}

    destResponse = _get_request(randomLangUrl, randomLangPayload)
    dest_language = random.choice(destResponse['data']['languages'])

    transPayload = {
        'source': 'en',
        'target': dest_language,
        'key': gtranslateApiKey,
        'q': urllib.parse.quote('I Love You')
    }

    transResponse = _get_request(transUrl, transPayload)
    msg = transResponse.get('data').get('translations')[0].get('translatedText')

Combining All

All the functions that have been created can be imported into the Twilio client script either by copying all the code into one file or importing the functions from files. we will be going with the first option to mirror our lambda deployment script which will be created in the next article.

Our scraped message and the translation of "I love you" is passed in as the message to the Twilio Client.

The whatsappcode.py script

    :::bash
    import json, sys, requests, random, os
    import urllib.parse
    from dotenv import load_dotenv
    from twilio.rest import Client
    from bs4 import BeautifulSoup as bs

    load_dotenv(override=True)

    # reading the environment variables
    account_sid = os.environ.get('TWILIOSID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    gtranslateApiKey = os.environ.get('GOOGLEAPIKEY')

    def getMessage():
        url = 'https://www.serenataflowers.com/pollennation/love-messages/'
        res = requests.get(url)
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError:
            sys.exit(1)
        soup = bs(res.text, features="html.parser")
        listOfMessages = soup.select('.simple-list li')
        textMessages = [item.text for item in listOfMessages]
        return random.choice(textMessages)

    def _get_request(url, payload):
        r = requests.get(url, params=payload)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            print('Error: the Request failed.')
            sys.exit(1)
        response = json.loads(r.content.decode('utf-8-sig'))
        return response

    transUrl = 'https://translation.googleapis.com/language/translate/v2'
    randomLangUrl = 'https://translation.googleapis.com/language/translate/v2/languages'

    client = Client(twiliosid, twiliotoken)

    randomLangPayload = {'key': gtranslateApiKey}

    destResponse = _get_request(randomLangUrl, randomLangPayload)
    dest_language = random.choice(destResponse['data']['languages'])

    transPayload = {
            'source': 'en',
            'target': dest_language,
            'key': gtranslateApiKey,
            'q': urllib.parse.quote('I Love You')
        }

    transResponse = _get_request(transUrl, transPayload)
    msg = transResponse.get('data').get('translations')[0].get('translatedText')

    randomquote = getMessage()
    msg = translate('I Love You', 'en', dest_language, gtranslateApiKey)
    fulltextmsg = randomquote + " \n P.S. " + msg


    message = client.messages.create(
                                from_='whatsapp:+14155238886',
                                body=fulltextmsg,
                                to='whatsapp:<your number>'
                            )
            
    return {
            'statusCode': 200,
            'body': message.sid
        }

### Running the Script Periodically.
This will not be a lengthy section as there are a lot of articles on cron usage. Here is a [good article on using Cron.](https://opensource.com/article/17/11/how-use-cron-linux/)
To run the script in cron, The python interpreter which the script will be using should be set by adding the path with a shebang at the top of the script.

To get your executable path, in your activate virtual environment

    :::bash
    $ which python

    /home/seyi/projects/bin/python

or Find the Path, which will always be located in the bin/ directory in your virtual environment

Add the Following to the first line in your code `#!<your-env-path>`

    :::bash
    #!/home/seyi/projects/bin/python

Please remember to change your path

After Adding the Interpreter to be used, convert your script to an executable. you will need sudo access to carry out this action

    :::bash
    $ sudo chmod +x scriptname.py

Also note the Full path to your script

    :::bash
    $ realpath yourscriptname.py

    /home/seyi/projects/whatsapp_val/whatsappCron.py

We then add this to crontab, to be run every hour during the day

    :::bash
    $ crontab -e

    0 */1 * * * /home/seyi/projects/whatsapp_val/whatsappCron.py


The script should be called at the start of the next hour and a Message will be sent to the recipient's number.

The next article will cover deploying your script to AWS lambda

**N.B.** Remember to remove your script from cron at the end of the day by commenting or deleting the line off cron, so you do not end up annoying the person you are sending the message to.

The Source code for the article can be found here