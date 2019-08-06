import sqlite3

# GET
def get_auth_tokens():
    """
    returns a TUPLE
     - empty if it doesn't exist
     - contains row if it does exist
    """

    conn = sqlite3.connect('robinhood.db')
    command = "SELECT access_token, refresh_token FROM authorization WHERE user_id=1;"
    cursor = conn.execute(command)
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()

    return all_rows

# CREATE
def create_authorization(access_token, refresh_token):
    """
    returns INTEGER
     - last id of row created
    """

    conn = sqlite3.connect('robinhood.db')
    command = "INSERT INTO authorization\
        (access_token, refresh_token, user_id)\
        VALUES ('{}', '{}', 1);".format(access_token, refresh_token)

    cursor = conn.execute(command)
    conn.commit()
    conn.close()

    return cursor.lastrowid


# UPDATE
def update_auth_tokens(access_token, refresh_token):
    """
    returns INTEGER
    - returns 0
    """

    conn = sqlite3.connect('robinhood.db')
    command = "UPDATE authorization\
        SET access_token='{}',\
            refresh_token='{}'\
                where user_id=1;".format(access_token, refresh_token)

    cursor = conn.execute(command)
    conn.commit()
    conn.close()

    return cursor.lastrowid
