# Your Python code goes here.
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        return Counter(
            (
                filter(
                    lambda x: x not in banned,
                    "".join(
                        [c.lower() if c.isalnum() else " " for c in paragraph]
                    ).split(),
                )
            )
        ).most_common(1)[0][0]
