# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011, Nicira Networks, Inc.
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
# @author: Somik Behera, Nicira Networks, Inc.
# @author: Salvatore Orlando, Citrix

import logging

from quantum.common import exceptions as exc
from quantum.db import api as db

LOG = logging.getLogger('quantum.plugins.SamplePlugin')

class QuantumEchoPlugin(object):

    """
    QuantumEchoPlugin is a demo plugin that doesn't
    do anything but demonstrated the concept of a
    concrete Quantum Plugin. Any call to this plugin
    will result in just a "print" to std. out with
    the name of the method that was called.
    """

    def get_all_networks(self, tenant_id):
        """
        Returns a dictionary containing all
        <network_uuid, network_name> for
        the specified tenant.
        """
        print("get_all_networks() called\n")

    def create_network(self, tenant_id, net_name):
        """
        Creates a new Virtual Network, and assigns it
        a symbolic name.
        """
        print("create_network() called\n")

    def delete_network(self, tenant_id, net_id):
        """
        Deletes the network with the specified network identifier
        belonging to the specified tenant.
        """
        print("delete_network() called\n")

    def get_network_details(self, tenant_id, net_id):
        """
        Deletes the Virtual Network belonging to a the
        spec
        """
        print("get_network_details() called\n")

    def rename_network(self, tenant_id, net_id, new_name):
        """
        Updates the symbolic name belonging to a particular
        Virtual Network.
        """
        print("rename_network() called\n")

    def get_all_ports(self, tenant_id, net_id):
        """
        Retrieves all port identifiers belonging to the
        specified Virtual Network.
        """
        print("get_all_ports() called\n")

    def create_port(self, tenant_id, net_id):
        """
        Creates a port on the specified Virtual Network.
        """
        print("create_port() called\n")

    def delete_port(self, tenant_id, net_id, port_id):
        """
        Deletes a port on a specified Virtual Network,
        if the port contains a remote interface attachment,
        the remote interface is first un-plugged and then the port
        is deleted.
        """
        print("delete_port() called\n")

    def update_port(self, tenant_id, net_id, port_id, port_state):
        """
        Updates the state of a port on the specified Virtual Network.
        """
        print("update_port() called\n")

    def get_port_details(self, tenant_id, net_id, port_id):
        """
        This method allows the user to retrieve a remote interface
        that is attached to this particular port.
        """
        print("get_port_details() called\n")

    def plug_interface(self, tenant_id, net_id, port_id, remote_interface_id):
        """
        Attaches a remote interface to the specified port on the
        specified Virtual Network.
        """
        print("plug_interface() called\n")

    def unplug_interface(self, tenant_id, net_id, port_id):
        """
        Detaches a remote interface from the specified port on the
        specified Virtual Network.
        """
        print("unplug_interface() called\n")


class DummyDataPlugin(object):

    """
    DummyDataPlugin is a demo plugin that provides
    hard-coded data structures to aid in quantum
    client/cli development
    """

    def get_all_networks(self, tenant_id):
        """
        Returns a dictionary containing all
        <network_uuid, network_name> for
        the specified tenant.
        """
        nets = {"001": "lNet1", "002": "lNet2", "003": "lNet3"}
        print("get_all_networks() called\n")
        return nets

    def create_network(self, tenant_id, net_name):
        """
        Creates a new Virtual Network, and assigns it
        a symbolic name.
        """
        print("create_network() called\n")
        # return network_id of the created network
        return 101

    def delete_network(self, tenant_id, net_id):
        """
        Deletes the network with the specified network identifier
        belonging to the specified tenant.
        """
        print("delete_network() called\n")

    def get_network_details(self, tenant_id, net_id):
        """
        retrieved a list of all the remote vifs that
        are attached to the network
        """
        print("get_network_details() called\n")
        vifs_on_net = ["/tenant1/networks/net_id/portid/vif2.0"]
        return vifs_on_net

    def rename_network(self, tenant_id, net_id, new_name):
        """
        Updates the symbolic name belonging to a particular
        Virtual Network.
        """
        print("rename_network() called\n")

    def get_all_ports(self, tenant_id, net_id):
        """
        Retrieves all port identifiers belonging to the
        specified Virtual Network.
        """
        print("get_all_ports() called\n")
        port_ids_on_net = ["2", "3", "4"]
        return port_ids_on_net

    def create_port(self, tenant_id, net_id):
        """
        Creates a port on the specified Virtual Network.
        """
        print("create_port() called\n")
        #return the port id
        return 201

    def update_port(self, tenant_id, net_id, port_id, port_state):
        """
        Updates the state of a port on the specified Virtual Network.
        """
        print("update_port() called\n")

    def delete_port(self, tenant_id, net_id, port_id):
        """
        Deletes a port on a specified Virtual Network,
        if the port contains a remote interface attachment,
        the remote interface is first un-plugged and then the port
        is deleted.
        """
        print("delete_port() called\n")

    def get_port_details(self, tenant_id, net_id, port_id):
        """
        This method allows the user to retrieve a remote interface
        that is attached to this particular port.
        """
        print("get_port_details() called\n")
        #returns the remote interface UUID
        return "/tenant1/networks/net_id/portid/vif2.1"

    def plug_interface(self, tenant_id, net_id, port_id, remote_interface_id):
        """
        Attaches a remote interface to the specified port on the
        specified Virtual Network.
        """
        print("plug_interface() called\n")

    def unplug_interface(self, tenant_id, net_id, port_id):
        """
        Detaches a remote interface from the specified port on the
        specified Virtual Network.
        """
        print("unplug_interface() called\n")


class FakePlugin(object):
    """
    FakePlugin is a demo plugin that provides
    in-memory data structures to aid in quantum
    client/cli/api development
    """

    def __init__(self):
        db_options = {"sql_connection": "sqlite:///fake_plugin.sqllite"}
        db.configure_db(db_options)        
        FakePlugin._net_counter = 0

    def _get_network(self, tenant_id, network_id):
        network = db.network_get(network_id)
        if not network:
            raise exc.NetworkNotFound(net_id=network_id)
        return network

    def _get_port(self, tenant_id, network_id, port_id):
        net = self._get_network(tenant_id, network_id)
        port = db.port_get(port_id)
        # Port must exist and belong to the appropriate network.
        if not port or port['network_id']!=net['uuid']:
            raise exc.PortNotFound(net_id=network_id, port_id=port_id)
        return port

    def _validate_port_state(self, port_state):
        if port_state.upper() not in ('ACTIVE', 'DOWN'):
            raise exc.StateInvalid(port_state=port_state)
        return True

    def _validate_attachment(self, tenant_id, network_id, port_id,
                             remote_interface_id):
        for port in db.port_list(network_id):
            if port['interface_id'] == remote_interface_id:
                raise exc.AlreadyAttached(net_id=network_id,
                                          port_id=port_id,
                                          att_id=port['interface_id'],
                                          att_port_id=port['uuid'])

    def get_all_networks(self, tenant_id):
        """
        Returns a dictionary containing all
        <network_uuid, network_name> for
        the specified tenant.
        """
        LOG.debug("FakePlugin.get_all_networks() called")
        nets = []
        for net in db.network_list(tenant_id):
            net_item = {'net-id':str(net.uuid), 
                        'net-name':net.name}
            nets.append(net_item)
        return nets        

    def get_network_details(self, tenant_id, net_id):
        """
        retrieved a list of all the remote vifs that
        are attached to the network
        """
        LOG.debug("FakePlugin.get_network_details() called")
        return self._get_network(tenant_id, net_id)

    def create_network(self, tenant_id, net_name):
        """
        Creates a new Virtual Network, and assigns it
        a symbolic name.
        """
        LOG.debug("FakePlugin.create_network() called")
        new_net = db.network_create(tenant_id, net_name)
        # Return uuid for newly created network as net-id.
        return {'net-id': new_net['uuid']}

    def delete_network(self, tenant_id, net_id):
        """
        Deletes the network with the specified network identifier
        belonging to the specified tenant.
        """
        LOG.debug("FakePlugin.delete_network() called")
        net = self._get_network(tenant_id, net_id)
        # Verify that no attachments are plugged into the network
        if net:
            if net['net-ports']:
                for port in db.port_list(net_id):
                    if port['interface-id']:
                        raise exc.NetworkInUse(net_id=net_id)
            db.network_destroy(net_id)
            return net
        # Network not found
        raise exc.NetworkNotFound(net_id=net_id)

    def rename_network(self, tenant_id, net_id, new_name):
        """
        Updates the symbolic name belonging to a particular
        Virtual Network.
        """
        LOG.debug("FakePlugin.rename_network() called")
        db.network_rename(net_id, tenant_id, new_name)
        net = self._get_network(tenant_id, net_id)
        return net

    def get_all_ports(self, tenant_id, net_id):
        """
        Retrieves all port identifiers belonging to the
        specified Virtual Network.
        """
        LOG.debug("FakePlugin.get_all_ports() called")
        port_ids = []
        ports = db.port_list(net_id)
        for x in ports:
            d = {'port-id':str(x.uuid)}
            port_ids.append(d)
        return port_ids

    def get_port_details(self, tenant_id, net_id, port_id):
        """
        This method allows the user to retrieve a remote interface
        that is attached to this particular port.
        """
        LOG.debug("FakePlugin.get_port_details() called")
        return self._get_port(tenant_id, net_id, port_id)

    def create_port(self, tenant_id, net_id, port_state=None):
        """
        Creates a port on the specified Virtual Network.
        """
        LOG.debug("FakePlugin.create_port() called")
        port = db.port_create(net_id)
        port_item = {'port-id':str(port.uuid)}
        return port_item

    def update_port(self, tenant_id, net_id, port_id, new_state):
        """
        Updates the state of a port on the specified Virtual Network.
        """
        port=self._get_port(tenant_id, net_id, port_id)
        LOG.debug("FakePlugin.update_port() called")
        self._validate_port_state(port_state)
        db.port_set_state(new_state)
        return 

    def delete_port(self, tenant_id, net_id, port_id):
        """
        Deletes a port on a specified Virtual Network,
        if the port contains a remote interface attachment,
        the remote interface is first un-plugged and then the port
        is deleted.
        """
        LOG.debug("FakePlugin.delete_port() called")
        net = self._get_network(tenant_id, net_id)
        port = self._get_port(tenant_id, net_id, port_id)
        if port['attachment']:
            raise exc.PortInUse(net_id=net_id, port_id=port_id,
                                att_id=port['attachment'])
        try:
            port = db.port_destroy(port_id)
        except Exception, e:
            raise Exception("Failed to delete port: %s" % str(e))
        d = {}
        d["port-id"] = str(port.uuid)
        return d

    def plug_interface(self, tenant_id, net_id, port_id, remote_interface_id):
        """
        Attaches a remote interface to the specified port on the
        specified Virtual Network.
        """
        LOG.debug("FakePlugin.plug_interface() called")
        # Validate attachment
        self._validate_attachment(tenant_id, net_id, port_id,
                                  remote_interface_id)
        port = self._get_port(tenant_id, net_id, port_id)
        if port['attachment']:
            raise exc.PortInUse(net_id=net_id, port_id=port_id,
                                att_id=port['attachment'])
        db.port_set_attachment(port_id, remote_interface_id)

    def unplug_interface(self, tenant_id, net_id, port_id):
        """
        Detaches a remote interface from the specified port on the
        specified Virtual Network.
        """
        LOG.debug("FakePlugin.unplug_interface() called")
        # TODO(salvatore-orlando):
        # Should unplug on port without attachment raise an Error?
        db.port_set_attachment(port_id, None)
