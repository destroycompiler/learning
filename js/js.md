# javascript


--------------------------------------------------------------------------------
### index

1. [data-types](#data-types)
2. [strings](#strings)
3. [template-literal](#template-literal)
4. [string-methods](#string-methods)
5. [comparision](#comparision)
6. [operators](#operators) 
7. [conditional](#conditional)
8. **important things**
    - [1](#imp-1) - 
    - [2](#imp-2) - 
    - [3](#imp-3) - js DOM manipulation
9. [Javascript Call Stack](#js-call-stack)

10. **Read Later**
- [var and let](https://stackoverflow.com/questions/762011/what-is-the-difference-between-let-and-var#:~:text=The%20main%20difference%20is%20scoping,(hence%20the%20block%20scope))
- [JS execution](https://www.youtube.com/watch?v=iLWTnMzWtj4)

11.  [error](#error)
12. [NodeJS](#node-js)
13. [Arrays](#arrays)
14. [for-of loop, filter(), map()](#map)
15. [do-while](#do-while)
16. [label](#label)
17. [Multiple Optional Arguments](#multiple-arguments)


- [DOM manipulation](#dom-manipulation)
- 





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

--------------------------------------------------------------------------------------------

### imp-1

Bear in mind that some built-in browser functions are not part of the core JavaScript language — some are defined as part of *browser APIs*

-------------------------------------------------------------------------------------------

### functions

- Functions that are part of objects are called methods.

```js

// default parameters

function hell(name = 'dc') {
    console.log(`hello ${name}`);
}

// hell() // gives "hello dc"
// hell("doo") gives "hello doo"


// --------------------------------------------------------------------

// #### ANONYMOUS FUNCTIONS

```

---

- ANONYMOUS FUNCTION

- function with no name, generally passed into another function as a parameter

```js

textBox.addEventListener('keydown', function(event) {
  console.log(`You pressed "${event.key}".`);
});

// addEventListener(eventToListenFor, functionToExecute)

// anonymous function

(function (arg) {
    // code
})


```

- ARROW FUNCTION

- another form to pass anonymous functions

```js

text.addEventListener('keydown', (event) => {
    // function code
});


```

- scope is there in functions, inside a function, local scope, outside, global scope

- If a same-named variable is declared inside the function then it shadows the outer one. 

*- fx(a, b);  value copied then passed, pass by value*

- if argument is not passed, it becomes underfined when the function is called

```js


function f(name, greeting="hello") {
    alert(name + " : " + greeting);
}

f("yo"); 

// its called like 
f("yo", undefined);


function sho(name, greeting = otherFunction()) {
    // anotherFunction() only  executed if the value of greeting not passed
}


```

- In JavaScript, a default parameter is evaluated every time the function is called without the respective parameter.

-Sometimes it makes sense to assign default values for parameters at a later stage after the function declaration.
We can check if the parameter is passed during the function execution, by comparing it with undefined.

eg:

```js
function fa(txt) {

    // code ...

    if(txt === undefined) {
        txt = 'empty message';
    }
    // --------------------------------

    // or

    txt = txt || 'msg';

    // code ..
}

```

- you can return without returning anything

`function f() {return;}` - it returns undefined

```js

return (
    // code
    // code
)

```

- for returning multiple lined code

- function expression :-
```js

let myFun = function() {
    // content
};
// call it by myFun();
// the variable myFun has been assigned as a function
// its called a function expression

// they store a function in the sayHi variable, both methods

function sayHi() {   // (1) create
  alert( "Hello" );
}

let func = sayHi;    // (2) copy

func(); // Hello     // (3) run the copy (it works)!
sayHi(); 



// using function as function param

function fuck(time, condom, stamina) {
    if(stamina == good) condom()
    else time()
}

function a() {}
function b() {}

// call
fuck(10, a, b);

// or 


```




















FUNCTION DECLARATION

- a function declared as a separate statement
    function sum(a, b) {
        return a+b;
    }

FUNCTION EXPRESSION

- function created inside an expression

let a = function() {
    //code
};


----------------------------------------------------------------------------------------------------
### imp-2

JAVASCRIPT ENGINE 

A Function Expression is created when the execution reaches it and is usable only from that moment.  

Once the execution flow passes to the right side of the assignment let sum = function… – here we go, the function is 
created and can be used (assigned, called, etc. ) from now on.  

Function Declarations are different.  A Function Declaration can be called earlier than it is defined. 
For example, a global Function Declaration is visible in the  whole script, no matter where it is.  That’s due to 
internal algorithms. When JavaScript prepares to run the script, it 
first looks for global Function Declarations in it and creates the functions. We can think of it as an “initialization 
stage”.  And after all Function Declarations are processed, the code is executed. So it has access to these functions.

As a rule of thumb, when we need to declare a function, the first thing to consider is Function Declaration syntax. It gives more freedom in how to organize our code, because we can call such functions before they are declared.

That’s also better for readability, as it’s easier to look up function f(…) {…} in the code than let f = function(…) {…};. Function Declarations are more “eye-catching”.

…But if a Function Declaration does not suit us for some reason, or we need a conditional declaration (we’ve just seen an example), then Function Expression should be used.

----------------------------------------------------------------------------------------------------

```js
// works
// --------------------------------------------------
say();

function say() {
    // code
}
// --------------------------------------------------

// doesnt work

say();

let say = function() {};


// --------------------------------------------------

```

In strict mode, when a Function Declaration is within a code block, it’s visible everywhere inside that block. 
But not outside of it.

Function Declaration is only visible inside the code block in which it resides.

```js

if (condition) {
    function f() {
        // code
    }
}

f(); // won't work


// otherwise, do this

let f;

if(condn) {f = function() {};}
else {f = function(){};}

// or use ? : ternary


```

#### arrow-function

```js


let fun = (arg, arg1) => returnExpression;

// for no argument
let fun = () => alert("fun");
// can be used same way as function expressions, dynamically to create the fxns

// same as

let fun = function(arg, arg1) {
    return returnExpression;
}

// multiline arrow funciton

let f = () => {

    // code
    return undefined;
};

```


### function-argument

```js
function fart(a, b, c) {
	console.log(arguments[0]);
	console.log(arguments[1]);
	console.log(arguments[2]);
	// function has inbuilt array called arguments, which contains the
	// list of all arguements

	console.log(arguments.length);
	// to output the number of arguments

	/*
	- updating the argument[x] also updates the variable associated with
	that argument

	- updating the variable also updates the arguments[x] element
	associated with that variable.
	*/
}
```

### js-call-stack

- [Javascript Call Stack Article](https://www.javascripttutorial.net/javascript-call-stack/)

> stackoverflow
> synchronous js
> LIFO
> stack
> when js executes the script it places the global execution context on top of the stack




### error

- An error is a type of object built into the JS language, consisting of a name/type and a message. Errors contain crucial information that can assist you in locating the code responsible for the error, determining why you have this error, and resolving the error.

1. syntax error
2. ReferenceError
3. TypeError



## Installing Node JS
### node-js

- `nvm` (Node Version Manager), because it makes it easy to change Node versions and upgrade Node. There is another tool called `npm` (Node Package Manager) that you will use later to install the various libraries and tools used in JavaScript environments. It can be easy to confuse these two, so read carefully!



### arrays

```js

// array is an object
let myArr = ['cars', 'names', 'bikes', 56];

// or
let myArr = new Array('stuff', 78);

console.log(myArr[index]);
// to access index

// array.length returns the length of the array

myArr.length

// add element
myArr.push(element);
myArr[myArr.length] = element;
```

> in JS arrays use **numbered indexes**, objects use **named indexes**

```js
let a = [49]; // array with single element

let b = new Array(49); // array with 49 undefined elements

// to check array
Array.isArray(arrayName); // to check for array

arrayName.toString(); // to convert array into string
array.join(" * "); // joins all array elements by the arg into string
array.pop(); // removes last element
array.push(element); // pushes new element, returns the length

// removes the first element, shifts all others left
// returns shifted out value
array.shift(); 

// to reverse an array
array.split('').reverse().join('');

// unshift adds element to first, and shifts others right
// returns new array length
array.unshift();
delete array[index]; // leaves undefined element which is deleted

let concatedAr = ar1.concat(ar2);
// [ar1, ar2] this order

arr.splice(startIndex, numberOfItemsRemoved, element1, element2, ..);
// use splice to remove items without leaving undefined holes in the array

arr.splice(startIndex, numberOfItemsRemoved);

let slicedAr = array.slice(startingIndex, endingIndex);
// [startingIndex, endingIndex)
// slice(startingIndex); // this format slices until the end

```

---

### for-of loop
### filter
### map


```js
let arr = ['Leopard', 'Serval', 'Jaguar', 'Tiger', 'Caracal', 'Lion'];
for (animal of arr) {
	console.log(animal);
}

// use map() to do something to each item
function toUpper(string) {
  return string.toUpperCase();
}

const cats = ['Leopard', 'Serval', 'Jaguar', 'Tiger', 'Caracal', 'Lion'];

const upperCats = cats.map(toUpper);

console.log(upperCats);
// [ "LEOPARD", "SERVAL", "JAGUAR", "TIGER", "CARACAL", "LION" ]


```

- we pass a function into cats.map() and map calls the function once for each item in the array, passing in the item as argument, then adds the return value from each call to a new array, then returns the array

---

- filter()

```js
function lCat(cat) {
  return cat.startsWith('L');
}

const cats = ['Leopard', 'Serval', 'Jaguar', 'Tiger', 'Caracal', 'Lion'];

const filtered = cats.filter(lCat);

console.log(filtered);
// [ "Leopard", "Lion" ]

```

- This looks a lot like `map()`, except the function we pass in returns a boolean if it returns `true`, then the item is included in the new array. Our function tests that the item starts with the letter "L", so the result is an array containing only cats whose names start with "L"

```js

const cats = ['Leopard', 'Serval', 'Jaguar', 'Tiger', 'Caracal', 'Lion'];

const filtered = cats.filter((cat) => cat.startsWith('L'));
console.log(filtered);
// [ "Leopard", "Lion" ]

// using a function expression

```


### do-while
```js

do {
	// code exec atleast once- [JS execution](https://www.youtube.com/watch?v=iLWTnMzWtj4)

- [JS execution](https://www.youtube.com/watch?v=iLWTnMzWtj4- [JS execution](https://www.youtube.com/watch?v=iLWTnMzWtj4)
} while (condition);

```

- small hacks :-
```js
while (i != 0) {
	
}
// can be written as
while(i) {

}
```

### label

```js
outer: for () {
	for () {
		if(condn) break outer;
		// or continue outer;	
	}
}
```



### multiple-optional-arguments
### multiple-arguments


### rest-parameters

- represent an indefinite number of arguments as an array

```js
function multiply(multiplier, ...theArgs) {
  return theArgs.map((x) => multiplier * x);
}

const arr = multiply(2, 1, 2, 3);
console.log(arr); // [2, 4, 6]

```





### dom
### DOM
### document-object-model
### dom-manipulation

- The DOM (or Document Object Model) is a tree-like representation of the contents of a webpage - a tree of “nodes” with different relationships depending on how they’re arranged in the HTML document.

```js

element.querySelector(selector);
// returns a referece to the first match of selector

element.querySelectorAll(selectors);
// returns a nodelist containing reference to all the matches of the selectors 

// NOTE : ARRAY AND NODELIST ARE NOT SAME

document.createElement(tagName, [options]);
// creates new element of type tagName
// function doesnt put in DOM, it just puts it in the memory
// then you edit the element, add styles etc, after that put it in DOM

// TO APPEND THE ELEMENT

parentNode.appendChild(childNode);
// appends childNode as last child of parentNode

parentNode.insertBefore(newNode, referenceNode);
// inserts newNode before referenceNode

let removed = parentNode.removeChild(child);
// removes child from parentNode on the DOM and returns a reference
// to child


```


- reference can be used to alter the elements and their properties

```js

let div = document.createElement('div');

div.style.color = 'red';
// adds indicated style

div.style.cssText = 'color: blue; background-color: white;';
// adds the css 

div.setAttribute('style', 'color: blue; background-color: white;');

div.style['background-color'] = 'blue'; // also works
div.classList.add('new');
// adds a class new
div.classList.remove('new');
// removes the class

div.classList.toggle('taget');
// adds if not there, or removes if itis there


div.textContent = 'Hello';
// creates the the text node containing the string
// adds the textContent 'Hello' inside the div

div.innerHTML = '<span>Hello ji</span>';
// renders the html inside the div

```


### imp-3

Keep in mind that the JavaScript **does not** alter your HTML, but the DOM - your HTML file will look the same, but the JavaScript changes what the browser renders.



- general : add script to last, first html will process then the js will run and alter the DOM.
- alternatively

```html
<head>
	<script src='location' defer></script>
</head>
```

- use **defer** to load the js after all the html has parsed.


### callbacks

- they are just functions passed into other functions as arguments.
- 




### data-attribute
 - data-*  can be used in html page as a custom attribute.

```js

window.addEventListener('keydown', function(e) {
const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);

audio.currentTime = 0; // this rewinds the clip, so multiple hitting works.
	// in case when pressed a different key, audio = null
	// thus we add a condition
	
	if(!audio) {
		return;
	}
	
	audio.play();
});

```