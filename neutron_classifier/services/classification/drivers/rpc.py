# Copyright 2017 Intel. All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_log import log as logging

import oslo_messaging

from neutron.common import rpc as n_rpc
from neutron.common import topics

from neutron_classifier._i18n import _LI

LOG = logging.getLogger(__name__)


class ClassificationRpcCallback(object):
    """Classification RPC server."""

    def __init__(self, driver):
        self.target = oslo_messaging.Target(version='1.0')
        self.driver = driver

    def get_classification_by_id(self, context, **kwargs):
        classification_id = kwargs.get('id')
        LOG.debug('from neutron_classifier service plugin')
        context.translate=None
        LOG.debug('David, context.translate=None')
        classification = self.driver.get_classification(
            context, classification_id)
        return classification
