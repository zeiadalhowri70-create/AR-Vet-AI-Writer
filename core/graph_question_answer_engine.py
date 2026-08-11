# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphQuestionAnswerEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def answer(self, question):

        question = question.lower()

        answers = []

        for node_id, node in self.graph.nodes.items():

            data = node.get("data", {})

            text = str(data).lower()

            if node_id.lower() in question or any(
                str(value).lower() in question for value in data.values()
            ):

                answers.append(
                    {"node": node_id, "type": node.get("type"), "data": data}
                )

        return answers

    def related_answer(self, node_id):

        results = []

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                results.append({"relation": edge["relation"], "target": edge["target"]})

        return results

    def info(self):

        return {
            "engine": "Graph Question Answer Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
