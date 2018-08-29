# encoding = utf-8
import media
import fresh_tomatoes

"""
Here you find the main() method that calls open_movies_page method from
fresh_tomatoes that render the web page.
"""

__author__ = "Gustavo Nobrega"
__license__ = "GPL"
__version__ = "1.0"
__release__ = "1.0.1"
__maintainer__ = "Gustavo Nobrega"
__email__ = "gustavonobrega@gmail.com"
__status__ = "Production"


def main():

    # Read file code block
    temp = None
    media_input = []
    file_input = open("records.txt", "r")
    for row in (row.strip().split(";") for row in file_input):
        # Counting parameters to movie's constructor
        if 5 == int(row.__len__()):
            temp = media.Movie(row[0], row[1], row[2], row[3], row[4])
            media_input.append(temp)
        else:
            raise Exception("An error has occurred read parameters(Incorrect" +
                            " amount of parameters). Check if there are 5 " +
                            "parameters in each row from records file.")
    print("List size is: "+str(media_input.__len__()))
    fresh_tomatoes.open_movies_page(media_input)

try:
    main()
except ValueError as error:
    # This exception is thrown if the user doesn't fills the file
    # (persistence) properly
    print(error.__str__())
