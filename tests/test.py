import subprocess
from nose.tools import eq_, ok_

def test_sha1():
	function_output = subprocess.check_output("python ./blockhash/mains.py -1 --file ./images/test.png", shell=True).rstrip().decode("utf-8")
	desired_output = "d886954ae0593abaeb6114e9dd12651378b852c1"
	eq_(desired_output ,function_output)

def test_sha224():
	function_output = subprocess.check_output("python ./blockhash/mains.py -2 --file ./images/test.png", shell=True).rstrip().decode("utf-8")
	desired_output = "b45bb365f75bd71d54c726e733754752391a7cc5044d83fd4efb86a9"
	eq_(desired_output,function_output)

def test_sha256():
	function_output = subprocess.check_output("python ./blockhash/mains.py -3 --file ./images/test.png", shell=True).rstrip().decode("utf-8")
	desired_output = "546c14f0cf534b37cf9e0579a82ed2cf7e2a279209a5d5b5ca25c6f7ccf79790"
	eq_(desired_output,function_output)

def test_sha384():
	function_output = subprocess.check_output("python ./blockhash/mains.py -4 --file ./images/test.png", shell=True).rstrip().decode("utf-8")
	desired_output = "dd98db89a3068a5825da89cc5b57f761e842b304b5b5aff31cb4a2bd055f1208ab1bc2e730c91d4fa96b76a64ede8d2c"
	eq_(desired_output,function_output)

def test_sha512():
	function_output = subprocess.check_output("python ./blockhash/mains.py -5 --file ./images/test.png", shell=True).rstrip().decode("utf-8")
	desired_output = "61a67dc1924a0c11508539c058c5d49480d558539bfa51efaa3c3fab18ae4a9bf69dd75b1d62a6228a4b47dae9968d00791cc7b7c8e199b37bf7bf2229b9bde9"
	eq_(desired_output,function_output)

def test_sha1_size():
	function_output = subprocess.check_output("python ./blockhash/mains.py -1 --file ./images/test.png -s 1024", shell=True).rstrip().decode("utf-8")
	desired_output = "2f73f1ed42aaea52f6f7e17d73ed2107545658f3"
	eq_(desired_output ,function_output)

def test_sha224_size():
	function_output = subprocess.check_output("python ./blockhash/mains.py -2 --file ./images/test.png -s 1024", shell=True).rstrip().decode("utf-8")
	desired_output = "c5afc457d69e82fa7221ff02f00deff1e62b7287ff17a34505029fa6"
	eq_(desired_output,function_output)

def test_sha256_size():
	function_output = subprocess.check_output("python ./blockhash/mains.py -3 --file ./images/test.png -s 1024", shell=True).rstrip().decode("utf-8")
	desired_output = "c17a87ddc7b1e325fdb7500c8fe942279e4f6ab9c943f34ad1dc651bc808c33b"
	eq_(desired_output,function_output)

def test_sha384_size():
	function_output = subprocess.check_output("python ./blockhash/mains.py -4 --file ./images/test.png -s 1024", shell=True).rstrip().decode("utf-8")
	desired_output = "4454e94b31924def74a9cb4225e3a6d7823daec8d7c896fcd1f8922a83088210899989f8d20075e5687bf7f5e8d5bdd1"
	eq_(desired_output,function_output)

def test_sha512_size():
	function_output = subprocess.check_output("python ./blockhash/mains.py -5 --file ./images/test.png -s 1024", shell=True).rstrip().decode("utf-8")
	desired_output = "ecda9fddee6d6e68791f95c897729c0f039e47d0712c06fdf381b07d3dfcbb13bc569e8df5a24ba2a5b67485374bd9fa7fad61feb5adef5f7d7ce7edd85eb9b1"
	eq_(desired_output,function_output)