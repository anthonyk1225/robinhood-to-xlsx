import sqlite3

# GET
def get_bearer_token():
    """
    returns a TUPLE
     - empty if it doesn't exist
     - contains row if it does exist
    """

    conn = sqlite3.connect('robinhood.db')
    command = "SELECT bearer_token FROM authorization WHERE user_id=1;"
    cursor = conn.execute(command)
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()

    return all_rows

# CREATE
def create_authorization(bearer_token):
    """
    returns INTEGER
     - last id of row created
    """

    conn = sqlite3.connect('robinhood.db')
    command = "INSERT INTO authorization\
        (bearer_token, user_id)\
        VALUES ('{}', 1);".format(bearer_token)

    cursor = conn.execute(command)
    conn.commit()
    conn.close()

    return cursor.lastrowid


# UPDATE
def update_bearer_token(bearer_token):
    """
    returns INTEGER
    - returns 0
    """

    conn = sqlite3.connect('robinhood.db')
    command = "UPDATE authorization\
        SET bearer_token='{}'\
        where user_id=1;".format(bearer_token)
    print(command)
    cursor = conn.execute(command)
    conn.commit()
    conn.close()

    return cursor.lastrowid
