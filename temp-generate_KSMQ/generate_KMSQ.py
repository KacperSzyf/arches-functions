from datetime import date
from importlib import resources
from platform import node
from site import execsitecustomize
import uuid
from venv import create
from arches.app.models.models import Concept as modelConcept
from arches.app.models.concept import Concept
from arches.app.models.tile import Tile
from django.core.exceptions import ValidationError
from arches.app.functions.base import BaseFunction
import json

details = {
    "name": "Generate KMSQ",
    "type": "node",
    "description": "Just a sample demonstrating node group selection",
    "defaultconfig": {"triggering_nodegroups": []},
    "classname": "GenerateKMSQ",
    "component": "views/components/functions/generate_KMSQ",
}

#Methods
def createNewTile(tile):
    location_qualifiers =  "727b4e04-7dcc-11ec-9a1f-00155db3508e"
    location = '14608154-7dcc-11ec-8ae4-00155db3508e'
    mapsheet = "bfbcd2a0-7dcc-11ec-9bd9-00155db3508e"
    kmsq = "af5d093e-7dcc-11ec-9bd9-00155db3508e"
    loaction_accuracy = "81194e3e-7dcc-11ec-871b-00155db3508e"
    map_reference = "5844718c-7dcc-11ec-a910-00155db3508e"
    
    new_tile = Tile().get_blank_tile_from_nodegroup_id(location_qualifiers, tile.resourceinstance_id)
    
    new_tile.data[kmsq] = NRGtoKMSQ(tile.data[map_reference])
    new_tile.data[mapsheet] = NRGtoMapsheet(tile.data[map_reference])
    return new_tile

def NRGtoKMSQ(ngr):   
    return ngr[:2] + ngr[2:4] + ngr[7:9]

def NRGtoMapsheet(nrg):
    #plus quarter
    quarter = 'NW'
    return nrg[:2] + nrg[2:3] + nrg[7:8] + quarter

class GenerateKMSQ(BaseFunction):

    def save(self, tile, request):
        new_tile = createNewTile(tile)
        new_tile.save()
        return     