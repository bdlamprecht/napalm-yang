
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/global/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level global MPLS configuration
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__null_label',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__null_label = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mpls-t:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:IMPLICIT"), is_leaf=True, yang_name="null-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'global', u'config']

  def _get_null_label(self):
    """
    Getter method for null_label, mapped from YANG variable /network_instances/network_instance/mpls/global/config/null_label (identityref)

    YANG Description: The null-label type used, implicit or explicit
    """
    return self.__null_label
      
  def _set_null_label(self, v, load=False):
    """
    Setter method for null_label, mapped from YANG variable /network_instances/network_instance/mpls/global/config/null_label (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_null_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_null_label() directly.

    YANG Description: The null-label type used, implicit or explicit
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mpls-t:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:IMPLICIT"), is_leaf=True, yang_name="null-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """null_label must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mpls-t:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:IMPLICIT"), is_leaf=True, yang_name="null-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
        })

    self.__null_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_null_label(self):
    self.__null_label = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mpls-t:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:IMPLICIT"), is_leaf=True, yang_name="null-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)

  null_label = __builtin__.property(_get_null_label, _set_null_label)


  _pyangbind_elements = {'null_label': null_label, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/global/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level global MPLS configuration
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__null_label',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__null_label = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mpls-t:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:IMPLICIT"), is_leaf=True, yang_name="null-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'global', u'config']

  def _get_null_label(self):
    """
    Getter method for null_label, mapped from YANG variable /network_instances/network_instance/mpls/global/config/null_label (identityref)

    YANG Description: The null-label type used, implicit or explicit
    """
    return self.__null_label
      
  def _set_null_label(self, v, load=False):
    """
    Setter method for null_label, mapped from YANG variable /network_instances/network_instance/mpls/global/config/null_label (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_null_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_null_label() directly.

    YANG Description: The null-label type used, implicit or explicit
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mpls-t:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:IMPLICIT"), is_leaf=True, yang_name="null-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """null_label must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mpls-t:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:IMPLICIT"), is_leaf=True, yang_name="null-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
        })

    self.__null_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_null_label(self):
    self.__null_label = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mpls-t:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:EXPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'IMPLICIT': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:IMPLICIT"), is_leaf=True, yang_name="null-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)

  null_label = __builtin__.property(_get_null_label, _set_null_label)


  _pyangbind_elements = {'null_label': null_label, }


