# -*- coding: utf-8 -*-


class DiagnosisBuilder:

    def build(self, graph, disease_id, profile):

        diagnosis = profile.get("scientific_profile", {}).get("diagnosis", {})

        tests = (
            diagnosis.get("field", [])
            + diagnosis.get("laboratory", [])
            + diagnosis.get("advanced_tests", [])
        )

        for test in tests:

            test_id = test.lower().replace(" ", "_")

            graph.add_node(test_id, "diagnostic_test", {"name": test})

            graph.add_edge(disease_id, "diagnosed_by", test_id)

        return graph
