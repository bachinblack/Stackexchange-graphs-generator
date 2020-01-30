# Stackexchange graphs generator
Python tool to generate graphs given a set of tags and a range of dates.  
This is a very small project but I believe it can be useful to decorate blog posts, articles and presentations.


# Usage

usage: main.py [-h] [-f FROMDATE] [-t TODATE] [-s STEP] [-S SITE] tags

A graphics generator for stack overflow questions.

positional arguments:
  tags                  Tag or coma-separated list of tags to look for (ex.:
                        c,python,javascript).
```
optional arguments:
  -h, --help            Show this help message and exit.
  -f, --fromdate
                        First date of the range in the format 'YYYY-mm-dd[ HH]'.
  -t, --todate
                        Second date of the range in the format 'YYYY-mm-dd[ HH]'.
  -s, --step            The step in the format nt where n is a number and t a type [h, d, m, y] (ex.: Two days=2d).
  -S, --site            The stackexchange platform to look into (default: stackoverflow).
  -x, --xkcd            Displays graph with an xkcd style.
 ```
  # Requirements
  
I believe most of these requirements are installed by default with any fresh python install (pandas is not).
I also don't know which is the minimal supported version for the packages. The higher, the better!
  
| Name           | Version       |
| -------------- |:-------------:|
| python         | >= 3.6        |
| numpy          | --            |
| pandas         | --            |
| matplotlib     | --            |
| python-dateutil| --            |
| argparse       | --            |
| requests       | --            |


  # Example
  
`python3.6 main.py c,python,javascript -f 2015-01-01 -t 2020-01-01 -s 1y`

![alt text][logo]

[logo]: https://github.com/bachinblack/Stackexchange-graphs-generator/blob/master/site/picture.png "Example graph"


`python3 main.py java,csharp,cpp -f 2012-01-01 -t 2020-01-01 -s 1y -x`

![alt text][logoxkcd]

[logoxkcd]: site/xkcd_example.png "Example graph with xkcd style"


# Contribution

I highly encourage anyone to contribute, either by sending comments, opening issues or making pull requests.  

# License

MIT Licensed. Copyright (c) Philippe BOUTTEREUX 2020.
