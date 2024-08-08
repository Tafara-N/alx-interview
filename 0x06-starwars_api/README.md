The “0. Star Wars Characters” project requires you to interact with an external API to fetch and display
information about Star Wars characters based on the movie ID provided as an argument. To successfully
complete this project, you need to be familiar with several key concepts related to web programming, API
interaction, and asynchronous programming in JavaScript.

# Concepts Needed:

1. **HTTP Requests in JavaScript:**

    - Understanding how to make HTTP requests to external services using the `request` module or alternatives like `fetch` in Node.js.
    - [A Complete Guide to Making HTTP Requests in Node.js](https://intranet.alxswe.com/rltoken/iRse23lnV4gAsD9JJTJMMQ)

2. **Working with APIs:**

    - Understanding the basics of RESTful APIs and how to interact with them.
    - Parsing JSON data returned by APIs.
    - [Working with APIs in JavaScript](https://intranet.alxswe.com/rltoken/KyGS_uB68mLaP5irrH8JVA)

3. **Asynchronous Programming:**

    - Managing asynchronous operations with callbacks, promises, and async/await syntax.
    - Handling API response data asynchronously.
    - [Asynchronous Programming in JavaScript](https://intranet.alxswe.com/rltoken/tdKMGJrRstCkXSReNfRFpQ)

4. **Command Line Arguments in Node.js:**

    - Using the `process.argv` array to access command-line arguments passed to a Node.js script.
    - [How to Parse Command Line Arguments in Node.js](https://intranet.alxswe.com/rltoken/oWBOWJZLF_D9GfOydPz6Kg)

5. **Array Manipulation and Iteration:**

    - Iterating over arrays and manipulating data structures to format and display character names.
    - [JavaScript Array Methods](https://intranet.alxswe.com/rltoken/8zdG036OYYvVco_AZTExoA)

By familiarizing yourself with these concepts and resources, you will be able to efficiently retrieve, process, and display Star Wars characters from the specified movie using the Star Wars API, demonstrating your ability to work with external APIs and manage asynchronous code in JavaScript.

# Additional Resources
- [Mock Technical Interview]()

# Requirements

## General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version `10.14.x`)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant. [Rules of Standard]() + [semicolons on top](). Also as reference: [AirBnB style]()
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`

# More Info

**Install Node 10**

```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

**Install semi-standard**

[Documentation]()

```bash
$ sudo npm install semistandard --global
```

**Install `request` module and use it**

[Documentation]()

```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Tasks

### 0. Star Wars Characters

Write a script that prints all characters of a Star Wars movie:

- The first positional argument passed is the Movie ID - example: `3 = “Return of the Jedi”`
- Display one character name per line **in the same order as the “characters” list in the /`films`/ endpoint**
- You must use the [Star wars API](https://intranet.alxswe.com/rltoken/gh_NaSUk9QlXHVoACFU-tg)
- You must use the `request` module

```bash
alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06$
```

**Repo:**
- GitHub repository: `alx-interview`
- Directory: `0x06-starwars_api`
- File: `0-starwars_characters.js`
