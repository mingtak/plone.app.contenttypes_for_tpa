# -*- coding: utf-8 -*-
from zope.interface import Interface
from plone.namedfile.field import NamedBlobImage

from plone.app.contenttypes import _


class IPloneAppContenttypesLayer(Interface):
    """Marker interface that defines a ZTK browser layer. We can reference
    this in the 'layer' attribute of ZCML <browser:* /> directives to ensure
    the relevant registration only takes effect when this theme is installed.

    The browser layer is installed via the browserlayer.xml GenericSetup
    import step.
    """


class ICollection(Interface):
    """Explicit marker interface for Collection
    """


class IDocument(Interface):
    """Explicit marker interface for Document
    """


class IFile(Interface):
    """Explicit marker interface for File
    """


class IFolder(Interface):
    """Explicit marker interface for Folder
    """
    banner1 = NamedBlobImage(
        title=_(u"Banner 1 image"),
        required=False,
    )

    banner2 = NamedBlobImage(
        title=_(u"Banner 2 image"),
        required=False,
    )

    banner3 = NamedBlobImage(
        title=_(u"Banner 3 image"),
        required=False,
    )

    banner4 = NamedBlobImage(
        title=_(u"Banner 4 image"),
        required=False,
    )

    banner5 = NamedBlobImage(
        title=_(u"Banner 5 image"),
        required=False,
    )


class IImage(Interface):
    """Explicit marker interface for Image
    """


class ILink(Interface):
    """Explicit marker interface for Link
    """


class INewsItem(Interface):
    """Explicit marker interface for News Item
    """


class IEvent(Interface):
    """Explicit marker interface for Event
    """
