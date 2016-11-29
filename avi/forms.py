"""
This module contains all ``django.forms.ModelForm`` implementations associated with AVI pipeline jobs (``gavip_avi.pipeline.models.AviJob``). 
The model subclasses of ``AviJob`` themselves are implemented in :mod:`avi.models`.
"""
from django.forms import ModelForm, Textarea

from avi.models import SimpleJob

DEFAULT_EXCLUDED_MODEL_FIELDS = [
    'expected_runtime',
    'output_path',
    'request',
    'resources_ram_mb',
    'resources_cpu_cores'
]


class QueryForm(ModelForm):
    """
    ModelForm for Query
    """
    class Meta:
        model = SimpleJob
        exclude = DEFAULT_EXCLUDED_MODEL_FIELDS
        
        widgets = {
            'query': Textarea(attrs={'rows':5, 'style':'width:100%'}),
        }
