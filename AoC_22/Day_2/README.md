Given score combinations given as:
	{ "AX", 3 }, { "BX", 0 }, { "CX", 6 },
    { "AY", 6 }, { "BY", 3 }, { "CY", 0 },
    { "AZ", 0 }, { "BZ", 6 }, { "CZ", 3 }

This can be expressed with the function:
	line - column=0 => score=3
	line - column=1 => score=6
	line - column=2 => score=0

If line - column < 0, %3 can be used to get the pretended result
once in x%3 x can't be negative we add a value 'a', such that (a+x)%3
where 'a' doesn't change the pretended result (a%3 = 0).

It was chosen the value of 3 for this matrix since there's no values
smaller than -3 given by the formula line - column.

Finally the lines can be given as lines X, Y, Z and columns as columns
A, B, C, these can be given as ASCII calculations.
	Line can be get by subtracting the current line by X.
	Column can be get by subtracting the current column by A.

Score by play X=1point, Y=2points, Z=3points can be get in a similar way.
	Score equals played move minus (X-1).