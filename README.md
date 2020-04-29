# UMD-course-availability
A simple command line tool for checking course availability at the University of Maryland

# How to use
After cloning this repository (and checking you have python installed), run:

```
python main.py [arg]
```

In this command, arg is a course prefix. The result of this command is printing the available sections of all classes with the given prefix. For example:

```
python main.py CMSC

CMSC106         Introduction to C Programming
0101            Instructor: TBA                 25  / 48

...
```

The argument can also be a portion of a prefix or a full course prefix with the course number. Too short of a prefix will have no result and a full course name will show the availability of that course.

```
python main.py C

<No result>

python main.py CMSC330

CMSC330         Organization of Programming Languages
0101            Anwar Mamat                     1   / 32
0103            Anwar Mamat                     12  / 32
0105            Anwar Mamat                     5   / 32
0106            Anwar Mamat                     33  / 34
0109            Anwar Mamat                     28  / 32
0201            Roger Eastman                   10  / 32
0205            Roger Eastman                   7   / 32
0207            Roger Eastman                   15  / 32

...
```

Note: The availability information comes from UMD's schedule of classes and is currently used for Fall 2020.
