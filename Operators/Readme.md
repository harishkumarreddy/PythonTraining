## Operators :
1. Arithmetic operators     ->  `+, -, *, /, %, **, //`
    NOTE: These will follow the BODMAS rule
2. Assignment operators     ->  `=, +=, -=, *=, /=, %=, **=, //=`
3. Comparison operators     -> ` ==, !=, <, <=, >, >=`
4. Logical operators        ->  `and, or, not`
5. Identity operators       ->  `is, is not`
6. Membership operators     ->  `in, not in`
7. Bitwise operators        ->  `&, |, ^, ~, <<, >>`


#### T-Table:
```
-------------------------------
| BOOL  | LO  | BOOL  | RES   |
-------------------------------
| TRUE  | and | TRUE  | TRUE  |
| TRUE  | and | FALSE | FALSE |
| FALSE | and | TRUE  | FALSE |
| FALSE | and | FALSE | FALSE |
| TRUE  | or  | TRUE  | TRUE  |
| TRUE  | or  | FALSE | TRUE  |
| FALSE | or  | TRUE  | TRUE  |
| FALSE | or  | FALSE | FALSE |
-------------------------------
| not TRUE   = FALSE           |
| not FALSE  = TRUE            |
-------------------------------
```
