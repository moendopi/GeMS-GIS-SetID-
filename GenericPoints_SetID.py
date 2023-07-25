"""
Model exported as python.
Name : GenericPoints_SetID
Group : 
With QGIS : 32804
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterMapLayer
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class Genericpoints_setid(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterMapLayer('genericpoints', 'GenericPoints', defaultValue=None, types=[QgsProcessing.TypeVectorPoint]))
        self.addParameter(QgsProcessingParameterFeatureSink('Genericpoints_id', 'GenericPoints_ID', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))

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
            'FORMULA': "'GNP' || to_string(@row_number+1)",
            'INPUT': parameters['genericpoints'],
            'OUTPUT': parameters['Genericpoints_id']
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Genericpoints_id'] = outputs['FieldCalculator']['OUTPUT']
        return results

    def name(self):
        return 'GenericPoints_SetID'

    def displayName(self):
        return 'GenericPoints_SetID'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Genericpoints_setid()
