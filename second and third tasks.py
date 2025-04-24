class Device:
    def __init__(self, topic):
        self.topic = topic
        self.status = 'off'
        self.device_name = topic.split('/')[-1]
        self.device_type = topic.split('/')[-2]

    def turn_on(self):
        self.status = 'on'
        print(f'{self.device_name} turned ON')

    def turn_off(self):
        self.status = 'off'
        print(f'{self.device_name} turned OFF')


class Sensor:
    def __init__(self, sensor_type, name, group_name):
        self.name = name
        self.sensor_type = sensor_type
        self.group_name = group_name

    def read(self):
        return f"{self.name} reading: 25°C"


class Admin_panel:

    def __init__(self):
        self.groups = {}
        self.sensors = []

    def create_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f'Group {group_name} created')
        else:
            print('Your group name already exists')

    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
        else:
            print(f'Group {group_name} does not exist')

    def create_device(self, group_name, device_type, name):
        if group_name in self.groups:
            topic = f'home/{group_name}/{device_type}/{name}'
            new_device = Device(topic)
            self.add_device_to_group(group_name, new_device)
            print(f'Device {name} added to {group_name}')
        else:
            print(f'Group {group_name} does not exist')

    def create_multiple_devices(self, group_name, device_type, number_of_devices):
        if group_name in self.groups:
            for i in range(1, number_of_devices + 1):
                device_name = f'{device_type}{i}'
                topic = f'home/{group_name}/{device_type}/{device_name}'
                new_device = Device(topic)
                self.add_device_to_group(group_name, new_device)
                print(f'Device {device_name} added to {group_name}')

    def turn_on_all_in_group(self, group_name):
        if group_name in self.groups:
            for device in self.groups[group_name]:
                device.turn_on()

    def turn_off_all_in_group(self, group_name):
        if group_name in self.groups:
            for device in self.groups[group_name]:
                device.turn_off()

    def turn_on_all(self):
        for group_name in self.groups:
            self.turn_on_all_in_group(group_name)

    def turn_off_all(self):
        for group_name in self.groups:
            self.turn_off_all_in_group(group_name)

    def get_status_in_group(self, group_name):
        if group_name in self.groups:
            print(f'Status in {group_name}:')
            for device in self.groups[group_name]:
                print(f'{device.device_name}: {device.status}')

    def get_status_in_device_type(self, device_type):
        print(f'Status of all {device_type}s:')
        for devices in self.groups.values():
            for device in devices:
                if device.device_type == device_type:
                    print(f'{device.device_name} in {device.topic.split("/")[1]}: {device.status}')

    def create_sensor(self, sensor_type, name, group_name):
        if group_name in self.groups:
            sensor = Sensor(sensor_type, name, group_name)
            self.sensors.append(sensor)
            print(f'Sensor {name} added to {group_name}')
        else:
            print(f'Group {group_name} does not exist')

    def get_status_sensor_in_group(self, group_name):
        print(f'Sensors in {group_name}:')
        for sensor in self.sensors:
            if sensor.group_name == group_name:
                print(sensor.read())
if __name__ == "__main__":
    panel = Admin_panel()

    panel.create_group("kitchen")
    panel.create_device("kitchen", "light", "light1")
    panel.create_multiple_devices("kitchen", "fan", 2)
    
    panel.turn_on_all_in_group("kitchen")
    panel.get_status_in_group("kitchen")

    panel.create_sensor("temperature", "sensor1", "kitchen")
    panel.get_status_sensor_in_group("kitchen")
