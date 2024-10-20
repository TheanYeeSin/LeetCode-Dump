# Your Python code goes here.
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_email = set()
        for email in emails:
            local, domain = email.split("@")
            temp = ""
            for c in local:
                if c == ".":
                    continue
                elif c == "+":
                    break
                else:
                    temp += c
            unique_email.add(temp + "@" + domain)
        return len(unique_email)
