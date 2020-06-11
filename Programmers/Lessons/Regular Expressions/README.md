# Regular Expressions

20.06.11 ~ 20.06.12

Site Link -> [https://programmers.co.kr/learn/courses/11](https://programmers.co.kr/learn/courses/11)

## Another Sites

Site Link -> [https://cs.lmu.edu/~ray/notes/regex/](https://cs.lmu.edu/~ray/notes/regex/)

Practice Link -> [https://regexone.com/](https://regexone.com/)

### REGEXONE Problem

#### Problem 1: Matching a decimal numbers

    my answer: -?\d+[\.,]?\d+[\.,e]?\d*[^p]$

    solution: ^-?\d+(,\d+)*(\.\d+(e\d+)?)?$

#### Problem 2: Matching phone numbers

    my answer: (\d{3})

    solution: (\d{3})

#### Problem 3: Matching emails

    my answer: ^([a-z\.]*)

    solution: ^([\w\.]*)

#### Problem 4: Matching HTML

    my answer: <(\w+).

    solution: <(\w+)

#### Problem 5: Matching specific filenames

    my answer: (.*)\.(jpg|png|gif)$

    solution: (\w+)\.(jpg|png|gif)$

#### Problem 6: Trimming whitespace from start and end of line

    my answer: ^[\s]*(.*)

    solution: ^\s*(.*)\s*$

#### Problem 7: Extracting information from a log file

    my answer: (\w+)\(([\w\.]+):(\d+)\)

    solution: (\w+)\(([\w\.]+):(\d+)\)

#### Problem 8: Parsing and extracting data from a URL

    my answer: (\w+)://([\w\-\.]+)(:(\d+))?

    solution: (\w+)://([\w\-\.]+)(:(\d+))?