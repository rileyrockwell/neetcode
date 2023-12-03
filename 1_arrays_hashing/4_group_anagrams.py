from typing import *


class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		return_list = []
		temp_dict = {}

		for word in strs:
			sorted_word = "".join(sorted(word))
			
			if sorted_word not in temp_dict:
				temp_dict[sorted_word] = [word]
			else:
				temp_dict[sorted_word].append(word)

		for elements in temp_dict.values():
			return_list.append(elements)

		return return_list




strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))