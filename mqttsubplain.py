from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import time
import random
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "/python/Johnsonmqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    aes_key=b'I am working on 727 report, haha'
    #print(type(aes_key),len(aes_key))
    # Create an AES cipher object with the generated key using AES-256 mode
    cipher = AES.new(aes_key, AES.MODE_ECB)

    def on_message(client, userdata, msg):
        #recmess=bytes.fromhex(msg.payload.decode())
        #decrypted_plaintext = unpad(cipher.decrypt(recmess), AES.block_size).decode()
        print("Decrypted Plaintext:", msg.payload.decode())
        #print(f"Received `{type(msg.payload.decode())}` from `{msg.topic}` topic")
        """

        time.sleep(1)
        """
    #client.subscribe(topic)
    client.subscribe(topic,qos=2)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()

