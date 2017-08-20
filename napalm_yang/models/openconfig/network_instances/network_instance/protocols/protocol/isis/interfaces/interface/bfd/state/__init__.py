
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/bfd/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines BFD state information.
  """
  __slots__ = ('_path_helper', '_extmethods', '__bfd_tlv',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bfd_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'interfaces', u'interface', u'bfd', u'state']

  def _get_bfd_tlv(self):
    """
    Getter method for bfd_tlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/bfd/state/bfd_tlv (boolean)

    YANG Description: When set to true, BFD TLV is used. This enables support for the IS-IS
BFD TLV options, which specify that a BFD session must be established
before an IS-IS adjacency can transition to the established state.
This option should be enabled on all IS-IS neighbors on a shared
interface.
    """
    return self.__bfd_tlv
      
  def _set_bfd_tlv(self, v, load=False):
    """
    Setter method for bfd_tlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/bfd/state/bfd_tlv (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_tlv() directly.

    YANG Description: When set to true, BFD TLV is used. This enables support for the IS-IS
BFD TLV options, which specify that a BFD session must be established
before an IS-IS adjacency can transition to the established state.
This option should be enabled on all IS-IS neighbors on a shared
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="bfd-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_tlv must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__bfd_tlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_tlv(self):
    self.__bfd_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  bfd_tlv = __builtin__.property(_get_bfd_tlv)


  _pyangbind_elements = OrderedDict([('bfd_tlv', bfd_tlv), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/bfd/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines BFD state information.
  """
  __slots__ = ('_path_helper', '_extmethods', '__bfd_tlv',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bfd_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'interfaces', u'interface', u'bfd', u'state']

  def _get_bfd_tlv(self):
    """
    Getter method for bfd_tlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/bfd/state/bfd_tlv (boolean)

    YANG Description: When set to true, BFD TLV is used. This enables support for the IS-IS
BFD TLV options, which specify that a BFD session must be established
before an IS-IS adjacency can transition to the established state.
This option should be enabled on all IS-IS neighbors on a shared
interface.
    """
    return self.__bfd_tlv
      
  def _set_bfd_tlv(self, v, load=False):
    """
    Setter method for bfd_tlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/bfd/state/bfd_tlv (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_tlv() directly.

    YANG Description: When set to true, BFD TLV is used. This enables support for the IS-IS
BFD TLV options, which specify that a BFD session must be established
before an IS-IS adjacency can transition to the established state.
This option should be enabled on all IS-IS neighbors on a shared
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="bfd-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_tlv must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__bfd_tlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_tlv(self):
    self.__bfd_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  bfd_tlv = __builtin__.property(_get_bfd_tlv)


  _pyangbind_elements = OrderedDict([('bfd_tlv', bfd_tlv), ])


