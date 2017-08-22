
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

from . import igp_ldp_sync
class mpls(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/mpls. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state relating to MPLS-related
features in IS-IS
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__igp_ldp_sync',)

  _yang_name = 'mpls'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__igp_ldp_sync = YANGDynClass(base=igp_ldp_sync.igp_ldp_sync, is_container='container', yang_name="igp-ldp-sync", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'mpls']

  def _get_igp_ldp_sync(self):
    """
    Getter method for igp_ldp_sync, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/mpls/igp_ldp_sync (container)

    YANG Description: Configuration and operational state relating to synchronisation
between the LDP and IS-IS
    """
    return self.__igp_ldp_sync
      
  def _set_igp_ldp_sync(self, v, load=False):
    """
    Setter method for igp_ldp_sync, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/mpls/igp_ldp_sync (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igp_ldp_sync is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igp_ldp_sync() directly.

    YANG Description: Configuration and operational state relating to synchronisation
between the LDP and IS-IS
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=igp_ldp_sync.igp_ldp_sync, is_container='container', yang_name="igp-ldp-sync", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igp_ldp_sync must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=igp_ldp_sync.igp_ldp_sync, is_container='container', yang_name="igp-ldp-sync", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__igp_ldp_sync = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igp_ldp_sync(self):
    self.__igp_ldp_sync = YANGDynClass(base=igp_ldp_sync.igp_ldp_sync, is_container='container', yang_name="igp-ldp-sync", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  igp_ldp_sync = __builtin__.property(_get_igp_ldp_sync, _set_igp_ldp_sync)


  _pyangbind_elements = {'igp_ldp_sync': igp_ldp_sync, }


from . import igp_ldp_sync
class mpls(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/mpls. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state relating to MPLS-related
features in IS-IS
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__igp_ldp_sync',)

  _yang_name = 'mpls'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__igp_ldp_sync = YANGDynClass(base=igp_ldp_sync.igp_ldp_sync, is_container='container', yang_name="igp-ldp-sync", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'mpls']

  def _get_igp_ldp_sync(self):
    """
    Getter method for igp_ldp_sync, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/mpls/igp_ldp_sync (container)

    YANG Description: Configuration and operational state relating to synchronisation
between the LDP and IS-IS
    """
    return self.__igp_ldp_sync
      
  def _set_igp_ldp_sync(self, v, load=False):
    """
    Setter method for igp_ldp_sync, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/mpls/igp_ldp_sync (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igp_ldp_sync is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igp_ldp_sync() directly.

    YANG Description: Configuration and operational state relating to synchronisation
between the LDP and IS-IS
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=igp_ldp_sync.igp_ldp_sync, is_container='container', yang_name="igp-ldp-sync", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igp_ldp_sync must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=igp_ldp_sync.igp_ldp_sync, is_container='container', yang_name="igp-ldp-sync", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__igp_ldp_sync = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igp_ldp_sync(self):
    self.__igp_ldp_sync = YANGDynClass(base=igp_ldp_sync.igp_ldp_sync, is_container='container', yang_name="igp-ldp-sync", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  igp_ldp_sync = __builtin__.property(_get_igp_ldp_sync, _set_igp_ldp_sync)


  _pyangbind_elements = {'igp_ldp_sync': igp_ldp_sync, }


