# kaplan_parser

A quick python script I whipped up to make counting confirmation emails
from form submissions a lot easier. 

To run:
```bash
python parse.py
```

You will be asked to input parameters to start the search.

```bash
Login email: <login>                             // "swag@gmail.com"
Password: <password>                             // "swog"
Number of days to search through: <timeframe>    // 3
Subject line search: <subject line>              // "UC Berkeley"
File to write to: <output>                       // "output.txt"
```

Results are in <output>.

### Misc. notes to self:

1. Sort and Count distinct lines:
  * sort <output> | uniq -c

2. Line count:
  * wc -l <output>