Client Requirements Specification

The client runs an old-fashioned rental service where customers can rent the following items:

    Books, described by:
        Author
        Title
        Genre
        ISBN
        Rental ID
    Movies, described by:
        Director
        Title
        Genre
        Duration
        Rental ID
    CDs, described by:
        Band
        Title
        Genre
        Tracklist
        Duration
        Rental ID

The application should provide functionality that allows logged-in users full editing capabilities for the items available for rent. The editing process must enforce the following validation rules:

    Books:
        All ISBNs must be unique.
        The combination of author, title, and genre must be unique.

    Movies:
        The number of different movies within a genre in the entire collection can differ by no more than 3.
        If the director and title are the same, the duration must differ.

    CDs:
        Within the same genre, no two CDs can have the same tracklist.
        CDs from the same band can only be offered in two genres.

The application should also track the quantities of each rental item, along with information about renters, their rentals, and returns.

Additionally, the application should offer rental statistics over specified time periods, including:

    The popularity of books, movies, and CDs by genre.
    A unified ranking of renters, broken down by the type and genre of the rented item.

Technical Requirements

    The application's data should be persisted in a database.
    The database should use Django's migration mechanism.
    The application should be developed using Django technology with Class-based views.
    The operations should implement full CRUD functionality for the program's data.
    The application, in addition to the admin panel, should provide user login functionality.