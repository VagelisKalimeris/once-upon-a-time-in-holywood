# Description

---
After re-watching this beautiful **Quentin Tarantino** movie, it was hard not to 
get impressed with it's end-credits calligraphy.

This here script transforms any lineup, given in *Python dictionary* or 
*json format*, to a **Latex** equation or document, in the style of the movie's 
end-credits.


# Requirements
Developed under Python 3.10


# Execution

Running the [main](main.py) script, the crew's input is expected to be 
[here](files/crew.json). Simply delete the example data and add your own.
The pattern is simple, roles with *single entry* &rarr; *strings*, roles with 
*multiple entries* &rarr; *list of strings*.  
*Latex* output will be saved [here](files/ouatih.tex). 

Alternatively the function `main.produce_latex` can be imported and executed in 
your code.


# Example
Running with the example data,
```
{
  "Directed by": "Quentin Tarantino",
  "Production Management": [
    "Georgia Kacandes",
    "Nathan Kelly",
    "Jason Zorigian"
  ],
  "Writen by": "Quentin Tarantino",
  "Produced by": [
    "Jeffrey Chan",
    "William Paul Clark",
    "David Heyman",
    "Georgia Kacandes",
    "Shannon McIntosh",
    "Daren Metropoulos",
    "Quentin Tarantino",
    "Dong Yu"
  ],
  "Cinematography by": "Robert Richardson",
  "Art direction by": [
    "Tristan Paris Bourne",
    "John Dexter",
    "Richard L. Johnson",
    "Eric Sundahl",
    "Dennis Bradford",
    "Jann K. Engel"
  ]
}
```
\
we get an output string that when compiled as **Latex** looks like this:

![](files/screenshot.png)

\
Example compiled and saved
as a [pdf document](files/ouatih_compiled.pdf).
