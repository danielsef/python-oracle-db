# myscript.py

from __future__ import print_function

import cx_Oracle

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
connection = cx_Oracle.connect("bigdata_interface", "bigdata_interface", "localhost:1521/XE")

# Oracle connection test
if __name__ == '__main__':
    cursor = connection.cursor()
    cursor.execute("""
        SELECT DEPARTMENT_ID, DEPARTMENT_NAME
        FROM HR.DEPARTMENTS
        WHERE department_id = :did AND manager_id = :eid""",
                   did=10,
                   eid=200)
    for DEPARTMENT_ID, DEPARTMENT_NAME in cursor:
        print("Values:", DEPARTMENT_ID, DEPARTMENT_NAME)


# Oracle stored procedure test


# Oracle function test


# CLOB read / write test




