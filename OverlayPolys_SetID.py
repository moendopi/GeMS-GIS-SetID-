"""
Model exported as python.
Name : OverlayPolys_SetID
Group : 
With QGIS : 32804
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterMapLayer
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class Overlaypolys_setid(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterMapLayer('overlaypolys', 'OverlayPolys', defaultValue=None, types=[QgsProcessing.TypeVectorPolygon]))
        self.addParameter(QgsProcessingParameterFeatureSink('Overlaypolys_id', 'OverlayPolys_ID', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))

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
            'FORMULA': "'OVP' || to_string(@row_number+1)",
            'INPUT': parameters['overlaypolys'],
            'OUTPUT': parameters['Overlaypolys_id']
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Overlaypolys_id'] = outputs['FieldCalculator']['OUTPUT']
        return results

    def name(self):
        return 'OverlayPolys_SetID'

    def displayName(self):
        return 'OverlayPolys_SetID'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Overlaypolys_setid()
