
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

class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/global/interface-attributes/interface/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters related to MPLS interfaces:
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface_id','__mpls_enabled',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mpls_enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mpls-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__interface_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'global', u'interface-attributes', u'interface', u'config']

  def _get_interface_id(self):
    """
    Getter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/global/interface_attributes/interface/config/interface_id (oc-if:interface-id)

    YANG Description: Indentifier for the MPLS interface
    """
    return self.__interface_id
      
  def _set_interface_id(self, v, load=False):
    """
    Setter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/global/interface_attributes/interface/config/interface_id (oc-if:interface-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: Indentifier for the MPLS interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_id must be of a type compatible with oc-if:interface-id""",
          'defined-type': "oc-if:interface-id",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)""",
        })

    self.__interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_id(self):
    self.__interface_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)


  def _get_mpls_enabled(self):
    """
    Getter method for mpls_enabled, mapped from YANG variable /network_instances/network_instance/mpls/global/interface_attributes/interface/config/mpls_enabled (boolean)

    YANG Description: Enable MPLS forwarding on this interface
    """
    return self.__mpls_enabled
      
  def _set_mpls_enabled(self, v, load=False):
    """
    Setter method for mpls_enabled, mapped from YANG variable /network_instances/network_instance/mpls/global/interface_attributes/interface/config/mpls_enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_enabled() directly.

    YANG Description: Enable MPLS forwarding on this interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mpls-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mpls-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__mpls_enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_enabled(self):
    self.__mpls_enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mpls-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  interface_id = __builtin__.property(_get_interface_id, _set_interface_id)
  mpls_enabled = __builtin__.property(_get_mpls_enabled, _set_mpls_enabled)


  _pyangbind_elements = {'interface_id': interface_id, 'mpls_enabled': mpls_enabled, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/global/interface-attributes/interface/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters related to MPLS interfaces:
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface_id','__mpls_enabled',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mpls_enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mpls-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__interface_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'global', u'interface-attributes', u'interface', u'config']

  def _get_interface_id(self):
    """
    Getter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/global/interface_attributes/interface/config/interface_id (oc-if:interface-id)

    YANG Description: Indentifier for the MPLS interface
    """
    return self.__interface_id
      
  def _set_interface_id(self, v, load=False):
    """
    Setter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/global/interface_attributes/interface/config/interface_id (oc-if:interface-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: Indentifier for the MPLS interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_id must be of a type compatible with oc-if:interface-id""",
          'defined-type': "oc-if:interface-id",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)""",
        })

    self.__interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_id(self):
    self.__interface_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)


  def _get_mpls_enabled(self):
    """
    Getter method for mpls_enabled, mapped from YANG variable /network_instances/network_instance/mpls/global/interface_attributes/interface/config/mpls_enabled (boolean)

    YANG Description: Enable MPLS forwarding on this interface
    """
    return self.__mpls_enabled
      
  def _set_mpls_enabled(self, v, load=False):
    """
    Setter method for mpls_enabled, mapped from YANG variable /network_instances/network_instance/mpls/global/interface_attributes/interface/config/mpls_enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_enabled() directly.

    YANG Description: Enable MPLS forwarding on this interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mpls-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mpls-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__mpls_enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_enabled(self):
    self.__mpls_enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="mpls-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  interface_id = __builtin__.property(_get_interface_id, _set_interface_id)
  mpls_enabled = __builtin__.property(_get_mpls_enabled, _set_mpls_enabled)


  _pyangbind_elements = {'interface_id': interface_id, 'mpls_enabled': mpls_enabled, }


