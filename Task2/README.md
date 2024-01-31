# Introduction to Programming

## Assignment: Task 2

### The Problem

Yorkshire Stormwatch is a group of volunteers who venture out during storms to measure the wind speed at various points along the Yorkshire Coast. They publish summary data on their website, and this is often reported by local News media.

Their readings are simple. They record the location, the wind speed (in mph), and the name of the current storm. These data are sent back to the group's Chief Data Scientist, who prepares the summary statistics.

### The Task

The data is submitted via a web form. There is often some delay, as the volunteers must find spare time in order to upload their records. The data is stored in a single text file, and the readings are in random order. A sample of a recent data file is:

```text
Filey,77,Debi
Saltburn,89,Debi
Filey,72,Isha
Bridlington,89,Henk
Scarborough,97,Agnes
Skipsea,87,Fergus
Whitby,81,Henk
```

So we see the location of the reading, the wind speed, and the name of the Storm that was prevalent at the time.

The required statistics are:

* The overall highest wind speed.
* The location recording the highest speed.
* The average speed for each of the towns.
* The name of the Storm that had the highest average wind speed.

The data is to be provided in a file (there is an example in this folder). It can be assumed to be in the correct format. The name of the file will be provided as a command-line argument.

_Your solution should be written using only standard Python. You may obviously use standard library modules._

### Hints

This is an exercise about how to store data. If you think carefully about how to get the data from the file into some suitable data structure, and implement this, the actual program becomes easy.

Remember that the highest wind speed may have been observed more than once, and possibly in several locations.

You can assume that the file contains at least one reading for each location, and at least one for each storm. (This observation is actually a good place to start).

### Examples

The following illustrate what should happen when the program executes in a variety of situations. 

Here is a small extract from a data stream. Working with a small file allows us to check the results. The actual files will be much larger.

```text
Filey,77,Debi
Saltburn,89,Debi
Filey,72,Isha
Bridlington,89,Henk
Scarborough,97,Agnes
Skipsea,87,Fergus
Whitby,81,Henk
Saltburn,102,Gerit
Hornsea,71,Isha
Filey,96,Ciaran
Hornsea,73,Jocelyn
Whitby,102,Fergus
Withernsea,91,Elin
Withernsea,67,Ciaran
```

The program should take the name of the file on the command-line, and the display the results. In this case 
they should be something like:

```text
$ python3 storm_analysis.py wind_speeds.txt

Wind Speed Analysis
~~~~~~~~~~~~~~~~~~~

Highest Speed Recorded: 102 MPH

102 MPH recorded at Saltburn during Storm Gerit
102 MPH recorded at Whitby during Storm Fergus

Filey: Average Speed 81.67 MPH
Saltburn: Average Speed 95.50 MPH
Bridlington: Average Speed 89.00 MPH
Scarborough: Average Speed 97.00 MPH
Skipsea: Average Speed 87.00 MPH
Whitby: Average Speed 91.50 MPH
Hornsea: Average Speed 72.00 MPH
Withernsea: Average Speed 79.00 MPH

Worst storm was Storm Gerit with average gusts of 102.00 MPH!
```

Obviously the program needs to exit gracefully if the input file (as provided on the command line) is not found:

```text
$ python3 storm_analysis.py
storm_analysis.py Error. Missing file name.
```

and also if the command-line argument is missing completely:

```text
$ python3 storm_analysis.py wind_speediess.txt
storm_analysis.py Error. Cannot open "wind_speediess.txt".
```
