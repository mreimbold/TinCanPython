#    Copyright 2014 Rustici Software
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import uuid
import re
from tincan.serializable_base import SerializableBase

"""
.. module StatementRef
   :synopsis: A StatementRef object that is a reference to another pre-existing statement.
"""


class StatementRef(SerializableBase):

    _UUID_REGEX = re.compile(
        r'^[a-f0-9]{8}-'
        r'[a-f0-9]{4}-'
        r'[1-5][a-f0-9]{3}-'
        r'[89ab][a-f0-9]{3}-'
        r'[a-f0-9]{12}$'
    )

    _props_req = [
        'object_type'
    ]

    _props = [
        'id'
    ]

    _props.extend(_props_req)

    @property
    def object_type(self):
        """Object type for Statement Ref. Will always be "StatementRef"

        :setter: Tries to convert to unicode
        :setter type: unicode
        :rtype: unicode

        """
        return self._object_type

    @object_type.setter
    def object_type(self, value):
        self._object_type = 'StatementRef'

    @property
    def id(self):
        """Id for Statement Ref

        :setter: Tries to convert to unicode
        :setter type: unicode
        :rtype: unicode

        """
        return self._id

    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, uuid.UUID):
            if isinstance(value, basestring) and not self._UUID_REGEX.match(value):
                raise ValueError("Invalid UUID string")
            value = uuid.UUID(value)
        self._id = value

    @id.deleter
    def id(self):
        del(self._id)
