<h1 align=center >WRECK THAT ONE PITCH LIKE RALPH</h1>

<p align=center >Created by Keith James on the 17th September 2021</p>

<p align="center"> This project was created with Python version 3 </p>

===============================================================================================================
<p align="left"> <a href="https://github.com/ryo-ma/github-profile-trophy"><img src="https://github-profile-trophy.vercel.app/?username=freestyletear" alt="freestyletear github profile trophy's" /></a> </p>

[![GitHub Issues](https://img.shields.io/github/issues/freestyletear/top-pic)](https://freestyletear.github.io/on-the-spot/issues)

## Description

One Minute Pitch is a web application that will allow users to post pitches, like, dislike and comment on other pitches.

## Languages and Tools

[<img src="https://www.python.org/static/opengraph-icon-200x200.png" alt="python" width="100" height="70"/>](https://www.w3schools.com/python/default.asp "python 3")
[<img src="https://e7.pngegg.com/pngimages/654/56/png-clipart-flask-web-framework-python-software-framework-jinja-flask-miscellaneous-monochrome-thumbnail.png" alt="flask" width="100" height="70"/>](https://flask.palletsprojects.com/en/2.0.x/ "flask")
[<img src="https://cdn-images-1.medium.com/max/1200/1*Zkhl4Zz43z2_iR_ADlP-rg.png" alt="google" width="70" height="70"/>](https://www.google.com/ "google")
[<img src="https://github.githubassets.com/images/modules/open_graph/github-octocat.png" alt="github" width="100" height="70"/>](https://docs.github.com/en "github")
[<img src="https://uploads.sitepoint.com/wp-content/uploads/2016/04/1461122387heroku-logo.jpg" alt="flask" width="100" height="70"/>](https://www.heroku.com/about "heroku")
[<img src="https://www.opensourceagenda.com/projects/flask-bootstrap/image.png" alt="flask" width="100" height="70"/>](https://pythonhosted.org/Flask-Bootstrap/ "flask_bootstrap")
[<img src="https://d1nhio0ox7pgb.cloudfront.net/_img/g_collection_png/standard/512x512/html_tag.png" alt="github" width="100" height="70"/>](https://www.w3schools.com/html/html_intro.asp "html")
[<p>Fake email account</p>](https://emailfake.com/)
[<p>CSS</p>](https://www.w3schools.com/css/)
[<p>Postgressql</p>](https://www.postgresql.org/)


## Features
- The home page allows users to see various pitches from the following Categories:
    - Interview
    - Promotion
    - Product
    - Business
- User can see all pitches for that category chosen.
- Users create an account and receive a welcome message in their email.
- Once registered a user can log in and have additional capabilities including:
    - A user can like and dislike a pitch but only once.
    - Users can additionally comment more than once on other pitches.
    - Users can as well create their own pitch.


<p><img align="center" src="https://github-readme-stats.vercel.app/api/top-langs?username=freestyletear&show_icons=true&locale=en&layout=compact&theme=cobalt" alt="freestyletear github status on top languages used" /></p>

<p>&nbsp;<img align="center" src="https://github-readme-stats.vercel.app/api?username=freestyletear&show_icons=true&locale=en&theme=cobalt" alt="freestyletear github status on extra pins" /></p>

<p><img align="center" src="https://github-readme-streak-stats.herokuapp.com/?user=freestyletear&show_icons=true&theme=cobalt" /></p>

## SetUp / Installation Requirements

- Clone this repository to a location in your file system. `git clone https://github.com/freestyletear/wreck-that-one-pitch-like-ralph.git`
- Open terminal command line then navigate to the root folder of the application. `cd wreck-that-one-pitch-like-ralph`

  - On the terminal enter
      ```
      $ git init
      ```
  - Then create a virtual enviroment depending with the python version you have it has to be above 3.0.0
      ```
      $ python3 -m venv --without-pip virtual
      ```
      - Or
        ```
        $ python3 -m venv virtual
        ```
  - Lets activate the enviroment (_virtual_ is just a word you can use any as long as you remember)
      ```
      $ source virtual/bin/ativate
      ```
  - Read the specs and requirements files and Install all the requirements.
  - Install dependancies that will create an environment for the app to run:
       ```
       $ pip3 install -r requirements
       ```
  - Edit the start.sh file to prepare your environment variables:
        export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitchit'
        export SECRET_KEY='Your secret key'
        export MAIL_USERNAME='Your email'
        export MAIL_PASSWORD='Your email password'
  - Run database migrations:
        python manage.py db init
        python manage.py db migrate -m "initial migration"
        python manage.py db upgrade
  - Run chmod a+x start.py
  - Run ./start.py
  - Note this will work if you've properly configured your app with the required dependencies 
  - Access the application through `localhost:5000`


  ## Behavior Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| View All Pitches based on various categories | Default Home Page <br> Click on a category to see pitches | Displays all pitches |
| Register as a user | Click `register` on the navbar | Redirects to registration page to sign up |
| Log in as a user | Click on `log in` | Redirects to log in page |
| Update your Profile | Click on `Profile` | Redirects to profile page where you can update your bio and profile picture |
| Create a pitch | Click on `Add Pitch` on the home page or `Pitch` on the navbar | Redirects to pitches form page where you may create a pitch|
| Like or dislike a Pitch | Click on `Like` or `Dislike` button when logged in | Adds likes and dislikes to a pitch  |
| Comment on a pitch | Click on  `Comment`| Redirects to the Comments page where you can comment on other pitches and see other comments |

## Additional Requirements

- Git
- Web-browser or your choice
- Github
- Pip
- Python 3+


- Navigate to `http://localhost:5000/` in your browser.

- Live link to view the project <a target="_blank" href="https://wreck-that-one-pitch-like-ralph.herokuapp.com/">WRECK THAT ONE PITCH LIKE RALPH</a>

>Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo reach out to (https://github.com/freestyletear/wreck-that-one-pitch-like-ralph/fork)
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request

## Known Bugs / Feature Request

* If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/freestyletear/wreck-that-one-pitch-like-ralph/issues/new) by including your search query and the expected result.
* If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/freestyletear/wreck-that-one-pitch-like-ralph/issues/new) Please include sample queries and their corresponding result.


## Sources

- 👨‍💻<p align="left"> <img width="800" height="300" src="" alt="" /> </p>


---

## To-do
1. Add fuctionality andstyling.
2. Yet to complete all tests for each model class. If you have ideas you may contribute to this project.

## 📫 Support and contact details

- portfolio https://keithjames-portfolio-version-two-2a6267.netlify.app/
- Main email address **_wreckthatonepitchlikeralph@gmail.com_**
- Assist-email addressess **_keithjame@gmail.com_** <br>  **_freestyletear@gmail.com_**
- phone: _Airtel-Kenya_ :- ~+254788507559~

| [Linkedin](https://www.linkedin.com/in/keith-james-34a3041ba/) |
[Facebook](https://web.facebook.com/keithjamesmerchantmagnifico/) |
[Instagram](https://www.instagram.com/freestyletear/) |
[Twitter](https://twitter.com/KeithJa90059609) |
[Tik-tok](https://www.tiktok.com/@keithjames_themerchant?lang=en) |

---
### License

*MIT*
Copyright (c) 2021 **Keith James**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---