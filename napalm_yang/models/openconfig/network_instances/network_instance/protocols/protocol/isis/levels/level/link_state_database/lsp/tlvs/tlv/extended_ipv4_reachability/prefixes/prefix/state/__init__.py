
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

class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/extended-ipv4-reachability/prefixes/prefix/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of an IPv4 extended prefix.
  """
  __slots__ = ('_path_helper', '_extmethods', '__up_down','__s_bit','__ipv4_prefix','__metric',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__s_bit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="s-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    self.__ipv4_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ipv4-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-prefix', is_config=False)
    self.__up_down = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="up-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:wide-metric', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'extended-ipv4-reachability', u'prefixes', u'prefix', u'state']

  def _get_up_down(self):
    """
    Getter method for up_down, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/up_down (boolean)

    YANG Description: The up/down bit. Set if a prefix is advertised from a higher level to
a lower level (e.g., level 2 to level 1), indicating that the prefix
has traveled down the hierarchy. Prefixes that have the up/down bit
set may only be advertised down the hierarchy, i.e., to lower levels.
When a prefix is first injected into IS-IS, the bit is UNSET.
    """
    return self.__up_down
      
  def _set_up_down(self, v, load=False):
    """
    Setter method for up_down, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/up_down (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_up_down is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_up_down() directly.

    YANG Description: The up/down bit. Set if a prefix is advertised from a higher level to
a lower level (e.g., level 2 to level 1), indicating that the prefix
has traveled down the hierarchy. Prefixes that have the up/down bit
set may only be advertised down the hierarchy, i.e., to lower levels.
When a prefix is first injected into IS-IS, the bit is UNSET.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="up-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """up_down must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="up-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__up_down = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_up_down(self):
    self.__up_down = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="up-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _get_s_bit(self):
    """
    Getter method for s_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/s_bit (boolean)

    YANG Description: The Sub-TLV present bit. If UNSET, the octets of Sub-TLVs are not
present. Otherwise, the bit is set and the octet following the prefix
will contain the length of the Sub-TLV portion of the structure.
    """
    return self.__s_bit
      
  def _set_s_bit(self, v, load=False):
    """
    Setter method for s_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/s_bit (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_s_bit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_s_bit() directly.

    YANG Description: The Sub-TLV present bit. If UNSET, the octets of Sub-TLVs are not
present. Otherwise, the bit is set and the octet following the prefix
will contain the length of the Sub-TLV portion of the structure.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="s-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """s_bit must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="s-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__s_bit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_s_bit(self):
    self.__s_bit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="s-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _get_ipv4_prefix(self):
    """
    Getter method for ipv4_prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/ipv4_prefix (inet:ipv4-prefix)

    YANG Description: IPv4 prefix contained within extended reachability TLVs.
    """
    return self.__ipv4_prefix
      
  def _set_ipv4_prefix(self, v, load=False):
    """
    Setter method for ipv4_prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/ipv4_prefix (inet:ipv4-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_prefix() directly.

    YANG Description: IPv4 prefix contained within extended reachability TLVs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ipv4-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-prefix', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_prefix must be of a type compatible with inet:ipv4-prefix""",
          'defined-type': "inet:ipv4-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ipv4-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-prefix', is_config=False)""",
        })

    self.__ipv4_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_prefix(self):
    self.__ipv4_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ipv4-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-prefix', is_config=False)


  def _get_metric(self):
    """
    Getter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/metric (oc-isis-types:wide-metric)

    YANG Description: ISIS metric value.
    """
    return self.__metric
      
  def _set_metric(self, v, load=False):
    """
    Setter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/metric (oc-isis-types:wide-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric() directly.

    YANG Description: ISIS metric value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:wide-metric', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric must be of a type compatible with oc-isis-types:wide-metric""",
          'defined-type': "oc-isis-types:wide-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:wide-metric', is_config=False)""",
        })

    self.__metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric(self):
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:wide-metric', is_config=False)

  up_down = __builtin__.property(_get_up_down)
  s_bit = __builtin__.property(_get_s_bit)
  ipv4_prefix = __builtin__.property(_get_ipv4_prefix)
  metric = __builtin__.property(_get_metric)


  _pyangbind_elements = OrderedDict([('up_down', up_down), ('s_bit', s_bit), ('ipv4_prefix', ipv4_prefix), ('metric', metric), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/extended-ipv4-reachability/prefixes/prefix/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of an IPv4 extended prefix.
  """
  __slots__ = ('_path_helper', '_extmethods', '__up_down','__s_bit','__ipv4_prefix','__metric',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__s_bit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="s-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    self.__ipv4_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ipv4-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-prefix', is_config=False)
    self.__up_down = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="up-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:wide-metric', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'extended-ipv4-reachability', u'prefixes', u'prefix', u'state']

  def _get_up_down(self):
    """
    Getter method for up_down, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/up_down (boolean)

    YANG Description: The up/down bit. Set if a prefix is advertised from a higher level to
a lower level (e.g., level 2 to level 1), indicating that the prefix
has traveled down the hierarchy. Prefixes that have the up/down bit
set may only be advertised down the hierarchy, i.e., to lower levels.
When a prefix is first injected into IS-IS, the bit is UNSET.
    """
    return self.__up_down
      
  def _set_up_down(self, v, load=False):
    """
    Setter method for up_down, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/up_down (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_up_down is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_up_down() directly.

    YANG Description: The up/down bit. Set if a prefix is advertised from a higher level to
a lower level (e.g., level 2 to level 1), indicating that the prefix
has traveled down the hierarchy. Prefixes that have the up/down bit
set may only be advertised down the hierarchy, i.e., to lower levels.
When a prefix is first injected into IS-IS, the bit is UNSET.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="up-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """up_down must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="up-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__up_down = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_up_down(self):
    self.__up_down = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="up-down", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _get_s_bit(self):
    """
    Getter method for s_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/s_bit (boolean)

    YANG Description: The Sub-TLV present bit. If UNSET, the octets of Sub-TLVs are not
present. Otherwise, the bit is set and the octet following the prefix
will contain the length of the Sub-TLV portion of the structure.
    """
    return self.__s_bit
      
  def _set_s_bit(self, v, load=False):
    """
    Setter method for s_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/s_bit (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_s_bit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_s_bit() directly.

    YANG Description: The Sub-TLV present bit. If UNSET, the octets of Sub-TLVs are not
present. Otherwise, the bit is set and the octet following the prefix
will contain the length of the Sub-TLV portion of the structure.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="s-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """s_bit must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="s-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__s_bit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_s_bit(self):
    self.__s_bit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="s-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _get_ipv4_prefix(self):
    """
    Getter method for ipv4_prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/ipv4_prefix (inet:ipv4-prefix)

    YANG Description: IPv4 prefix contained within extended reachability TLVs.
    """
    return self.__ipv4_prefix
      
  def _set_ipv4_prefix(self, v, load=False):
    """
    Setter method for ipv4_prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/ipv4_prefix (inet:ipv4-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_prefix() directly.

    YANG Description: IPv4 prefix contained within extended reachability TLVs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ipv4-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-prefix', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_prefix must be of a type compatible with inet:ipv4-prefix""",
          'defined-type': "inet:ipv4-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ipv4-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-prefix', is_config=False)""",
        })

    self.__ipv4_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_prefix(self):
    self.__ipv4_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ipv4-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-prefix', is_config=False)


  def _get_metric(self):
    """
    Getter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/metric (oc-isis-types:wide-metric)

    YANG Description: ISIS metric value.
    """
    return self.__metric
      
  def _set_metric(self, v, load=False):
    """
    Setter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/extended_ipv4_reachability/prefixes/prefix/state/metric (oc-isis-types:wide-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric() directly.

    YANG Description: ISIS metric value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:wide-metric', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric must be of a type compatible with oc-isis-types:wide-metric""",
          'defined-type': "oc-isis-types:wide-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:wide-metric', is_config=False)""",
        })

    self.__metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric(self):
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:wide-metric', is_config=False)

  up_down = __builtin__.property(_get_up_down)
  s_bit = __builtin__.property(_get_s_bit)
  ipv4_prefix = __builtin__.property(_get_ipv4_prefix)
  metric = __builtin__.property(_get_metric)


  _pyangbind_elements = OrderedDict([('up_down', up_down), ('s_bit', s_bit), ('ipv4_prefix', ipv4_prefix), ('metric', metric), ])


