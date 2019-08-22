# robinhood-to-xlsx

## Environment

You are going to need / want to use
- Python - [The version of python that I use is 3.7.2](https://www.python.org/downloads/release/python-372/)
- pip (pip3 w/ python3)
- Virtualenv - [I use version 16.4.3](https://virtualenv.pypa.io/en/latest/)

## Installation

After forking, cloning into wherever
```
$ cd to/wherever/it/is
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt
```

## Credentials file
The file will look like this
```
# your credentials
username = "" # Your robinhood username or email
password = "" # Your robinhood password

# should also be generated, but needs to be found for now
device_token = "" # Your device token in the headers

```
- `(venv) $ touch credentials.py`
- Update `username="yourusername"`, `password="yourpassword"`
- Log in to robinhood and open up the inspector (`cmd+opt+i` on mac)
- Type `document.cookie` in the console and copy your `device_token`
- Update `device_token="your-device-token"` in `credentials.py`

## Running the app

`(venv) $ python3 app.py`

Two choices follow
- `json`
- `xlsx`
##### Getting your history - json
When you want to get the most up to date history, select `json` and then any of the selections.
##### Generating excel files - xlsx
When you want to generate an excel file from the `json` you have stored, select `xlsx`.

![](https://pbs.twimg.com/media/DOKNxxPVAAAbun0.jpg)

## Why even have this?
Good question. This will allow you to easily download your history from robinhood and export it to a xlsx file, all for easy viewing.

When exported, it will have aggregated data such as **total P/L** or **Most successful company traded**(Coming soon).

Of course, you will be able to amend the file to your liking afterwards as well. You can even adjust the controller files & settings as well, in case you would like it to be a staple in your exports. 

## Settings
The `settings.py` file contains what data the excel file will contain. For example, if you would like to include more information in the export to dividends, all you need to do is adjust `selected_keys_dividends`. Same goes for if you would like to remove a column.  You can also adjust the width of the columns by adjusting the width field for each respective dict.

You can see all of the fields available to include, by looking in the `data` folder and then the respective entity.

## Contributing

Feel free to leave a pull request, or raise issues for any topic you may have.
