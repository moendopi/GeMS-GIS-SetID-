"""
Model exported as python.
Name : GeologicLines_SetID
Group : 
With QGIS : 32804
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterMapLayer
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class Geologiclines_setid(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterMapLayer('geologiclines', 'GeologicLines', defaultValue=None, types=[QgsProcessing.TypeVectorLine]))
        self.addParameter(QgsProcessingParameterFeatureSink('Geologiclines_id', 'GeologicLines_ID', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(1, model_feedback)
        results = {}
        outputs = {}

        # Field calculator
        alg_params = {
            'FIELD_LENGTH': 254,
            'FIELD_NAME': '_ID',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # Text (string)
            'FORMULA': "'GEL' || to_string(@row_number+1)",
            'INPUT': parameters['geologiclines'],
            'OUTPUT': parameters['Geologiclines_id']
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Geologiclines_id'] = outputs['FieldCalculator']['OUTPUT']
        return results

    def name(self):
        return 'GeologicLines_SetID'

    def displayName(self):
        return 'GeologicLines_SetID'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Geologiclines_setid()
