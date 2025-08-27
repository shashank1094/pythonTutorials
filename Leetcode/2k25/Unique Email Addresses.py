# https://leetcode.com/problems/unique-email-addresses/editorial/
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_count = 0
        email_set = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            first_plus_index = local_name.find('+')
            if first_plus_index != -1:
                local_name = local_name[:first_plus_index]
            local_name = local_name.replace('.', '')
            clean_email = local_name + '@' + domain_name
            if clean_email not in email_set:
                email_set.add(clean_email)
                unique_count += 1
        return unique_count


if __name__ == '__main__':
    # print(Solution().numUniqueEmails(
    #     ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
    print(Solution().numUniqueEmails(
        ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]))
