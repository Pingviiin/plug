import re
import random
"""Route all the packets."""


class Packet:
    """Packet class."""

    def __init__(self, content: str, source_ip: str, destination_ip: str, id: int, sequence_number: int):
        """Initialize packet class."""
        # Write your code here
        self.content = content
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.id = id
        self.sequence_number = sequence_number

    def __repr__(self) -> str:
        """
        Represent packet.

        Format the string of the packet as:
        '[content] from [source_ip] to [destination_ip] ([id]:[sequence_number])'
        """
        # Write your code here
        return f"{self.content} from {self.source_ip} to {self.destination_ip} ({self.id}:{self.sequence_number})"


class EndDevice:
    """End device class."""

    def __init__(self):
        """
        Initialize end device.

        End device will have an IP address if they are connected to a router.
        Also, end device will collect all packets that are sent to them.
        """
        # Write your code here
        self.ip_address = ""
        self.packets = []

    def get_ip_address(self) -> str:
        """Return the current IP address of the device."""
        # Write your code here
        return self.ip_address

    def set_ip_address(self, ip_address: str) -> None:
        """
        Set an IP address for the device.

        You don't need to validate the IP address here.
        """
        # Write your code here
        self.ip_address = ip_address
        
        return self.ip_address

    def add_packet(self, packet: Packet) -> None:
        """Add a packet to end device."""
        # Write your code here
        self.packets += [packet]

    def clear_packet_history(self) -> None:
        """Clear all packets from history."""
        # Write your code here
        self.packets.clear()

    def get_all_packets(self) -> list[Packet]:
        """Get a list of all packets in the order they were added."""
        # Write your code here
        return self.packets

    def get_all_packets_by_id(self, given_id: int) -> list[Packet]:
        """Get a list of all packets that have the given ID."""
        # Write your code here
        return [packet for packet in self.packets if packet.id == given_id]

    def get_all_packets_by_source_ip(self, given_ip: str) -> list[Packet]:
        """Get a list of all packets that have given source IP."""
        # Write your code here
        return [packet for packet in self.packets if packet.source_ip == given_ip]


class Router:
    """Router class."""

    def __validate_ipv4(self, ip_address: str) -> bool:
        """Validate IPv4."""
        # Write your code here
        return bool(re.search(r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$", ip_address))

    def __init__(self, ip_address: str):
        """
        Initialize router.

        IP address must be a string in the format "x.x.x.1"
        where x is a number in the range [0, 255], such as "192.168.0.1".

        If the IP address does not match this criteria, set the IP address to "192.168.0.1".

        The first 3 sections ("192.168.0" in this example) form a subnet. You will need this later!
        """
        # Write your code here
        if self.__validate_ipv4(ip_address):
            self.ip_address = ip_address
        else:
            self.ip_address = "192.168.0.1"
            
        self.used_addresses = set()
        self.devices = []

    def get_ip_address(self) -> str:
        """Return the current IP address of the router."""
        # Write your code here
        return self.ip_address

    def generate_ip_address(self) -> str:
        """
        Generate a valid IP address.

        The IP address must be in the router's subnet.
        This means that the first 3 sections of the IP address must be the same as in the router's IP.

        The final section can be a random number in the range [2, 254].

        Make sure you can't generate an IP address that's already in use by a device!

        If there are no possible IP addresses to generate, raise an IPv4AddressSpaceExhaustedException().
        """
        # Write your code here
        subnet = self.ip_address.rsplit(".", 1)[0]
        possible_addresses = [f"{subnet}.{i}" for i in range(2, 255)]
        available_addresses = [ip for ip in possible_addresses if ip not in self.used_addresses]
        
        if available_addresses == []:
            raise IPv4AddressSpaceExhaustedException()
            
        random_address = random.choice(available_addresses)
        self.used_addresses.add(random_address)
        
        return random_address
        

    def add_device(self, device: EndDevice) -> bool:
        """
        Add end device to router.

        The same device can not be added twice.
        Each device should be assigned an unique IP address in the correct subnet.

        The method should return True if device was added, else False.
        """
        # Write your code here
        if device in self.devices:
            return False

        ip_address = self.generate_ip_address()

        if ip_address:
            device.ip_address = ip_address
            self.devices += [device]
            return True
        else:
            return False

    def remove_device(self, device: EndDevice) -> bool:
        """
        Remove an end device from the router.

        If a device is removed from the router, then the router can no longer send
        packets to the device and the device's IP address is set to an empty string.

        The method should return True if device was removed, else False.
        """
        # Write your code here
        if device in self.devices:
            self.used_addresses.discard(device.ip_address)
            device.ip_address = ""
            self.devices.remove(device)
            return True
        
        else:
            return False

    def get_devices(self) -> list[EndDevice]:
        """Get all devices that are connected to the router in the order they were connected."""
        # Write your code here
        return self.devices

    def get_device_by_ip(self, ip: str) -> EndDevice | None:
        """
        Get a device by given IP.

        If there is no device with given IP, then return None.
        Otherwise return the found device.
        """
        # Write your code here
        for device in self.devices:
            if device.ip_address == ip:
                return device
        else:
            return None

    def receive_packet(self, packet: Packet) -> None:
        """
        Receive a packet from the Internet.

        If there is a device with the destination IP in this subnet then forward this packet to this device.
        Otherwise drop this packet. (don't do anything with it)
        """
        # Write your code here
        for device in self.devices:
            if device.ip_address == packet.destination_ip:
                device.add_packet(packet)
                return


class IPv4AddressSpaceExhaustedException(Exception):
    """Raised when there are no more available IP addresses."""


if __name__ == "__main__":
    """Main for testing the functions."""
    # Initialize router
    router = Router("192.168.1.1")
    print(router.get_ip_address())  # 192.168.1.1
    print(router.get_devices())     # []
    print()

    # Initialize end devices
    device1 = EndDevice()
    device2 = EndDevice()
    print(f"{device1.get_ip_address()!a}")     # ''
    print()

    # Add devices to router
    print(router.add_device(device1))   # True
    print(router.add_device(device1))   # False (no duplicates allowed)
    print(router.add_device(device2))   # True
    print(len(router.get_devices()))    # 2
    print()

    # Check generated IP addresses
    print(device1.get_ip_address().startswith("192.168.1."))                # True (correct subnet)
    print(1 < int(device1.get_ip_address().split(".")[-1]) < 255)           # True (correct ending)
    print(device1.get_ip_address() == device2.get_ip_address())             # False (different IP addresses generated)
    print(router.get_device_by_ip(device1.get_ip_address()) == device1)     # True
    print()

    # Create packet from device1 to device2
    packet1 = Packet("message1", device1.get_ip_address(), device2.get_ip_address(), 1, 1)
    print(packet1)                          # message1 from 192.168.1.[some number] to 192.168.1.[some number](1:1)
    router.receive_packet(packet1)          # (this should send packet to device2)
    print(len(device2.get_all_packets()))   # 1
    print(len(device1.get_all_packets()))   # 0
    print(len(device2.get_all_packets_by_id(1)))    # 1
    print(len(device2.get_all_packets_by_source_ip(device1.get_ip_address())))  # 1
    print()

    # Create packet from device1 to unknown destination
    packet2 = Packet("message2", device1.get_ip_address(), "10.0.255.44", 2, 1)
    router.receive_packet(packet2)          # (this should drop the packet)
    print(len(device1.get_all_packets()))   # 0
    print(len(device2.get_all_packets()))   # 1
    print()

    # Remove end device from router
    print(router.remove_device(device1))    # True
    print(router.remove_device(device1))    # False (already removed)
    print(f"{device1.get_ip_address()!a}")  # ''
    print(len(router.get_devices()))        # 1
