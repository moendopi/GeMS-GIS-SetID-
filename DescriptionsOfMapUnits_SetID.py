"""
Model exported as python.
Name : DescriptionOfMapUnits_SetID
Group : 
With QGIS : 32804
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterMapLayer
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class Descriptionofmapunits_setid(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterMapLayer('descriptionofmapunits', 'DescriptionOfMapUnits', defaultValue=None, types=[QgsProcessing.TypeMapLayer]))
        self.addParameter(QgsProcessingParameterFeatureSink('Descriptionofmapunits_id', 'DescriptionOfMapUnits_ID', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))

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
            'FORMULA': "'DMU' || to_string(@row_number+1)",
            'INPUT': parameters['descriptionofmapunits'],
            'OUTPUT': parameters['Descriptionofmapunits_id']
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Descriptionofmapunits_id'] = outputs['FieldCalculator']['OUTPUT']
        return results

    def name(self):
        return 'DescriptionOfMapUnits_SetID'

    def displayName(self):
        return 'DescriptionOfMapUnits_SetID'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Descriptionofmapunits_setid()
