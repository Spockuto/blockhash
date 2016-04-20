import subprocess
from nose.tools import eq_, ok_

def test_sha1():
	function_output = subprocess.check_output("python ./blockhash/mains.py -1 --file ./images/test.png", shell=True).rstrip().decode("utf-8")
	desired_output = "b87076dd43116c293f3140d6cce605db04a88d6f"
	eq_(desired_output ,function_output)

def test_sha224():
	function_output = subprocess.check_output("python ./blockhash/mains.py -2 --file ./images/test.png", shell=True).rstrip().decode("utf-8")
	desired_output = "68ca0ab03dade888dd3965a38d62d6014a696ee3d3a2dc19148510b7"
	eq_(desired_output,function_output)

def test_sha256():
	function_output = subprocess.check_output("python ./blockhash/mains.py -3 --file ./images/test.png", shell=True).rstrip().decode("utf-8")
	desired_output = "f879be85fb0df9e44390b7d9f13af07765a5814576c90dd4a1e756c48b89f83d"
	eq_(desired_output,function_output)

def test_sha384():
	function_output = subprocess.check_output("python ./blockhash/mains.py -4 --file ./images/test.png", shell=True).rstrip().decode("utf-8")
	desired_output = "305220a536c12b3ce80156047f900ef483b67d83e82cff183623316537567ea54284c676db6ff433560696cde3020a83"
	eq_(desired_output,function_output)

def test_sha512():
	function_output = subprocess.check_output("python ./blockhash/mains.py -5 --file ./images/test.png", shell=True).rstrip().decode("utf-8")
	desired_output = "7d130cf7198e22a69ce182db5886c19f989ff6ffc42a7bd98f444a3e044651a0aa3de97d79b26bb9184940d4e4039ebe8eeee057b9cf2d6bfa76e0a8dc6bfbb1"
	eq_(desired_output,function_output)
