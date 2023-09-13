from rdflib import URIRef
from rdflib.namespace import Namespace, DefinedNamespace


class SM(DefinedNamespace):
    _fail = True
    _underscore_num = True
    _NS = Namespace("https://linked.data.gov.au/def/supermodel/")

    #: Supermodel Class.
    Supermodel: URIRef
    #: ComponentModels that are in the Supermodel.
    componentModel: URIRef

    #: ComponentModel Class.
    ComponentModel: URIRef
    #: Class IRIs here are ignored by the documentation output.
    ignoreClass: URIRef


class LODE(DefinedNamespace):
    _fail = True
    _underscore_num = True
    _NS = Namespace("https://w3id.org/lode/ns/pylode/")

    #: lode:componentModel
    componentModel: URIRef

    #: lode:ignoreClass
    ignoreClass: URIRef

    #: lode:isQualifiedProfileOf
    isQualifiedProfileOf: URIRef
