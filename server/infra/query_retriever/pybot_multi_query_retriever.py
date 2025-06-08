from langchain_core.callbacks import CallbackManagerForRetrieverRun
from typing import List
from langchain.chains import LLMChain
from langchain.retrievers.multi_query import MultiQueryRetriever
import logging

logger = logging.getLogger(__name__)

"""
The original class MultiQueryRetriever for some reason only work if you have a single template variable called "question" as it is hard-coded.
But the LLM Chain can receive any dict with the variables, this class exists to override the generate_queries methods and send to LLM Chain the whole dict in any format and not only "question"
Code Reference: https://github.com/langchain-ai/langchain/discussions/28169#discussioncomment-11297594
"""
class PybotMultiQueryRetriever(MultiQueryRetriever):
    def generate_queries(
            self, question: str, run_manager: CallbackManagerForRetrieverRun
    ) -> List[str]:
        """Generate queries based on user input.

        Args:
            question: The user query.
            run_manager: Callback manager for handling retriever runs.

        Returns:
            List of LLM-generated queries that are similar to the user input.
        """
        response = self.llm_chain.invoke(
            question, config={"callbacks": run_manager.get_child()}
        )
        if isinstance(self.llm_chain, LLMChain):
            lines = response["text"].splitlines()
        else:
            lines = response

        if self.verbose:
            logger.info(f"Generated queries: {lines}")

        return lines
