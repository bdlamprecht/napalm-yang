
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

from . import config
from . import state
from . import interface_tracking
class vrrp_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces/subinterface/ipv6/addresses/address/vrrp/vrrp-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of VRRP groups, keyed by virtual router id
  """
  __slots__ = ('_path_helper', '_extmethods', '__virtual_router_id','__config','__state','__interface_tracking',)

  _yang_name = 'vrrp-group'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)
    self.__virtual_router_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="virtual-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='leafref', is_config=True)
    self.__interface_tracking = YANGDynClass(base=interface_tracking.interface_tracking, is_container='container', yang_name="interface-tracking", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)

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
      return [u'interfaces', u'interface', u'subinterfaces', u'subinterface', u'ipv6', u'addresses', u'address', u'vrrp', u'vrrp-group']

  def _get_virtual_router_id(self):
    """
    Getter method for virtual_router_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/addresses/address/vrrp/vrrp_group/virtual_router_id (leafref)

    YANG Description: References the configured virtual router id for this
VRRP group
    """
    return self.__virtual_router_id
      
  def _set_virtual_router_id(self, v, load=False):
    """
    Setter method for virtual_router_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/addresses/address/vrrp/vrrp_group/virtual_router_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual_router_id() directly.

    YANG Description: References the configured virtual router id for this
VRRP group
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="virtual-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual_router_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="virtual-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='leafref', is_config=True)""",
        })

    self.__virtual_router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual_router_id(self):
    self.__virtual_router_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="virtual-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/addresses/address/vrrp/vrrp_group/config (container)

    YANG Description: Configuration data for the VRRP group
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/addresses/address/vrrp/vrrp_group/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for the VRRP group
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/addresses/address/vrrp/vrrp_group/state (container)

    YANG Description: Operational state data for the VRRP group
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/addresses/address/vrrp/vrrp_group/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data for the VRRP group
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)


  def _get_interface_tracking(self):
    """
    Getter method for interface_tracking, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/addresses/address/vrrp/vrrp_group/interface_tracking (container)

    YANG Description: Top-level container for VRRP interface tracking
    """
    return self.__interface_tracking
      
  def _set_interface_tracking(self, v, load=False):
    """
    Setter method for interface_tracking, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/addresses/address/vrrp/vrrp_group/interface_tracking (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_tracking is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_tracking() directly.

    YANG Description: Top-level container for VRRP interface tracking
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_tracking.interface_tracking, is_container='container', yang_name="interface-tracking", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_tracking must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_tracking.interface_tracking, is_container='container', yang_name="interface-tracking", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)""",
        })

    self.__interface_tracking = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_tracking(self):
    self.__interface_tracking = YANGDynClass(base=interface_tracking.interface_tracking, is_container='container', yang_name="interface-tracking", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='container', is_config=True)

  virtual_router_id = __builtin__.property(_get_virtual_router_id, _set_virtual_router_id)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  interface_tracking = __builtin__.property(_get_interface_tracking, _set_interface_tracking)


  _pyangbind_elements = OrderedDict([('virtual_router_id', virtual_router_id), ('config', config), ('state', state), ('interface_tracking', interface_tracking), ])


