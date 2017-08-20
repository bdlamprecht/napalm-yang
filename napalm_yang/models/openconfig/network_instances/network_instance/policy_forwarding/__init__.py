
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

from . import policies
from . import interfaces
from . import path_selection_groups
class policy_forwarding(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/policy-forwarding. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state relating to policy-forwarding within
a network instance.
  """
  __slots__ = ('_path_helper', '_extmethods', '__policies','__interfaces','__path_selection_groups',)

  _yang_name = 'policy-forwarding'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__path_selection_groups = YANGDynClass(base=path_selection_groups.path_selection_groups, is_container='container', yang_name="path-selection-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__policies = YANGDynClass(base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'policy-forwarding']

  def _get_policies(self):
    """
    Getter method for policies, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies (container)

    YANG Description: Forwarding policies defined to enact policy-based forwarding
on the local system.
    """
    return self.__policies
      
  def _set_policies(self, v, load=False):
    """
    Setter method for policies, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policies is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policies() directly.

    YANG Description: Forwarding policies defined to enact policy-based forwarding
on the local system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policies must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__policies = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policies(self):
    self.__policies = YANGDynClass(base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_interfaces(self):
    """
    Getter method for interfaces, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces (container)

    YANG Description: Configuration and operational state relating policy
forwarding on interfaces.
    """
    return self.__interfaces
      
  def _set_interfaces(self, v, load=False):
    """
    Setter method for interfaces, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interfaces() directly.

    YANG Description: Configuration and operational state relating policy
forwarding on interfaces.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interfaces must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interfaces(self):
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_path_selection_groups(self):
    """
    Getter method for path_selection_groups, mapped from YANG variable /network_instances/network_instance/policy_forwarding/path_selection_groups (container)

    YANG Description: Surrounding container for the path selection groups defined
within the policy forwarding model.
    """
    return self.__path_selection_groups
      
  def _set_path_selection_groups(self, v, load=False):
    """
    Setter method for path_selection_groups, mapped from YANG variable /network_instances/network_instance/policy_forwarding/path_selection_groups (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_selection_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_selection_groups() directly.

    YANG Description: Surrounding container for the path selection groups defined
within the policy forwarding model.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=path_selection_groups.path_selection_groups, is_container='container', yang_name="path-selection-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_selection_groups must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=path_selection_groups.path_selection_groups, is_container='container', yang_name="path-selection-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__path_selection_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_selection_groups(self):
    self.__path_selection_groups = YANGDynClass(base=path_selection_groups.path_selection_groups, is_container='container', yang_name="path-selection-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  policies = __builtin__.property(_get_policies, _set_policies)
  interfaces = __builtin__.property(_get_interfaces, _set_interfaces)
  path_selection_groups = __builtin__.property(_get_path_selection_groups, _set_path_selection_groups)


  _pyangbind_elements = OrderedDict([('policies', policies), ('interfaces', interfaces), ('path_selection_groups', path_selection_groups), ])


from . import policies
from . import interfaces
from . import path_selection_groups
class policy_forwarding(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/policy-forwarding. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state relating to policy-forwarding within
a network instance.
  """
  __slots__ = ('_path_helper', '_extmethods', '__policies','__interfaces','__path_selection_groups',)

  _yang_name = 'policy-forwarding'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__path_selection_groups = YANGDynClass(base=path_selection_groups.path_selection_groups, is_container='container', yang_name="path-selection-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__policies = YANGDynClass(base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'policy-forwarding']

  def _get_policies(self):
    """
    Getter method for policies, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies (container)

    YANG Description: Forwarding policies defined to enact policy-based forwarding
on the local system.
    """
    return self.__policies
      
  def _set_policies(self, v, load=False):
    """
    Setter method for policies, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policies is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policies() directly.

    YANG Description: Forwarding policies defined to enact policy-based forwarding
on the local system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policies must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__policies = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policies(self):
    self.__policies = YANGDynClass(base=policies.policies, is_container='container', yang_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_interfaces(self):
    """
    Getter method for interfaces, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces (container)

    YANG Description: Configuration and operational state relating policy
forwarding on interfaces.
    """
    return self.__interfaces
      
  def _set_interfaces(self, v, load=False):
    """
    Setter method for interfaces, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interfaces() directly.

    YANG Description: Configuration and operational state relating policy
forwarding on interfaces.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interfaces must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interfaces(self):
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_path_selection_groups(self):
    """
    Getter method for path_selection_groups, mapped from YANG variable /network_instances/network_instance/policy_forwarding/path_selection_groups (container)

    YANG Description: Surrounding container for the path selection groups defined
within the policy forwarding model.
    """
    return self.__path_selection_groups
      
  def _set_path_selection_groups(self, v, load=False):
    """
    Setter method for path_selection_groups, mapped from YANG variable /network_instances/network_instance/policy_forwarding/path_selection_groups (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_selection_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_selection_groups() directly.

    YANG Description: Surrounding container for the path selection groups defined
within the policy forwarding model.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=path_selection_groups.path_selection_groups, is_container='container', yang_name="path-selection-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_selection_groups must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=path_selection_groups.path_selection_groups, is_container='container', yang_name="path-selection-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__path_selection_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_selection_groups(self):
    self.__path_selection_groups = YANGDynClass(base=path_selection_groups.path_selection_groups, is_container='container', yang_name="path-selection-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  policies = __builtin__.property(_get_policies, _set_policies)
  interfaces = __builtin__.property(_get_interfaces, _set_interfaces)
  path_selection_groups = __builtin__.property(_get_path_selection_groups, _set_path_selection_groups)


  _pyangbind_elements = OrderedDict([('policies', policies), ('interfaces', interfaces), ('path_selection_groups', path_selection_groups), ])


