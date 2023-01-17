# Introduction to Programming

## Assignment: Task 3

### The Problem

The University of Poppleton has a number of buildings which are used for various activities. It is important to
track which members of staff are in each building at any point in time. A list could be crucial in the event of a
fire, for example.

To this end, every staff member has a card which they are required to swipe when they enter or leave a building. By
analysing the data thus generated it should be possible to determine which members of staff are currently in which
building.

A prototype system has been installed in Poppleton Hall (on Poppleton Campus), and it requires some software.

### The Task

There will need to be two input to this software. The first will be a list of staff members along with their
ID number. The ID number is recorded by the device on each door when a card is "swiped". This file is of arbitrary
length, and looks like this:

```text
2799 Mr Jeffrey Cardona
2315 Miss Dawn Walker
2027 Mrs Michelle Kelty
1469 Mr Dennis Henderson
7943 Prof Emily Booth
1570 Dr John Scott
7686 Dr Lois Judd
2986 Miss Helen Obrien
3345 Ms Irene Destefano
4212 Miss Nichole Lipner
7260 Prof Denise Borst
9386 Prof Dolores Coney
```

The second input file consists of data generated from each "swipe". There are three doors in the Hall, and the file
shows which door was accessed, and by which card. It is also of arbitrary length, but a small fragment might be:

```text
2799 1
2315 2
1469 2
2799 2
```

It is assumed that initially the building is empty. So, looking at the staff file, we can see that this data reveals 
that Mr Cardona used Door 1 to enter the building, then Miss Walker used Door 2, and Mr Henderson also used Door 2. 
Therefore, after the third line all three are currently in the building. The final line above reveals that Mr Cardona 
then used Door 2; as he was in the building, he must have left, so only the other two remain in the building.

The software should read a staff list and a list of door accesses. After each access it should display the number
of staff in the building, along with their names. Some example output is below. Both files are provided as
command-line arguments.

The software should end by printing the final list of staff in the building.

### Examples

The following illustrate what should happen when the program executes in a variety of situations. 

Here is a small staff list. It is very short to make tracing events easier.
```text
5094 Prof Joannie Longwell
7822 Prof Debra Ziegler
5373 Mr Ronald Mistretta
8962 Prof Roderick Jones
1985 Miss Elissa Robinson
```

and here is some sample door data for the same staff members:

```text
5373 3
5094 2
1985 1
1985 2
8962 1
5373 1
5373 2
8962 1
5094 3
1985 2
7822 3
1985 3
```

So, taking Miss Robinson (ID 1985) as an example. we can see that she entered via Door 1 (line 3), left via Door 2 (line
4), and then later returned via Door 2 before leaving finally via Door 3. This, and much else, is apparent in 
the output:

```text
$ python3 popleton_hall.py staff.txt doors.txt                                                                                                                                  [12:29:36]
Door Activation 1
Mr Ronald Mistretta accessed Door 3.
Mr Ronald Mistretta has entered the building.
In [1]: Mr Ronald Mistretta.

Door Activation 2
Prof Joannie Longwell accessed Door 2.
Prof Joannie Longwell has entered the building.
In [2]: Mr Ronald Mistretta, Prof Joannie Longwell.

Door Activation 3
Miss Elissa Robinson accessed Door 1.
Miss Elissa Robinson has entered the building.
In [3]: Mr Ronald Mistretta, Prof Joannie Longwell, Miss Elissa Robinson.

Door Activation 4
Miss Elissa Robinson accessed Door 2.
Miss Elissa Robinson has left the building.
In [2]: Mr Ronald Mistretta, Prof Joannie Longwell.

Door Activation 5
Prof Roderick Jones accessed Door 1.
Prof Roderick Jones has entered the building.
In [3]: Mr Ronald Mistretta, Prof Joannie Longwell, Prof Roderick Jones.

Door Activation 6
Mr Ronald Mistretta accessed Door 1.
Mr Ronald Mistretta has left the building.
In [2]: Prof Joannie Longwell, Prof Roderick Jones.

Door Activation 7
Mr Ronald Mistretta accessed Door 2.
Mr Ronald Mistretta has entered the building.
In [3]: Prof Joannie Longwell, Prof Roderick Jones, Mr Ronald Mistretta.

Door Activation 8
Prof Roderick Jones accessed Door 1.
Prof Roderick Jones has left the building.
In [2]: Prof Joannie Longwell, Mr Ronald Mistretta.

Door Activation 9
Prof Joannie Longwell accessed Door 3.
Prof Joannie Longwell has left the building.
In [1]: Mr Ronald Mistretta.

Door Activation 10
Miss Elissa Robinson accessed Door 2.
Miss Elissa Robinson has entered the building.
In [2]: Mr Ronald Mistretta, Miss Elissa Robinson.

Door Activation 11
Prof Debra Ziegler accessed Door 3.
Prof Debra Ziegler has entered the building.
In [3]: Mr Ronald Mistretta, Miss Elissa Robinson, Prof Debra Ziegler.

Door Activation 12
Miss Elissa Robinson accessed Door 3.
Miss Elissa Robinson has left the building.
In [2]: Mr Ronald Mistretta, Prof Debra Ziegler.

Final Status
In [2]: Mr Ronald Mistretta, Prof Debra Ziegler.
```

The program should also exit gracefully in error cases such as missing or incorrectly formatted files. There is no
need for the error messages generated to say exactly what is awry.
