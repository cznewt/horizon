# vim: tabstop=4 shiftwidth=4 softtabstop=4

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
#
# @author: Abishek Subramanian, Cisco Systems, Inc.
# @author: Sergey Sudakovich,   Cisco Systems, Inc.

import logging

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tables

from openstack_dashboard import api

LOG = logging.getLogger(__name__)


class CreateNetworkProfile(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Network Profile")
    url = "horizon:router:nexus1000v:create_network_profile"
    classes = ("ajax-modal", "btn-create")


class DeleteNetworkProfile(tables.DeleteAction):
    data_type_singular = _("Network Profile")
    data_type_plural = _("Network Profiles")

    def delete(self, request, obj_id):
        try:
            api.neutron.profile_delete(request, obj_id)
        except Exception:
            msg = _('Failed to delete network profile (%s).') % obj_id
            LOG.info(msg)
            redirect = reverse('horizon:router:nexus1000v:index')
            exceptions.handle(request, msg, redirect=redirect)


class EditNetworkProfile(tables.LinkAction):
    name = "update"
    verbose_name = _("Edit Network Profile")
    url = "horizon:router:nexus1000v:update_network_profile"
    classes = ("ajax-modal", "btn-edit")


class NetworkProfile(tables.DataTable):
    id = tables.Column("profile_id", verbose_name=_("Profile ID"), hidden=True)
    name = tables.Column("name", verbose_name=_("Network Profile"), )
    project = tables.Column("project_name", verbose_name=_("Project"))
    segment_type = tables.Column("segment_type",
                                 verbose_name=_("Segment Type"))
    segment_range = tables.Column("segment_range",
                                  verbose_name=_("Segment Range"))
    multicast_ip_range = tables.Column("multicast_ip_range",
                                       verbose_name=_("Multicast IP Range"))
    physical_network = tables.Column("physical_network",
                                     verbose_name=_("Physical Network Name"))

    class Meta:
        name = "network_profile"
        verbose_name = _("Network Profile")
        table_actions = (CreateNetworkProfile, DeleteNetworkProfile,)
        row_actions = (EditNetworkProfile, DeleteNetworkProfile,)


class EditPolicyProfile(tables.LinkAction):
    name = "edit"
    verbose_name = _("Edit Policy Profile")
    url = "horizon:project:images_and_snapshots:images:update"
    classes = ("ajax-modal", "btn-edit")


class PolicyProfile(tables.DataTable):
    id = tables.Column("profile_id", verbose_name=_("Profile ID"), hidden=True)
    name = tables.Column("name", verbose_name=_("Policy Profile"), )
    project_id = tables.Column("project_name", verbose_name=_("Project"))

    class Meta:
        name = "policy_profile"
        verbose_name = _("Policy Profile")
