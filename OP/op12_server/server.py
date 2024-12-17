"""Serve all the packets."""

from router import Packet, EndDevice, Router
import re
import pytest


class EndDevicePlus(EndDevice):
    """
    End Device Plus class.

    This class extends the EndDevice class from EX12.
    """

    def __init__(self):
        """Initialize End Device Plus."""
        # Write your code here
        super().__init__()

    def get_message(self, id: int) -> str:
        """
        Get message from packets by ID.

        Message is a string formed by the contents of all received packets with the specified ID.

        Make sure you pay attention to the correct order of the packets using their sequence number.
        If the device has not received any packets with this ID, return an empty string.
        There must be no extra symbols between the contents of two packets.

        If some packets have been lost (such as there being packets 1 and 3, but not packet 2),
        then add an underscore (_) in place of each missing packet.
        """
        # Write your code here
        packets = self.get_all_packets_by_id(id)

        if not packets:
            return ""

        packets = sorted(packets, key=lambda packet: packet.sequence_number)

        message = []
        sequence = 1
        for packet in packets:
            while sequence < packet.sequence_number:
                message.append("_")
                sequence += 1
            message.append(packet.content)
            sequence += 1

        return "".join(message)


class RouterPlus(Router):
    """
    Router Plus class.

    This class extends the Router class from EX12.
    """

    def __init__(self, ip_address: str):
        """Initialize Router Plus."""
        # Write your code here
        super().__init__(ip_address)

    def receive_packet(self, packet: Packet) -> None:
        """
        Receive a Packet from the Internet with additional fuctionality.

        If packet's destination IP ends with .255 then the packet has to be sent to every known device on the router.
        In any other case packet should be handled like it was was handled in Router. (use super())

        Remember to check that the subnet of the packet matches the subnet of the router before sending it out.
        """
        # Write your code here
        router_subnet = self.ip_address.rsplit(".", 1)[0]
        packet_subnet = packet.destination_ip.rsplit(".", 1)[0]

        if router_subnet != packet_subnet:
            return

        if packet.destination_ip.endswith(".255"):
            for device in self.devices:
                device.add_packet(packet)

        else:
            super().receive_packet(packet)

    def restart_router(self) -> None:
        """
        Restart the router.

        Upon restarting the router all of the devices get new IP addresses.
        None of the devices can have the same IP that they had before the restart.

        Make sure the order of devices does not change when RouterPlus restarts.
        New IP-s for the devices can not go out of the allowed IP range [2-254].
        """
        # Write your code here
        self.used_addresses.clear()

        for device in self.devices:
            old_ip = device.get_ip_address()
            new_ip = self.generate_ip_address()

            while new_ip == old_ip:
                new_ip = self.generate_ip_address()

            device.set_ip_address(new_ip)


class Server:
    """Server class."""

    def __validate_ipv4(self, ip_address: str) -> bool:
        """Validate IPv4."""
        # Write your code here
        return bool(re.search(r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$", ip_address))

    def __init__(self):
        """Initialize server."""
        # Write your code here
        self.ip_address = ""
        self.routers = []

    def split_message(self, message: str) -> list[str]:
        """
        Split message into smaller pieces.

        Because the maximum content length for a packet is 5 symbols,
        then we have to split up bigger messages in order to send them over the network.

        The messages have to be split into maximum length pieces and put into a list in the correct order.
        The list of message pieces has to be returned.

        If the message is exactly 5 symbols or less then just return the message in a list.
        Example:
            "Hello World" -> ["Hello", " Worl", "d"]
        """
        # Write your code here
        if message == "":
            return [""]
        return [message[i:i+5] for i in range(0, len(message), 5)]

    def set_ip_address(self, ip_address: str) -> None:
        """
        Set an IP address for the Server.

        Make sure to validate the IP address here.
        A Server's IP cannot end with 0 (network identifier), 1 (router) or 255 (broadcast).
        If given IP is not a valid IP, do not modify the current IP address.
        """
        # Write your code here
        if self.__validate_ipv4(ip_address) and not ip_address.endswith((".0", ".1", ".255")):
            self.ip_address = ip_address

    def get_ip_address(self) -> str:
        """Return the current IP address of the server."""
        # Write your code here
        return self.ip_address

    def add_router(self, router: Router) -> bool:
        """
        Add router to the server.

        Same router can not be added to the server multiple times.

        The method should return True if a router was added to the server, else False.
        """
        # Write your code here
        if router not in self.routers:
            self.routers.append(router)
            return True
        return False

    def remove_router(self, router: Router) -> bool:
        """
        Remove a router from the server.

        If a router is removed from the router, then the server can no longer send
        packets to the router.

        The method should return True if a router was removed from the server, else False.
        """
        # Write your code here
        if router in self.routers:
            self.routers.remove(router)
            return True
        return False

    def get_routers(self) -> list[Router]:
        """Get all routers that are connected to the server in the order they were connected."""
        # Write your code here
        return self.routers

    def send_packet_to_ip(self, packet: Packet) -> None:
        """
        Send a Packet to a device with the Packet's destination IP address.

        You'll first need to check your connected routers to see if any of them have
        the same subnet as the target IP address.

        If there are no suitable routers or the IP address is invalid, drop the packet (do not send it).
        Also, packet should be dropped if packet's content size is over the limit (5 symbols).

        If you find a router with the same subnet as the target IP, you can use that router's
        receive_packet() method to handle the rest of the delivery.
        """
        # Write your code here
        if len(packet.content) > 5:
            return

        dest_subnet = packet.destination_ip.rsplit(".", 1)[0]
        for router in self.get_routers():
            if router.get_ip_address().startswith(dest_subnet):
                router.receive_packet(packet)
                return

    def send_message_to_ip(self, message: str, ip_address: str, id: int) -> None:
        """
        Send message to given IP addess.

        You have to create new Packets to be sent yourself.
        Remember that a Packet's content can not be longer than 5 symbols.

        Given ID is used to differentiate messages.
        This ID has to be used in the packets.

        You should use send_packet_to_ip() method here.
        """
        # Write your code here
        parts = self.split_message(message)
        for i, part in enumerate(parts, start=1):
            packet = Packet(part, self.get_ip_address(), ip_address, id, i)
            self.send_packet_to_ip(packet)

    def send_message_to_all(self, message: str, id: int) -> None:
        """
        Send message to every known router and to every end device on these routers.

        You should use send_message_to_ip() method here.
        Sending to every end device should be handled by the router.
        """
        # Write your code here
        parts = self.split_message(message)
        for router in self.get_routers():
            broadcast_ip = router.get_ip_address().rsplit('.', 1)[0] + '.255'
            for sequence, part in enumerate(parts, start=1):
                packet = Packet(part, self.get_ip_address(), broadcast_ip, id, sequence)
                self.send_packet_to_ip(packet)


if __name__ == "__main__":
    """Main for testing the functions."""
    # Initialize RouterPlus
    router = RouterPlus("192.168.1.1")
    print(router.get_ip_address())  # 192.168.1.1
    print(router.get_devices())     # []
    print()

    # Initialize end devices
    device1 = EndDevicePlus()
    device2 = EndDevicePlus()
    print(f"{device1.get_ip_address()!a}")     # ''
    print()

    # Add devices to router
    print(router.add_device(device1))   # True
    print(router.add_device(device1))   # False (no duplicates allowed)
    print(router.add_device(device2))   # True
    print(len(router.get_devices()))    # 2
    print()

    # Check generated IP addresses
    print(device1.get_ip_address().startswith("192.168.1.")
          )                # True (correct subnet)
    # True (correct ending)
    print(1 < int(device1.get_ip_address().split(".")[-1]) < 255)
    # False (different IP addresses generated)
    print(device1.get_ip_address() == device2.get_ip_address())
    print(router.get_device_by_ip(device1.get_ip_address()) == device1)     # True
    print()

    # Get message
    router.receive_packet(
        Packet("Te", "192.168.1.1", device1.get_ip_address(), 2, 1))
    router.receive_packet(
        Packet("re!", "192.168.1.1", device1.get_ip_address(), 2, 3))
    print(device1.get_message(2))           # Te_re!
    print(len(device1.get_all_packets()))   # 2
    print(len(device2.get_all_packets()))   # 0
    print()

    # Packet with a destination IP that ends with .255 is sent to all connected devices
    packet_broadcast = Packet("test", "192.168.1.1", "192.168.1.255", 1, 1)
    router.receive_packet(packet_broadcast)
    print(len(device1.get_all_packets()))   # 3
    print(len(device2.get_all_packets()))   # 1
    print()

    # Restarting router gives every device a new IP
    old_ip_device1 = device1.get_ip_address()
    old_ip_device2 = device2.get_ip_address()
    router.restart_router()
    print(device1.get_ip_address() == old_ip_device1)   # False
    print(device2.get_ip_address() == old_ip_device2)   # False
    print()

    # Initialize Server
    server = Server()
    print(f"{server.get_ip_address()!a}")       # ''
    server.set_ip_address("1.2.3.4")
    print(f"{server.get_ip_address()!a}")       # '1.2.3.4'
    print(server.add_router(router))            # True
    print(len(server.get_routers()))            # 1
    print()

    # Server send packet
    packet_server = Packet("test", "1.2.3.4", device2.get_ip_address(), 3, 1)
    server.send_packet_to_ip(packet_server)
    print(len(device1.get_all_packets()))       # 3
    print(len(device2.get_all_packets()))       # 2
    print()

    # Server send message
    server.send_message_to_ip("pretty long message",
                              device2.get_ip_address(), 4)
    print(f"{device2.get_message(4)!a}")        # 'pretty long message'
    print(f"{device1.get_message(4)!a}")        # ''
    print()

    # Server send message to all
    router2 = RouterPlus("10.0.0.1")
    device3 = EndDevicePlus()
    device4 = EndDevicePlus()
    router2.add_device(device3)
    router2.add_device(device4)
    server.add_router(router2)
    server.send_message_to_all("All your files have been encrypted!", 1337)
    print(device1.get_message(1337))    # All your files have been encrypted!
    print(device4.get_message(1337))    # All your files have been encrypted!
    print()

def test_server_send_message_to_all_creates_packets_with_correct_values():
    server = Server()
    router1 = RouterPlus("192.168.0.1")
    router2 = RouterPlus("1.1.1.1")
    router3 = RouterPlus("192.168.1.1")
    device11 = EndDevicePlus()
    device12 = EndDevicePlus()
    device21 = EndDevicePlus()
    device22 = EndDevicePlus()
    device31 = EndDevicePlus()
    device32 = EndDevicePlus()

    server.set_ip_address("172.32.16.254")

    router1.add_device(device11)
    router1.add_device(device12)

    router2.add_device(device21)
    router2.add_device(device22)

    router3.add_device(device31)
    router3.add_device(device32)

    server.add_router(router1)
    server.add_router(router2)
    server.add_router(router3)

    message = "test"

    server.send_message_to_all(message, 100)

    total_packets = device11.get_all_packets() + device12.get_all_packets() + device21.get_all_packets() \
                    + device22.get_all_packets() + device31.get_all_packets() + device32.get_all_packets()

    if len(total_packets) != 6:
        pytest.fail("Server did not send out correct amount of packets!\n" +
                    f"expected: 6\nactual: {len(total_packets)}")

    starts_with = "test from 172.32.16.254 to "
    ends_with = ".255 (100:1)"
    for packet in total_packets:
        if not (packet.__repr__().startswith(starts_with) and packet.__repr__().endswith(ends_with)):
            pytest.fail("Packets were not correctly created.")

test_server_send_message_to_all_creates_packets_with_correct_values()