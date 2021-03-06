# HTML Search

This program is a GUI for a very basic html parser, using Python, limited to elements containing text. The user can select an html element to search for and input a website url, and the results are displayed. The tkinter, ~~urlib~~ requests, and ~~re~~ beautifulsoup libraries are implemented for learning purposes. 

## Instructions
Upon launch, the GUI is in a default state. The user can select from a list of html elements using buttons on the left edge of the window. The user can also input an URL in the designated region. 

Upon clicking the search button, the results will be collected and displayed in the box below the search button (in the box that by default reads "Results will appear here"). 

If no results are found, results box will display a status indicating such. If results are found, they will be displayed one at a time in the results box. The user can click the left and right arrow buttons next to the results box to cycle through the current displayed result from the list of results.

![alt text](https://user-images.githubusercontent.com/12664577/41743817-e58a2fb4-756f-11e8-9064-e9be1359b30d.PNG)

Upon clicking the search button again, the results box will be reset based on the newly obtained results using the new URL.

The user can exit the program using either the "X" window button or choosing File > Exit. 

## Future developement

* Improve loading time or add an indicator that the application is loading
* Add a search for custom search where the user can input an html element to search for
* Add the ability to search for embedded elements, where the user selects the elements and the order to search for them

## Built With

* [Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/)
* [Requests](http://docs.python-requests.org/en/master/)

## Authors

* **Graham Haynie** - [grahamhaynie](https://github.com/grahamhaynie)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details