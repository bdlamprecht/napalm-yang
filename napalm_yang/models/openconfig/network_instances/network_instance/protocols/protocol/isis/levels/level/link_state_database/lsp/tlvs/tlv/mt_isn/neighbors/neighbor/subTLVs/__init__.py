
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import subTLVs_
class subTLVs(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isn/neighbors/neighbor/subTLVs. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container describes IS Neighbor sub-TLVs.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__subTLVs',)

  _yang_name = 'subTLVs'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__subTLVs = YANGDynClass(base=YANGListType("subtlv_type",subTLVs_.subTLVs, yang_name="subTLVs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='subtlv-type', extensions=None), is_container='list', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'mt-isn', u'neighbors', u'neighbor', u'subTLVs']

  def _get_subTLVs(self):
    """
    Getter method for subTLVs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs (list)

    YANG Description: List of subTLV types in the LSDB for the specified TLV.
    """
    return self.__subTLVs
      
  def _set_subTLVs(self, v, load=False):
    """
    Setter method for subTLVs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subTLVs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subTLVs() directly.

    YANG Description: List of subTLV types in the LSDB for the specified TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("subtlv_type",subTLVs_.subTLVs, yang_name="subTLVs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='subtlv-type', extensions=None), is_container='list', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subTLVs must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("subtlv_type",subTLVs_.subTLVs, yang_name="subTLVs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='subtlv-type', extensions=None), is_container='list', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__subTLVs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subTLVs(self):
    self.__subTLVs = YANGDynClass(base=YANGListType("subtlv_type",subTLVs_.subTLVs, yang_name="subTLVs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='subtlv-type', extensions=None), is_container='list', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  subTLVs = __builtin__.property(_get_subTLVs)


  _pyangbind_elements = {'subTLVs': subTLVs, }


import subTLVs_
class subTLVs(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isn/neighbors/neighbor/subTLVs. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container describes IS Neighbor sub-TLVs.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__subTLVs',)

  _yang_name = 'subTLVs'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__subTLVs = YANGDynClass(base=YANGListType("subtlv_type",subTLVs_.subTLVs, yang_name="subTLVs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='subtlv-type', extensions=None), is_container='list', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'mt-isn', u'neighbors', u'neighbor', u'subTLVs']

  def _get_subTLVs(self):
    """
    Getter method for subTLVs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs (list)

    YANG Description: List of subTLV types in the LSDB for the specified TLV.
    """
    return self.__subTLVs
      
  def _set_subTLVs(self, v, load=False):
    """
    Setter method for subTLVs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subTLVs/subTLVs (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subTLVs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subTLVs() directly.

    YANG Description: List of subTLV types in the LSDB for the specified TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("subtlv_type",subTLVs_.subTLVs, yang_name="subTLVs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='subtlv-type', extensions=None), is_container='list', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subTLVs must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("subtlv_type",subTLVs_.subTLVs, yang_name="subTLVs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='subtlv-type', extensions=None), is_container='list', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__subTLVs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subTLVs(self):
    self.__subTLVs = YANGDynClass(base=YANGListType("subtlv_type",subTLVs_.subTLVs, yang_name="subTLVs", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='subtlv-type', extensions=None), is_container='list', yang_name="subTLVs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  subTLVs = __builtin__.property(_get_subTLVs)


  _pyangbind_elements = {'subTLVs': subTLVs, }

