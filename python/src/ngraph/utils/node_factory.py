from typing import Any, Dict, List, Optional

from _pyngraph import NodeFactory as _NodeFactory

from ngraph.impl import Node


class NodeFactory(object):
    """Factory front-end to create node objects."""

    def __init__(self, opset_version='opset1'):  # type: (str) -> None
        """Create the NodeFactory object.

        :param      opset_version:  The opset version the factory will use to produce ops from.
        """
        self.factory = _NodeFactory(opset_version)

    def create(self, op_type_name, arguments, attributes=None):
        # type: (str, List[Node], Optional[Dict[str, Any]]) -> Node
        """Create node object from provided description.

        :param      op_type_name:  The operator type name.
        :param      arguments:     The operator arguments.
        :param      attributes:    The operator attributes.

        :returns:   Node object representing requested operator with attributes set.
        """
        if attributes is None:
            attributes = {}
        node = self.factory.create(op_type_name, arguments, attributes)
        return node
