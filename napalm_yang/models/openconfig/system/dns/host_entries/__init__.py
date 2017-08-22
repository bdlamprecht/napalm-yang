
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

from . import host_entry
class host_entries(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/dns/host-entries. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for list of static host entries
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__host_entry',)

  _yang_name = 'host-entries'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__host_entry = YANGDynClass(base=YANGListType("hostname",host_entry.host_entry, yang_name="host-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostname', extensions=None), is_container='list', yang_name="host-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='list', is_config=True)

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
      return [u'system', u'dns', u'host-entries']

  def _get_host_entry(self):
    """
    Getter method for host_entry, mapped from YANG variable /system/dns/host_entries/host_entry (list)

    YANG Description: List of static host entries
    """
    return self.__host_entry
      
  def _set_host_entry(self, v, load=False):
    """
    Setter method for host_entry, mapped from YANG variable /system/dns/host_entries/host_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host_entry() directly.

    YANG Description: List of static host entries
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("hostname",host_entry.host_entry, yang_name="host-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostname', extensions=None), is_container='list', yang_name="host-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("hostname",host_entry.host_entry, yang_name="host-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostname', extensions=None), is_container='list', yang_name="host-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='list', is_config=True)""",
        })

    self.__host_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host_entry(self):
    self.__host_entry = YANGDynClass(base=YANGListType("hostname",host_entry.host_entry, yang_name="host-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostname', extensions=None), is_container='list', yang_name="host-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='list', is_config=True)

  host_entry = __builtin__.property(_get_host_entry, _set_host_entry)


  _pyangbind_elements = {'host_entry': host_entry, }


