
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

from . import reserved_label_block
class reserved_label_blocks(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/global/reserved-label-blocks. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A range of labels starting with the start-label and up-to and including
the end label that should be allocated as reserved. These labels should
not be utilised by any dynamic label allocation on the local system unless
the allocating protocol is explicitly configured to specify that
allocation of labels should be out of the label block specified.
  """
  __slots__ = ('_path_helper', '_extmethods', '__reserved_label_block',)

  _yang_name = 'reserved-label-blocks'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__reserved_label_block = YANGDynClass(base=YANGListType("local_id",reserved_label_block.reserved_label_block, yang_name="reserved-label-block", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-id', extensions=None), is_container='list', yang_name="reserved-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'global', u'reserved-label-blocks']

  def _get_reserved_label_block(self):
    """
    Getter method for reserved_label_block, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block (list)

    YANG Description: A range of labels starting with the start-label up to and including
the end label that should be allocated for use by a specific protocol.
    """
    return self.__reserved_label_block
      
  def _set_reserved_label_block(self, v, load=False):
    """
    Setter method for reserved_label_block, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reserved_label_block is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reserved_label_block() directly.

    YANG Description: A range of labels starting with the start-label up to and including
the end label that should be allocated for use by a specific protocol.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("local_id",reserved_label_block.reserved_label_block, yang_name="reserved-label-block", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-id', extensions=None), is_container='list', yang_name="reserved-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reserved_label_block must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("local_id",reserved_label_block.reserved_label_block, yang_name="reserved-label-block", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-id', extensions=None), is_container='list', yang_name="reserved-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__reserved_label_block = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reserved_label_block(self):
    self.__reserved_label_block = YANGDynClass(base=YANGListType("local_id",reserved_label_block.reserved_label_block, yang_name="reserved-label-block", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-id', extensions=None), is_container='list', yang_name="reserved-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  reserved_label_block = __builtin__.property(_get_reserved_label_block, _set_reserved_label_block)


  _pyangbind_elements = OrderedDict([('reserved_label_block', reserved_label_block), ])


from . import reserved_label_block
class reserved_label_blocks(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/global/reserved-label-blocks. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A range of labels starting with the start-label and up-to and including
the end label that should be allocated as reserved. These labels should
not be utilised by any dynamic label allocation on the local system unless
the allocating protocol is explicitly configured to specify that
allocation of labels should be out of the label block specified.
  """
  __slots__ = ('_path_helper', '_extmethods', '__reserved_label_block',)

  _yang_name = 'reserved-label-blocks'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__reserved_label_block = YANGDynClass(base=YANGListType("local_id",reserved_label_block.reserved_label_block, yang_name="reserved-label-block", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-id', extensions=None), is_container='list', yang_name="reserved-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'global', u'reserved-label-blocks']

  def _get_reserved_label_block(self):
    """
    Getter method for reserved_label_block, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block (list)

    YANG Description: A range of labels starting with the start-label up to and including
the end label that should be allocated for use by a specific protocol.
    """
    return self.__reserved_label_block
      
  def _set_reserved_label_block(self, v, load=False):
    """
    Setter method for reserved_label_block, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks/reserved_label_block (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reserved_label_block is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reserved_label_block() directly.

    YANG Description: A range of labels starting with the start-label up to and including
the end label that should be allocated for use by a specific protocol.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("local_id",reserved_label_block.reserved_label_block, yang_name="reserved-label-block", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-id', extensions=None), is_container='list', yang_name="reserved-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reserved_label_block must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("local_id",reserved_label_block.reserved_label_block, yang_name="reserved-label-block", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-id', extensions=None), is_container='list', yang_name="reserved-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__reserved_label_block = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reserved_label_block(self):
    self.__reserved_label_block = YANGDynClass(base=YANGListType("local_id",reserved_label_block.reserved_label_block, yang_name="reserved-label-block", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-id', extensions=None), is_container='list', yang_name="reserved-label-block", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  reserved_label_block = __builtin__.property(_get_reserved_label_block, _set_reserved_label_block)


  _pyangbind_elements = OrderedDict([('reserved_label_block', reserved_label_block), ])


