Title: Creating my Personal Static Website with Pelican
Date: 2020-01-20 10:20
Category: Web_Development
Tags: python, pelican
Slug: my-personal-website-setup
Author: Seyi Obaweya
Summary: The process of creating a website can sometimes look daunting. There are a lot of over engineered options for running a simple blog. This article walks you through the use of Static Site generators which is known for its simplicity in creating a personal website. 
  

I am excited to share the process of creating my personal website which was made to document my projects, share my learning journey and probably act as a portfolio. There are so many choices for creating a website, with easy options like WordPress, blogger and other hosted solutions, however being someone who likes tinkering, I prefer to host a website myself to be able to customize and break it. This led to discovering Static Site Generators in my quest for simple and cost-effective solutions.


This seemed perfect as my blog will mainly be static HTML pages, giving me a variety of options for hosting. Another reason for choosing a static site generator was the ability to write content in Markdown removing the need for creating static pages by hand with HTML, which would be more effort than worth it. There are a ton of Static Site generators out there, List can be found <a href="https://www.staticgen.com/" target="_blank">here</a>.  

Eventually, I ended up choosing **Pelican** which is a python based Static Site Generator over other popular SSGs as python is my preferred scripting language making the setup and customization process easy for me. Also, pelican uses Jinja templating to generate its HTML which is straightforward and flexible

I would not go in-depth into Pelican site generators. The <a href="Documentation" target="_blank">documentation</a> is quite extensive and easy to understand.

The Article will be broken into the following Parts:  
## 
1. **Setting Up Pelican Site Generator** <-- this article
2. [Customizing your Site](#)
3. [Hosting your Static Site on AWS S3 Buckets](#)
4. [Creating your Pelican CD Pipeline using Travis](#)
5. [Buying a Domain name and Pointing the Domain to your Bucket](#)


It is quite shocking spinning up a website has become this easy, the total cost of the entire project has been $4 so far. The process of setting up this website is fast, simple and secure with the drawback of having the technical know-how. I hope this article simplifies the process.


## Project Set-Up  
**Installing a Python Virtual Environment**  
  
The first thing to do is preparing your python environment for the project, I use python virtual environments for my projects in other to perform some degree of isolation from other system projects

installing the virtual-env package for ubuntu  

    :::python
    sudo apt-get install python3-env 

installing the virtual-env package for centos  

    :::python
    sudo yum install python3-env 
  
    
Create a folder to hold your Virtual Environment. This will Act as your Project Root Folder

    :::python
    mkdir website-virtual-env
    python3 -m venv website-virtual-env

The above command installs some files in the project folder, Navigate into the activate the virtual environment with the command

    :::python
    cd website-virtual-env
    source bin/activate

**Installing Pelican Package**  
  
Pelican can be Installed in the Virtual Environment using the Command

    :::python
    pip install pelican[Markdown]

**Create Git repo for your Pelican Project**  
  
Create a new project using newproject script. link to article [here]({filename}/articles/02_newproject_script.md){:target="_blank"}.

    :::python
    newproject -d $HOME/currentdirectory/ -f site seyiobaweyasite

Alternatively, can create a new project manually using the following setps   
## 
- creating the project folder in the Virtual Environment and navigating to the directory  

        :::python
        mkdir seyiobaweyasite && cd seyiobaweyasite

- initialize git repo

        :::python
        git init
  
    
### Setting Up Pelican  
  
In the project folder, use the `pelican-quickstart` command to start a new Pelican project. This will open an interactive command session that would ask questions about your website.

    :::python
    $ pelican-quickstart

    Welcome to pelican-quickstart v3.4.0.

    This script will help you create a new Pelican-based website.

    Please answer the following questions so this script can generate the files
    needed by Pelican.

    $ Where do you want to create your new web site? [.] folder_to_use
    $ What will be the title of this web site? BlogName
    $ Who will be the author of this web site? Your Name
    $ What will be the default language of this web site? [en]
    $ Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) y
    $ What is your URL prefix? (see above example; no trailing slash) www.someexample.com
    $ Do you want to enable article pagination? (Y/n) y
    $ How many articles per page do you want? [10]
    $ Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) y
    $ Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) y
    $ Do you want to upload your website using FTP? (y/N) n
    $ Do you want to upload your website using SSH? (y/N) n
    $ Do you want to upload your website using Dropbox? (y/N) n
    $ Do you want to upload your website using Rackspace Cloud Files? (y/N) n
    $ Do you want to upload your website using GitHub Pages? (y/N) n
    Done. Your new project is available at home/projects/seyiobaweyasite


The Pelican Quick Start Command Generates the Following Project Structure 

    :::python
    $ tree -L 2
    .
    ├── content
    ├── Makefile
    ├── output
    ├── pelicanconf.py
    ├── publishconf.py
    └──tasks.py

  

  
`output` directory stores the static files (HTML/Images, PDF, ...) which are generated from the markdown content. These are the contents that are copied over to the directory/server hosting your site.  
  
`pelicanconf.py` is the main configuration file for pelican. view [link](http://docs.getpelican.com/en/3.6.3/settings.html){:target="_blank"} for more info. The settings you define in the configuration file will be passed to the templates, which allows you to use your settings to add site-wide content.  

    ::python
    AUTHOR = 'demo-author'  
    SITENAME = 'demo-site'  
    SITEURL = 'http://localhost:8000'   
    STATIC_PATHS = ['images', 'static']   
    
    other optional config  
    MAIN_MENU = True  
    USE_FOLDER_AS_CATEGORY = False  
    DISABLE_URL_HASH = True  
    SUMMARY_MAX_LENGTH = 30  
    DEFAULT_PAGINATION = 10  


`publishconf.py` the file should contain the production-specific settings you want to add to your site. the file imports the pelicanconf.py file and overwrites the settings that are changed for production. After you have reviewed your site in your local development environment, the site can be published to the production environment with this configuration  

`Makefile` file for UNIX users that contains convenience tasks for common operations such as running the development server, building the html pages. it acts as an automation wrapper for the pelican commands  
allows the following commands. The commonly use make commands are:  
## 
- `make html` is used to generate html pages from the content directory. Equivalent of `pelican content` command  
- `make serve` is a wrapper for `pelican --listen`. This serves the output directory on the default port `localhost:8000`. The command uses the default configuration file and port is no additional parameters are passed to it.  
- `make devserver` performs the same actions as the make serve command with the additional task of watching the content folder and regenerating the static pages automatically if any changes are made to the content folder.
- `make publish` is used to publish static pages using the `publishconf.py` file which containts production specific settings
  
The makefile can also be extended to perform users specific tasks such as creating an article template, building a new theme. (Future Post Consideration)



`content` directory is where your articles/pages are stored. Articles can be written in markdown, Restructured Text or HTML. For the sake of keeping my pages organized, contents are kept in folders in the content directory  
   
Sample content Structure

    :::python
    $ tree -L 3 content/

    content/
    ├── articles
    │   ├── 02-newcontent.md
    │   ├── 03_content.md
    │   ├── 04_content.md
    │   └── content-new.md
    ├── images
    │   ├── fav.png
    │   ├── python_icon.png
    │   ├── site_logo.jpeg
    │   └── test.jpeg
    ├── pages
    │   └── About-Me.md
    └── static
        └── custom.css

### Writing Content  
  
Content can be written in both Markdown and HTML syntax. I rather find markdown easy to use and sometimes infuse HTML elements in my markdown notes. The basic structure of a markdown article is found below. see the <a href="http://docs.getpelican.com/en/3.6.3/content.html" target="_blank">pelican documentation</a> for more info on writing content.  
The image below shows a sample article 

    :::text
    Title: My First Post  
    Date: 2020-01-17 10:20  
    Category: New_Posts  
    Tags: bash, git  
    Slug: my-first-post  
    Author: Seyi Obaweya  

    Article Body Lorem ipsum dolor sit amet consectetur adipisicing elit...

### Meta Data  
  
The article starts with a file metadata that pelican uses to get information about the article.  
### 
- `Title`: Heading of the blog post. is a required field for every Post  
- `Author`: Author of the blog post  
- `Date`: Date the article was published in the format YYYY-mm-dd hh:mm  
- `Category`: Used to Classify the Blog Post  
- `Tags`: This contains topics the post covers, separated by a comma  
- `Summary`: A one or 2 line summary of your post. Will be displayed on the index page. if this is not defined, Pelican Truncates your blog post to be used as the summary.  
- `Slug`: This will be the name of the HTML file generated. if not defined, Pelican uses the title separated by commas  
  
Other Metadata can be seen on the pelican documentation page  
  
### Main Body   
  
The Main Body of the Article follows the basic Markdown syntax. for more information on writing in markdown click [Here](https://www.markdownguide.org/basic-syntax/){:target="_blank"}

**Adding Static Files**  
  
Static Files such as images, documents can be linked to each article, by referencing the file location in markdown syntax. Pelican should be made aware of these locations by adding it to the STATIC_PATH variable in the pelicanconf.py file

    :::python
    vi pelicanconf.py  

    STATIC_PATHS = ['images', 'pdfs', 'static', 'zipfiles']  
## 
- **Images**  : `![some alternate text]({filename}/images/han.jpg)`   
some alternate text will be displayed if the image is not found. Also note, the static path folders are included in the "content" folder  
images can also be referenced using HTML syntax such as `<img src="/images/han.jpg">  `

  
- **Files**: For creating download links such as pdfs and zip files, Add the download location to static paths  
`[Our Menu]({static}/pdfs/menu.pdf)`  



**Adding Links**  
  
External links can be referenced using both markdown and HTML syntax  
Markdown: `[Link](https:\\www.someexample.com\)`  
  
HTML: `<a href="https:\\www.someexample.com\">link<\a>`  


internal links to contents like previous articles  
`[First Post]({filename}/articles/02-newcontent.md)`


**Adding code syntax highlighting**  
  
Pelican handles code syntax using the Markdown CodeHilite extension. To use this, include the language identifier just above the code block, indenting both the identifier and the code

Code Syntax without Line numbers

    :::python
    print("some code without line numbers.")

Code syntax with Line numbers

    #!python
    print("some code with line numbers.")


## Post-Content Creation  
  
After creating the new content, use the `pelican content` command to generate the HTML Pages. You can also use `make devserver` to generate HTML and serve the Page locally on your development environment.

Your content can now be viewed on `localhost:8000`


The Next Article on **Customizing your Site** can be found [Here](#)








