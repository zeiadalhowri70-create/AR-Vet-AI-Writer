# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Veterinary Self Learning Feedback Engine

Stage 2.8.4
"""


class VeterinarySelfLearningFeedbackEngine:

    VERSION = "1.0.0"

    def __init__(self):

        self.feedback_history = []

    def add_feedback(self, predicted, confirmed, confidence=0):

        correct = predicted == confirmed

        feedback = {
            "predicted": predicted,
            "confirmed": confirmed,
            "correct": correct,
            "confidence": confidence,
        }

        self.feedback_history.append(feedback)

        return feedback

    def learning_score(self):

        if not self.feedback_history:

            return 0

        correct = sum(1 for item in self.feedback_history if item["correct"])

        return round((correct / len(self.feedback_history)) * 100, 2)

    def get_learning_signal(self, disease_id):

        matches = [
            item for item in self.feedback_history if item["predicted"] == disease_id
        ]

        if not matches:

            return {"disease": disease_id, "feedback_count": 0, "learning_score": 0}

        correct = sum(1 for item in matches if item["correct"])

        return {
            "disease": disease_id,
            "feedback_count": len(matches),
            "learning_score": round((correct / len(matches)) * 100, 2),
        }

    def health(self):

        return {
            "status": True,
            "engine": "Veterinary Self Learning Feedback Engine",
            "version": self.VERSION,
        }
