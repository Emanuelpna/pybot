from typing_extensions import List

from langchain_core.output_parsers import BaseOutputParser


class LineListOutputParser(BaseOutputParser[List[str]]):
    def parse(self, text: str) -> List[str]:
        return list(filter(None, text.strip().split("\n")))
