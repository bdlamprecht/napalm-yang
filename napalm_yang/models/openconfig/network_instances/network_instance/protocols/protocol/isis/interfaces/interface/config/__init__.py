
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS interface configuration.
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__interface_id','__passive','__hello_padding','__circuit_type',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__passive = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__circuit_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'BROADCAST': {}, u'POINT_TO_POINT': {}},), is_leaf=True, yang_name="circuit-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:circuit-type', is_config=True)
    self.__hello_padding = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'STRICT': {}, u'ADAPTIVE': {}, u'LOOSE': {}, u'DISABLE': {}},), is_leaf=True, yang_name="hello-padding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:hello-padding-type', is_config=True)
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'interfaces', u'interface', u'config']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/enabled (boolean)

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_interface_id(self):
    """
    Getter method for interface_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/interface_id (oc-if:interface-id)

    YANG Description: Interface for which ISIS configuration is to be applied.
    """
    return self.__interface_id
      
  def _set_interface_id(self, v, load=False):
    """
    Setter method for interface_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/interface_id (oc-if:interface-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: Interface for which ISIS configuration is to be applied.
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


  def _get_passive(self):
    """
    Getter method for passive, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/passive (boolean)

    YANG Description: When set to true, the referenced interface is a passive interface
such that it is not eligible to establish adjacencies with other
systems, but is advertised into the IS-IS topology.
    """
    return self.__passive
      
  def _set_passive(self, v, load=False):
    """
    Setter method for passive, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/passive (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_passive is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_passive() directly.

    YANG Description: When set to true, the referenced interface is a passive interface
such that it is not eligible to establish adjacencies with other
systems, but is advertised into the IS-IS topology.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """passive must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__passive = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_passive(self):
    self.__passive = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_hello_padding(self):
    """
    Getter method for hello_padding, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/hello_padding (oc-isis-types:hello-padding-type)

    YANG Description: This leaf controls padding type for IS-IS Hello PDUs.
    """
    return self.__hello_padding
      
  def _set_hello_padding(self, v, load=False):
    """
    Setter method for hello_padding, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/hello_padding (oc-isis-types:hello-padding-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_padding is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_padding() directly.

    YANG Description: This leaf controls padding type for IS-IS Hello PDUs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'STRICT': {}, u'ADAPTIVE': {}, u'LOOSE': {}, u'DISABLE': {}},), is_leaf=True, yang_name="hello-padding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:hello-padding-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_padding must be of a type compatible with oc-isis-types:hello-padding-type""",
          'defined-type': "oc-isis-types:hello-padding-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'STRICT': {}, u'ADAPTIVE': {}, u'LOOSE': {}, u'DISABLE': {}},), is_leaf=True, yang_name="hello-padding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:hello-padding-type', is_config=True)""",
        })

    self.__hello_padding = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_padding(self):
    self.__hello_padding = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'STRICT': {}, u'ADAPTIVE': {}, u'LOOSE': {}, u'DISABLE': {}},), is_leaf=True, yang_name="hello-padding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:hello-padding-type', is_config=True)


  def _get_circuit_type(self):
    """
    Getter method for circuit_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/circuit_type (oc-isis-types:circuit-type)

    YANG Description: ISIS circuit type (p2p, broadcast).
    """
    return self.__circuit_type
      
  def _set_circuit_type(self, v, load=False):
    """
    Setter method for circuit_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/circuit_type (oc-isis-types:circuit-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_circuit_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_circuit_type() directly.

    YANG Description: ISIS circuit type (p2p, broadcast).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'BROADCAST': {}, u'POINT_TO_POINT': {}},), is_leaf=True, yang_name="circuit-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:circuit-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """circuit_type must be of a type compatible with oc-isis-types:circuit-type""",
          'defined-type': "oc-isis-types:circuit-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'BROADCAST': {}, u'POINT_TO_POINT': {}},), is_leaf=True, yang_name="circuit-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:circuit-type', is_config=True)""",
        })

    self.__circuit_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_circuit_type(self):
    self.__circuit_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'BROADCAST': {}, u'POINT_TO_POINT': {}},), is_leaf=True, yang_name="circuit-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:circuit-type', is_config=True)

  enabled = __builtin__.property(_get_enabled, _set_enabled)
  interface_id = __builtin__.property(_get_interface_id, _set_interface_id)
  passive = __builtin__.property(_get_passive, _set_passive)
  hello_padding = __builtin__.property(_get_hello_padding, _set_hello_padding)
  circuit_type = __builtin__.property(_get_circuit_type, _set_circuit_type)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('interface_id', interface_id), ('passive', passive), ('hello_padding', hello_padding), ('circuit_type', circuit_type), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS interface configuration.
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__interface_id','__passive','__hello_padding','__circuit_type',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__passive = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__circuit_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'BROADCAST': {}, u'POINT_TO_POINT': {}},), is_leaf=True, yang_name="circuit-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:circuit-type', is_config=True)
    self.__hello_padding = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'STRICT': {}, u'ADAPTIVE': {}, u'LOOSE': {}, u'DISABLE': {}},), is_leaf=True, yang_name="hello-padding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:hello-padding-type', is_config=True)
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'interfaces', u'interface', u'config']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/enabled (boolean)

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_interface_id(self):
    """
    Getter method for interface_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/interface_id (oc-if:interface-id)

    YANG Description: Interface for which ISIS configuration is to be applied.
    """
    return self.__interface_id
      
  def _set_interface_id(self, v, load=False):
    """
    Setter method for interface_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/interface_id (oc-if:interface-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: Interface for which ISIS configuration is to be applied.
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


  def _get_passive(self):
    """
    Getter method for passive, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/passive (boolean)

    YANG Description: When set to true, the referenced interface is a passive interface
such that it is not eligible to establish adjacencies with other
systems, but is advertised into the IS-IS topology.
    """
    return self.__passive
      
  def _set_passive(self, v, load=False):
    """
    Setter method for passive, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/passive (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_passive is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_passive() directly.

    YANG Description: When set to true, the referenced interface is a passive interface
such that it is not eligible to establish adjacencies with other
systems, but is advertised into the IS-IS topology.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """passive must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__passive = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_passive(self):
    self.__passive = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_hello_padding(self):
    """
    Getter method for hello_padding, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/hello_padding (oc-isis-types:hello-padding-type)

    YANG Description: This leaf controls padding type for IS-IS Hello PDUs.
    """
    return self.__hello_padding
      
  def _set_hello_padding(self, v, load=False):
    """
    Setter method for hello_padding, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/hello_padding (oc-isis-types:hello-padding-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_padding is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_padding() directly.

    YANG Description: This leaf controls padding type for IS-IS Hello PDUs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'STRICT': {}, u'ADAPTIVE': {}, u'LOOSE': {}, u'DISABLE': {}},), is_leaf=True, yang_name="hello-padding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:hello-padding-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_padding must be of a type compatible with oc-isis-types:hello-padding-type""",
          'defined-type': "oc-isis-types:hello-padding-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'STRICT': {}, u'ADAPTIVE': {}, u'LOOSE': {}, u'DISABLE': {}},), is_leaf=True, yang_name="hello-padding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:hello-padding-type', is_config=True)""",
        })

    self.__hello_padding = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_padding(self):
    self.__hello_padding = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'STRICT': {}, u'ADAPTIVE': {}, u'LOOSE': {}, u'DISABLE': {}},), is_leaf=True, yang_name="hello-padding", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:hello-padding-type', is_config=True)


  def _get_circuit_type(self):
    """
    Getter method for circuit_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/circuit_type (oc-isis-types:circuit-type)

    YANG Description: ISIS circuit type (p2p, broadcast).
    """
    return self.__circuit_type
      
  def _set_circuit_type(self, v, load=False):
    """
    Setter method for circuit_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/config/circuit_type (oc-isis-types:circuit-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_circuit_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_circuit_type() directly.

    YANG Description: ISIS circuit type (p2p, broadcast).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'BROADCAST': {}, u'POINT_TO_POINT': {}},), is_leaf=True, yang_name="circuit-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:circuit-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """circuit_type must be of a type compatible with oc-isis-types:circuit-type""",
          'defined-type': "oc-isis-types:circuit-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'BROADCAST': {}, u'POINT_TO_POINT': {}},), is_leaf=True, yang_name="circuit-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:circuit-type', is_config=True)""",
        })

    self.__circuit_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_circuit_type(self):
    self.__circuit_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'BROADCAST': {}, u'POINT_TO_POINT': {}},), is_leaf=True, yang_name="circuit-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:circuit-type', is_config=True)

  enabled = __builtin__.property(_get_enabled, _set_enabled)
  interface_id = __builtin__.property(_get_interface_id, _set_interface_id)
  passive = __builtin__.property(_get_passive, _set_passive)
  hello_padding = __builtin__.property(_get_hello_padding, _set_hello_padding)
  circuit_type = __builtin__.property(_get_circuit_type, _set_circuit_type)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('interface_id', interface_id), ('passive', passive), ('hello_padding', hello_padding), ('circuit_type', circuit_type), ])


