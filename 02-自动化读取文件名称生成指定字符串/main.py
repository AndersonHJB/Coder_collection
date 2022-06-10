# -*- coding: utf-8 -*-
# @Author: AI悦创
# @Date:   2022-06-10 15:37:42
# @Last Modified by:   aiyc
# @Last Modified time: 2022-06-10 15:52:51
import os

BASE = "[{filename}](https://video.aiyc.top/weiqi/{name})"

def read_file(path):
	r_list = []
	result = os.walk(path)
	for i in result:
		# print(i[2])
		r_list.append(i[2])
	return r_list


def join_str(filename):
	with open("README.md", "wt+", encoding="utf8") as f:
		for name in filename[0]:
			content = BASE.format(filename=name, name=name)
			f.write(content + "\n")

if __name__ == "__main__":
	path = "."
	filename_list = read_file(path)
	# filename_list.sort()
	print(filename_list)
	# print(type(filename_list))
	join_str(filename_list)