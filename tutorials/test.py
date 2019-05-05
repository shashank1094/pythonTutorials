# # # # # # # # # n = int(input())
# # # # # # # # #
# # # # # # # # # a = [int(x) for x in input().split(sep=" ", maxsplit=n)]
# # # # # # # # #
# # # # # # # # # print(a)
# # # # # # # #
# # # # # # # #
# # # # # # # # # import re
# # # # # # # # #
# # # # # # # # # sentence = 'horses are fast'
# # # # # # # # # regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
# # # # # # # # # matched = re.search(regex, sentence)
# # # # # # # # # print(matched.groupdict())
# # # # # # # #
# # # # # # # # def f(arr, k):
# # # # # # # #     um = {}
# # # # # # # #     sum = 0
# # # # # # # #     maxLen = 0
# # # # # # # #     for i in range(len(arr)):
# # # # # # # #         sum += arr[i]
# # # # # # # #         if sum == k:
# # # # # # # #             maxLen = i + 1
# # # # # # # #         if sum-k in um:
# # # # # # # #             maxLen = i - um[sum - k]
# # # # # # # #         else:
# # # # # # # #             um[sum] = i
# # # # # # # #
# # # # # # # #     return maxLen
# # # # # # # #
# # # # # # # # print(f([11,2,-2,3], 0))
# # # # # # #
# # # # # # #
# # # # # # # # read the string filename
# # # # # # # filename = input()
# # # # # # # file_content = ""
# # # # # # # with open(filename, "r") as f:
# # # # # # #     file_content = f.read()
# # # # # # #
# # # # # # # file_content = file_content.split('\n')
# # # # # # # from itertools import groupby
# # # # # # #
# # # # # # # extsn_appeared = []
# # # # # # # sorted_content = sorted(file_content, key=lambda x: x.split('.')[-1])
# # # # # # # for extsn, grp in groupby(sorted_content, lambda x: x.split('.')[-1]):
# # # # # # #     extsn_appeared.append(extsn)
# # # # # # #     with open(extsn + "_" + filename, "w") as temp_f:
# # # # # # #         temp_f.write("\n".join(list(grp)))
# # # # # # #
# # # # # # # extsn_appeared
# # # # # # # extsn_required = ["c", "cpp", "cs"]
# # # # # # # extsn_left = set(extsn_required) - set(extsn_appeared)
# # # # # # #
# # # # # # # for single_extns in extsn_left:
# # # # # # #     with open(single_extns + "_" + filename, "w") as temp_f:
# # # # # # #         temp_f.write("")
# # # # # #
# # # # # # # !/bin/python3
# # # # # #
# # # # # # import sys
# # # # # # import os
# # # # # # from urllib.request import Request
# # # # # # from urllib.request import urlopen
# # # # # # from urllib.error import URLError
# # # # # # import json
# # # # # #
# # # # # #
# # # # # # # Complete the function below.
# # # # # # def getNumberOfMovies(substr):
# # # # # #     endpoint = "https://jsonmock.hackerrank.com/api/movies/search/?Title={substr}"
# # # # # #     res = urlopen(endpoint.format(substr=substr))
# # # # # #     if res.getcode() == 200:
# # # # # #         result = res.read().decode('utf-8')
# # # # # #         result = json.loads(result)
# # # # # #         print(result)
# # # # # #     # print(res.html = )
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # # f = open(os.environ['OUTPUT_PATH'], 'w')
# # # # # # #
# # # # # # # try:
# # # # # # #     _substr = str(input())
# # # # # # # except:
# # # # # # #     _substr = None
# # # # # #
# # # # # # # res = getNumberOfMovies(_substr)
# # # # # # res = getNumberOfMovies("maze")
# # # # # # # f.write(str(res) + "\n")
# # # # # #
# # # # # # # f.close()
# # # # #
# # # # #
# # # # # # read the string filename
# # # # # # filename = input()
# # # # # # file_content = ""
# # # # # # with open(filename, "r") as f:
# # # # # #     file_content = f.read()
# # # # #
# # # # # file_content = """unicomp6.unicomp.net   - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
# # # # # burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0
# # # # # burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0
# # # # # burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 0
# # # # # d104.aa.net - - [01/Jul/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
# # # # # unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
# # # # # unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786
# # # # # unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204
# # # # # d104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
# # # # # d104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786"""
# # # # #
# # # # # file_content = file_content.split('\n')
# # # # # from itertools import groupby
# # # # # import re
# # # # #
# # # # # required_content = [re.split(" +-", x)[0].lower().strip() for x in file_content]
# # # # # required_content = [t for t in required_content if t]
# # # # # sorted_content = sorted(required_content)
# # # # #
# # # # # result = []
# # # # # for host, grp in groupby(sorted_content):
# # # # #     result.append("{} {}".format(host, len(list(grp))))
# # # # #
# # # # # print("\n".join(result))
# # # # # # with open("records" + "_" + filename, "w") as temp_f:
# # # # # #     temp_f.write("\n".join(result))
# # # #
# # # #
# # # # #!/bin/python3
# # # #
# # # # import sys
# # # # import os
# # # # from urllib.request import Request
# # # # from urllib.request import urlopen
# # # # from urllib.error import URLError
# # # # import json
# # # #
# # # #
# # # # # Complete the function below.
# # # # # Base url: https://jsonmock.hackerrank.com/api/movies/search/?Title=
# # # #
# # # # def getMovieTitles(substr):
# # # #     endpoint = "https://jsonmock.hackerrank.com/api/movies/search/?Title={substr}&page={page_num}"
# # # #     titles = []
# # # #     total_pages = 1
# # # #     try:
# # # #         page_visited_till_now = 1
# # # #         res = urlopen(endpoint.format(substr=substr, page_num=page_visited_till_now))
# # # #         if res.getcode() == 200:
# # # #             raw_result = res.read().decode('utf-8')
# # # #             result = json.loads(raw_result)
# # # #             total_pages = result.get('total_pages', 1)
# # # #             titles.extend([x.get('Title') for x in result.get('data', []) if x.get('Title')])
# # # #             if total_pages > 1:
# # # #                 for i in range(2, total_pages + 1):
# # # #                     child_res = urlopen(endpoint.format(substr=substr, page_num=i))
# # # #                     if child_res.getcode() == 200:
# # # #                         child_raw_result = child_res.read().decode('utf-8')
# # # #                         child_result = json.loads(child_raw_result)
# # # #                         titles.extend([x.get('Title') for x in child_result.get('data', []) if x.get('Title')])
# # # #     except:
# # # #         pass
# # # #     return sorted(titles)
# # # #
# # # # print(getMovieTitles("spiderman"))
# # #
# # #
# # # # def maxProfit(costPerCut, salePrice, lengths):
# # # #     max_length = max(lengths)
# # # #     max_profit = float("-inf")
# # # #     for i in range(max_length + 1, 1, -1):
# # # #         number_of_cuts = sum([(length // i) - 1 if length % i == 0 else (length // i) for length in lengths])
# # # #         total_uniform_rods = sum([(length // i) for length in lengths])
# # # #         total_profit = (total_uniform_rods * salePrice * i) - (number_of_cuts * costPerCut)
# # # #         if total_profit > max_profit:
# # # #             max_profit = total_profit
# # # #     return max_profit
# # # #
# # # #
# # # # print(maxProfit(1, 10, [30, 59, 110]))
# # #
# # #
# # # file_content = """unicomp6.unicomp.net   - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
# # # burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0
# # # burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0
# # # burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 0
# # # d104.aa.net - - [01/Jul/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
# # # unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
# # # unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786
# # # unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204
# # # d104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
# # # d104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786"""
# # #
# # # file_content = file_content.split('\n')
# # # from itertools import groupby
# # # import re
# # #
# # # required_content = [re.split("- - \[", x)[0].lower().strip() for x in file_content]
# # # required_content = [t for t in required_content if t]
# # # sorted_content = sorted(required_content)
# # #
# # # result = []
# # # for host, grp in groupby(sorted_content):
# # #     result.append("{} {}".format(host, len(list(grp))))
# # #
# # # print("\n".join(result))
# #
# #
# # def maxProfit(costPerCut, salePrice, lengths):
# #     max_length = max(lengths)
# #     max_profit = float("-inf")
# #     optimal_length=0
# #     for i in range(1, max_length+1):
# #         number_of_cuts = sum([(length // i) - 1 if length % i == 0 else (length // i) for length in lengths])
# #         total_uniform_rods = sum([(length // i) for length in lengths])
# #         total_profit = (total_uniform_rods * salePrice * i) - (number_of_cuts * costPerCut)
# #         if total_profit > max_profit:
# #             f_number_of_cuts = number_of_cuts
# #             optimal_length = i
# #             max_profit = total_profit
# #     print(optimal_length, f_number_of_cuts)
# #
# #     lengths = sorted(lengths)
# #     max_score = 0
# #     total_uniform_rods = m_len = 0
# #     from itertools import groupby
# #     for k,g in groupby(lengths):
# #         g_len = len(list(g))
# #         temp_score = k * g_len
# #         if temp_score>max_score:
# #             total_uniform_rods = g_len
# #             m_len = k
# #     total_profit = (total_uniform_rods * salePrice * m_len)
# #     if total_profit > max_profit:
# #             max_profit = total_profit
# #
# #     return max_profit
# #
# # print(maxProfit(100, 10, [10, 10, 2]))
#
# def sum_fib(n):
#     f = 1
#     s = 1
#     t = f + s
#     sum = f+s
#     while (t <= n):
#         sum += t
#         f = s
#         s = t
#         t = f + s
#     # sum -= t
#
#     return sum
#
#
# print(sum_fib(2))
#
# # 1 1 2 3 5 8 13
#
#
import numpy as np

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)
print(b[0][0])
