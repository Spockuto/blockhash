#!/usr/bin/env python

import subprocess
from nose.tools import eq_, ok_

def test_sha1():
	function_output = subprocess.check_output("python ./blockhash/mains.py -1 --file ./images/test.png", shell=True).rstrip()
	desired_output = "e45eabab13f84de0bb24fb5f5ddd57d462ebbf57"
	eq_(desired_output,function_output)

def test_sha224():
	function_output = subprocess.check_output("python ./blockhash/mains.py -2 --file ./images/test.png", shell=True).rstrip()
	desired_output = "1a52bf0a20c734839167bb7b5b2ccd271e0ce9d523585439ac950917"
	eq_(desired_output,function_output)

def test_sha256():
	function_output = subprocess.check_output("python ./blockhash/mains.py -3 --file ./images/test.png", shell=True).rstrip()
	desired_output = "16b6eb59000c18eb3a361aab1c228e18f441cf79da5b665f70230d60b671809e"
	eq_(desired_output,function_output)

def test_sha384():
	function_output = subprocess.check_output("python ./blockhash/mains.py -4 --file ./images/test.png", shell=True).rstrip()
	desired_output = "e1f6d95b7c5136ac52335ea1a645936e46ffdf75b52e31d8f3899866b92205356ec9c4f7238145b2bc5d6178a0c78fc0"
	eq_(desired_output,function_output)

def test_sha512():
	function_output = subprocess.check_output("python ./blockhash/mains.py -5 --file ./images/test.png", shell=True).rstrip()
	desired_output = "bc12b37fa6a252a65eb25203de4526148c6801098d188fa0e7b39cae32f0d6881ecfe7f9040a3722e93f286f2ddb1d5f3188dd45936ad1a2c3b7176c818053b9"
	eq_(desired_output,function_output)

