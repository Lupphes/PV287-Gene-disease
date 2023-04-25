from ontobio.ontol_factory import OntologyFactory
from ontobio.assoc_factory import AssociationSetFactory

## label IDs for convenience
MOUSE = 'NCBITaxon:10090'
NUCLEUS = 'GO:0005634'
TRANSCRIPTION_FACTOR = 'GO:0003700'
PART_OF = 'BFO:0000050'

## Create an ontology object containing all of GO, with relations filtered
ofactory = OntologyFactory()
ont = ofactory.create('go').subontology(relations=['subClassOf', PART_OF])

## Create an AssociationSet object with all mouse GO annotations
afactory = AssociationSetFactory()
aset = afactory.create(ontology=ont,
                       subject_category='gene',
                       object_category='function',
                       taxon=MOUSE)

genes = aset.query([TRANSCRIPTION_FACTOR],[NUCLEUS])
print("Mouse TF genes NOT annotated to nucleus: {}".format(len(genes)))
for g in genes:
    print("  Gene: {} {}".format(g,aset.label(g)))