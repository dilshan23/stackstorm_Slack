import socket
from st2reactor.sensor.base import Sensor


class MySensor(Sensor):
    def __init__(self, sensor_service, config):
        super(MySensor, self).__init__(sensor_service=sensor_service, config=config)
        self._stop = False

    def setup(self):
        pass

    def run(self):
        while not self._stop:
            try:
                # Create a socket and bind it to the desired port
                server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_socket.bind(('0.0.0.0', 8181))
                server_socket.listen(1)
                self.sensor_service.set_value('port_status', 'listening')
                self.sensor_service.dispatch(trigger='my_sensor.event', payload={'message': 'Event received'})

                # Accept connections and process events
                while True:
                    client_socket, _ = server_socket.accept()
                    # Process the event from the client_socket
                    # Your event processing logic here
            except KeyboardInterrupt:
                self._stop = True
            finally:
                server_socket.close()

    def cleanup(self):
        pass


sensor = MySensor()
sensor.run()
