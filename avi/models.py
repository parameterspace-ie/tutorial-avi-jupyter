from django.db import models
from pipeline.models import AviJob


class SimpleJob(AviJob):
    """
    This model is used to store the parameters for the AVI pipeline.
    Notice that it contains identical field names here as is the variables in
    the pipeline itself.

    An AviJob model must contain all fields required by the intended
    pipeline class (ProcessData) in this case.
    """

    query = models.CharField(max_length=1000, 
        default="""SELECT source_id, ra, dec, phot_g_mean_flux, phot_g_mean_mag, 
    DISTANCE(POINT('ICRS',ra,dec), POINT('ICRS',266.41683,-29.00781)) 
    AS dist FROM gaiadr1.gaia_source WHERE 
    1=CONTAINS(POINT('ICRS',ra,dec), CIRCLE('ICRS',266.41683,-29.00781, 0.08333333))""")
    pipeline_task = "ProcessData"

    def get_absolute_url(self):
        return "%i/" % self.pk