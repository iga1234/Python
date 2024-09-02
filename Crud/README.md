Task Description

The task involves creating a module that provides basic database functionality, specifically covering CRUD operations (Create, Read, Update, Delete). The database structure is as follows: id;first_name;last_name;pesel.

By default, the database is empty when the script is launched.
CREATE

The user has two options to add new records to the database:

    Load data from a text file (a sample file named data.txt is provided in the repository).
    Manually enter values in the console.

Before adding a record to the database, the uniqueness of the id must be verified.
READ

The user should be able to read the entire content of the database in a readable format.
UPDATE

The user is prompted to provide the ID of the record they wish to update, followed by the new values. If the provided ID does not exist in the database, an appropriate message should be displayed.
DELETE

The user can delete a record based on the provided ID. If the provided ID does not exist in the database, an appropriate message should be displayed.
ADDITIONAL FEATURES

    A function to calculate the average age of people in the database based on the pesel number.
    A function to return the number of men and women in the database based on the pesel number.

Notes

    The id is assumed to be a primary and unique key.
    For file operations, refer to Python File I/O.
    All functions should be written in a separate module, and the main program should only call these functions as needed.