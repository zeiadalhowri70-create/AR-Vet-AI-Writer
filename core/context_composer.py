# -*- coding: utf-8 -*-

"""
Context Composer
AR-Vet AI Writer

Stage 3.1.3.A
"""


class ContextComposer:

    def compose(self, context):

        if not context:
            return ""

        lines = []

        for key, value in context.items():

            lines.append(f"## {key}")

            if isinstance(value, dict):

                for k, v in value.items():
                    lines.append(f"- {k}: {v}")

            elif isinstance(value, list):

                for item in value:
                    lines.append(f"- {item}")

            else:

                lines.append(str(value))

            lines.append("")

        return "\n".join(lines)

    def info(self):

        return {"engine": "Context Composer", "version": "1.0"}
