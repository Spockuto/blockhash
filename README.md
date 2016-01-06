#`blockhash`
[![Build Status](https://travis-ci.org/Spockuto/blockhash.svg?branch=master)](https://travis-ci.org/Spockuto/blockhash)
[![Coverage Status](https://coveralls.io/repos/Spockuto/blockhash/badge.svg?branch=master&service=github)](https://coveralls.io/github/Spockuto/blockhash?branch=master)

**A SHA implementations which serves normal SHA for small files and**
**block based SHA for larger files which speeds up your process**


![Block Based Hashing](images/image.png)


#Installation

##Using `pip`

`$ pip install blockhash`

##Get the latest build from the Source

* Clone the repo `git clone https://github.com/spockuto/blockhash.git`
* Run `python setup.py install`

##Dependencies

* future `$ pip install future`

Usage
=====
```sh
$	blockhash --help
	
	usage: blockhash [-h] [-1] [-2] [-3] [-4] [-5] [-f FILE]

	Speed up your SHA. A different hash style.
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -1, --sha1
	  -2, --sha224
	  -3, --sha256
	  -4, --sha384
	  -5, --sha512
	  -f FILE, --file FILE  The path to the file	  
```

#Contribute

If you want to add features, improve them, or report issues, feel free to send a pull request.

#Contributors

* [Venkkatesh Sekar](https://github.com/Spockuto)

#License

MIT © [Venkkatesh Sekar](https://in.linkedin.com/in/venkkateshsekar)
