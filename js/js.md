# javascript


--------------------------------------------------------------------------------
### index







--------------------------------------------------------------------------------



### data-types


- Seven primitive data types:
    1. number for numbers of any kind: integer or floating-point, integers are limited by ±(2^53-1).
    2. bigint for integer numbers of arbitrary length.
    3. string for strings. A string may have zero or more characters, there’s no separate single-character type.
    4. boolean for true/false.
    5. null for unknown values – a standalone type that has a single value null.
    6. undefined for unassigned values – a standalone type that has a single value undefined.
    7. symbol for unique identifiers.

- And one non-primitive data type:
    8. object for more complex data structures.

- use ```typeof x``` for data type of x


### strings

- use double/single quotes, acc to your preference.
- escape by \, some escape sequences are also there, \v, \t etc, google them if u want.

##### template-literal
    - ` string ` use backtiks, then ` ${variableName}` will format the string accordingly
    - console.log(` hello ${name} `);
    - concatnate using the + too ,

`console.log("hello " + name + "how r u");`

```js
// Number object converts whats passed into it into number

const string = "1234";
const num = Number(string);
console.log(typeof num);

// toString() does its converse

    const a = 55;
    const z = a.toString();
    typeof z // string

// expressions in strings

const output = `I like the song ${song}. I gave it a score of ${
  (score / highestScore) * 100
}%.`;

// methods

```

#### string-methods

```js

string.slice(start, end);
string.substr(start, length);

string.replace("textToBeReplacedinString", "textWhichisToBeReplaced");
// doesnt change the string
// returns new string
// replaces only first occurence
// case sensitive

string.replace(/theString/i, "textToReplace");
// use with i flag for case insensitive

/*
- this is called regular expression, which is without quotes
*/

// /g is the global flag, replaces all occurences
string.replace(/theString/g, "textToReplace");
string.toUpperCase();
string.toLowerCase();


// concat joins the string

string1.concat(" ", string2);

// its like string1 + " " + string2

```

- A STRING METHOD RETURNS A NEW STRING, IT DOESNT MODIFY THE OLD ONE
- STRINGS ARE **IMMUTABLE**, CANT BE CHANGED ONLY REPLACED.



```js

string.trim();
// removes the whitespace

//similarly
string.trimStart();
string.trimEnd();

string.padStart(numberOfPads, "stringToPad");
// eg: let s = "abs"
// padStart(10, "x");
// --> "xxxxxxxabs"

string.padEnd(sameAsAbove);


// returns character at index
string.charAt(index);

// UTF code
string.charCodeAt(index);

// note let a = "hi";
// a[0] = 'a';
// doesnt give error but doesnt work too


// to convert it into an array
string.split("");
//



// during string comparisions, js uses lexicographic order, a < b < c etc



```


### comparision

- when comparing values of diff types, js converts string to numbers
- "2" > 1           //true

```js

0 == false // true, type conversion happens
0 === false // false, checks without type conversion

null == undefined // true
null === undefined // false

// for math comparisions, > < etc, null is 0, undefined is NaN
// thus undefined converts to NaN , and NaN gives false in all operations   

/*


    Treat any comparison with undefined/null except the strict equality === with exceptional care.
    Don’t use comparisons >= > < <= with a variable which may be null/undefined, unless you’re really sure of what you’re doing. If a variable can have these values, check for them separately.


*/



```

### operators

- OR (converts non boolean to boolean) ||
-   Evaluates operands from left to right.
-   For each operand, converts it to boolean. If the result is true, stops and returns the original value of that  
    operand.
-   If all operands have been evaluated (i.e. all were false), returns the last operand.

- short circuit evaluation

```js

trueCondition || alert("not printed");
falseCondition || alert("printed");

// alert doesnt return a value, it returns undefined

/*
It means that || processes its arguments until the first truthy value is reached, and then the value is returned immediately, without even touching the other argument.

The importance of this feature becomes obvious if an operand isn’t just a value, but an expression with a side effect, such as a variable assignment or a function call.
*/

```

- AND  &&
- and finds first falsy value,
- returns last operand if all before true
- left to right evaluation

- NOT  !
- converts to boolean
- returns the inverse value

- double not !! used for converting to boolean type
`alert(!!0)`
- built in `Boolean()` function does the same thing


- precedence , && > ||

- Any value that is not false, undefined, null, 0, NaN, or an empty string ('') actually returns true when tested as a 
conditional statement, 

### conditional

- if, else, else if, switch-case, like c++
- ternary operator      condition ? ifTrueDoThis : ifFalseDoThis;
- you can nest ternary operators so be aware









































