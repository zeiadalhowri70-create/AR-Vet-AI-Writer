# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Confidence Calibration Engine

Stage 2.3.3
"""


class ConfidenceCalibrationEngine:

    VERSION = "1.0.0"

    def __init__(self):

        self.name = "Confidence Calibration Engine"

    def calibrate(self, results):

        if not results:

            return []

        max_score = max(item.get("final_score", 0) for item in results)

        # Production safety guard
        if max_score <= 0:
            calibrated = []
            for item in results:
                new_item = dict(item)
                new_item.update(
                    {
                        "confidence": 0,
                        "confidence_level": "UNKNOWN",
                        "calibration_status": "WAITING_FOR_SCORE",
                    }
                )
                calibrated.append(new_item)
            return calibrated

        calibrated = []

        for item in results:

            score = item.get("final_score", 0)

            confidence = round((score / max_score) * 100, 2)

            if confidence >= 80:

                level = "HIGH"

            elif confidence >= 50:

                level = "MEDIUM"

            else:

                level = "LOW"

            new_item = dict(item)

            new_item.update({"confidence": confidence, "confidence_level": level})

            calibrated.append(new_item)

        return calibrated

    def health(self):

        return {"status": True, "engine": self.name, "version": self.VERSION}
