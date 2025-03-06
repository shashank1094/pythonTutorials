# https://leetcode.com/problems/smallest-sufficient-team/?envType=company&envId=amazon&favoriteSlug=amazon-all

import copy
from typing import List


class Solution:
    minimum_people = None

    def helper(self, skills_left, people_included_till_now, people_index, people):
        if len(skills_left) == 0:
            if self.minimum_people is None:
                self.minimum_people = copy.deepcopy(people_included_till_now)
            elif len(self.minimum_people) > len(people_included_till_now):
                self.minimum_people = copy.deepcopy(people_included_till_now)
            return
        if people_index >= len(people):
            return

        temp_skills = skills_left - set(people[people_index])
        if len(temp_skills) < len(skills_left):
            people_included_till_now.append(people_index)
            self.helper(temp_skills, people_included_till_now, people_index + 1, people)
            people_included_till_now.pop()
        self.helper(skills_left, people_included_till_now, people_index + 1, people)

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        req_skills = set(req_skills)
        self.helper(req_skills, [], 0, people)
        return self.minimum_people


if __name__ == '__main__':
    print(Solution().smallestSufficientTeam(req_skills=["java", "nodejs", "reactjs"],
                                            people=[["java"], ["nodejs"], ["nodejs", "reactjs"]]))
    print(Solution().smallestSufficientTeam(req_skills=["algorithms", "math", "java", "reactjs", "csharp", "aws"],
                                            people=[["algorithms", "math", "java"], ["algorithms", "math", "reactjs"],
                                                    ["java", "csharp", "aws"], ["reactjs", "csharp"],
                                                    ["csharp", "math"],
                                                    ["aws", "java"]]))
    print(Solution().smallestSufficientTeam(
        req_skills=["wmycibrjxh", "wicacrldwneag", "ndutqtjuzu", "pgo", "gxsskiz", "rbrymc", "erpevpmu", "jboexi",
                    "vpfdcjwngzuf", "w"],
        people=[[], ["ndutqtjuzu", "pgo"], ["ndutqtjuzu"], ["pgo", "rbrymc"], ["wicacrldwneag", "ndutqtjuzu"], [],
                ["wicacrldwneag", "rbrymc", "erpevpmu"], ["w"], ["wmycibrjxh", "wicacrldwneag", "pgo", "w"], [], ["w"],
                ["gxsskiz", "erpevpmu", "vpfdcjwngzuf"], ["wicacrldwneag"], ["vpfdcjwngzuf"],
                ["wmycibrjxh", "erpevpmu"], ["ndutqtjuzu", "pgo"], ["ndutqtjuzu", "pgo"],
                ["wmycibrjxh", "erpevpmu", "jboexi"], ["wmycibrjxh", "wicacrldwneag", "jboexi"],
                ["wmycibrjxh", "wicacrldwneag", "rbrymc"], ["wicacrldwneag"], ["erpevpmu", "vpfdcjwngzuf"],
                ["wmycibrjxh"], ["jboexi", "w"], ["erpevpmu", "jboexi", "w"], ["w"], ["erpevpmu", "jboexi"], ["jboexi"],
                ["wicacrldwneag"], [], ["jboexi", "vpfdcjwngzuf"], ["wmycibrjxh", "jboexi"], ["wicacrldwneag"], [],
                ["pgo"], ["wicacrldwneag"], [], ["wmycibrjxh", "vpfdcjwngzuf"], ["wmycibrjxh"],
                ["pgo", "vpfdcjwngzuf", "w"], ["wicacrldwneag", "jboexi"],
                ["wicacrldwneag", "erpevpmu", "vpfdcjwngzuf"], ["wicacrldwneag"],
                ["wmycibrjxh", "pgo", "erpevpmu", "vpfdcjwngzuf"], ["w"], ["vpfdcjwngzuf", "w"],
                ["wmycibrjxh", "erpevpmu"], ["wicacrldwneag", "pgo", "jboexi"],
                ["wmycibrjxh", "erpevpmu", "vpfdcjwngzuf"], ["w"], [], [], [], ["pgo", "jboexi"], ["wicacrldwneag"],
                ["wicacrldwneag", "erpevpmu", "jboexi"], ["wmycibrjxh", "pgo"],
                ["wmycibrjxh", "wicacrldwneag", "gxsskiz"], ["erpevpmu"], ["pgo", "rbrymc", "erpevpmu", "w"]]))
