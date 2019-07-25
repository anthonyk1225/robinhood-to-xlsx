# robinhood-to-xlsx

## Environment

You are going to need / want to use
- Python - [The version of python that I use is 3.7.2](https://www.python.org/downloads/release/python-372/)
- pip (I happen to use pip3)
- sqlite3 - [Link to download on mac](https://tableplus.io/blog/2018/08/download-install-sqlite-for-mac-osx-in-5-minutes.html) (this is so you can interact with it in your terminal, not necessarily mandatory but recommended)
- Virtualenv - [I use version 16.4.3](https://virtualenv.pypa.io/en/latest/)

## Installation

After forking, cloning into wherever
`cooldude$ cd to/wherever/it/is`
`cooldude$ virtualenv venv`
`cooldude$ source venv/bin/activate`
`(venv) cooldude$ pip3 install -r requirements.txt`

## Setting up
- Create all tables - `(venv) madlad$ python3 sql/db.py`
- Update `email` & `password` in `credentials.py`
- Log in to robinhood in your browser and open up the inspector (cmd+option+i for mac users)
- Type `document.cookie` in the console and copy your `device_token`
- Update `device_token` in `credentials.py` to what was in `document.cookie` for `device_token`



## Why even have this?
Good question. This will allow you to easily download your history from robinhood and export it to a xlsx file, all for easy viewing.

When exported, it will have aggregated data such as **total P/L** or **Most successful company traded**.

Of course, you will be able to amend the file to your liking afterwards as well. You can even adjust the controller files & settings as well, in case you would like it to be a staple in your exports. 


## Contributing

Feel free to leave a pull request, or raise issues for any topic you may have.


