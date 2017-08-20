
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
  from YANG module openconfig-vlan - based on the path /vlans/vlan/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for VLANs
  """
  __slots__ = ('_path_helper', '_extmethods', '__vlan_id','__name','__status','__tpid',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACTIVE': {}, u'SUSPENDED': {}},), default=unicode("ACTIVE"), is_leaf=True, yang_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='enumeration', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='string', is_config=True)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    self.__tpid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-vlan-types:TPID_0X9200': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'oc-vlan-types:TPID_0x8100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0x9100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0x8A88': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0X9200': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'oc-vlan-types:TPID_0x8A88': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0x8100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'oc-vlan-types:TPID_0x9100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}},), default=unicode("oc-vlan-types:TPID_0x8100"), is_leaf=True, yang_name="tpid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='identityref', is_config=True)

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
      return [u'vlans', u'vlan', u'config']

  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /vlans/vlan/config/vlan_id (oc-vlan-types:vlan-id)

    YANG Description: Interface VLAN id.
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /vlans/vlan/config/vlan_id (oc-vlan-types:vlan-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: Interface VLAN id.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with oc-vlan-types:vlan-id""",
          'defined-type': "oc-vlan-types:vlan-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)


  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /vlans/vlan/config/name (string)

    YANG Description: Interface VLAN name.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /vlans/vlan/config/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Interface VLAN name.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='string', is_config=True)


  def _get_status(self):
    """
    Getter method for status, mapped from YANG variable /vlans/vlan/config/status (enumeration)

    YANG Description: Admin state of the VLAN
    """
    return self.__status
      
  def _set_status(self, v, load=False):
    """
    Setter method for status, mapped from YANG variable /vlans/vlan/config/status (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_status() directly.

    YANG Description: Admin state of the VLAN
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACTIVE': {}, u'SUSPENDED': {}},), default=unicode("ACTIVE"), is_leaf=True, yang_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """status must be of a type compatible with enumeration""",
          'defined-type': "openconfig-vlan:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACTIVE': {}, u'SUSPENDED': {}},), default=unicode("ACTIVE"), is_leaf=True, yang_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='enumeration', is_config=True)""",
        })

    self.__status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_status(self):
    self.__status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACTIVE': {}, u'SUSPENDED': {}},), default=unicode("ACTIVE"), is_leaf=True, yang_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='enumeration', is_config=True)


  def _get_tpid(self):
    """
    Getter method for tpid, mapped from YANG variable /vlans/vlan/config/tpid (identityref)

    YANG Description: Optionally set the tag protocol identifier field (TPID) that
is accepted on the VLAN
    """
    return self.__tpid
      
  def _set_tpid(self, v, load=False):
    """
    Setter method for tpid, mapped from YANG variable /vlans/vlan/config/tpid (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tpid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tpid() directly.

    YANG Description: Optionally set the tag protocol identifier field (TPID) that
is accepted on the VLAN
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-vlan-types:TPID_0X9200': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'oc-vlan-types:TPID_0x8100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0x9100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0x8A88': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0X9200': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'oc-vlan-types:TPID_0x8A88': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0x8100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'oc-vlan-types:TPID_0x9100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}},), default=unicode("oc-vlan-types:TPID_0x8100"), is_leaf=True, yang_name="tpid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tpid must be of a type compatible with identityref""",
          'defined-type': "openconfig-vlan:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-vlan-types:TPID_0X9200': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'oc-vlan-types:TPID_0x8100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0x9100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0x8A88': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0X9200': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'oc-vlan-types:TPID_0x8A88': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0x8100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'oc-vlan-types:TPID_0x9100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}},), default=unicode("oc-vlan-types:TPID_0x8100"), is_leaf=True, yang_name="tpid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='identityref', is_config=True)""",
        })

    self.__tpid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tpid(self):
    self.__tpid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-vlan-types:TPID_0X9200': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'oc-vlan-types:TPID_0x8100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0x9100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0x8A88': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0X9200': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'oc-vlan-types:TPID_0x8A88': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'TPID_0x8100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}, u'oc-vlan-types:TPID_0x9100': {'@namespace': u'http://openconfig.net/yang/vlan-types', '@module': u'openconfig-vlan-types'}},), default=unicode("oc-vlan-types:TPID_0x8100"), is_leaf=True, yang_name="tpid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='identityref', is_config=True)

  vlan_id = __builtin__.property(_get_vlan_id, _set_vlan_id)
  name = __builtin__.property(_get_name, _set_name)
  status = __builtin__.property(_get_status, _set_status)
  tpid = __builtin__.property(_get_tpid, _set_tpid)


  _pyangbind_elements = OrderedDict([('vlan_id', vlan_id), ('name', name), ('status', status), ('tpid', tpid), ])


