

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
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():

  def on_connect(client, userdata, flags, rc):
    if rc == 0:
      print("Connected to MQTT Broker!")
    else:
      print("Failed to connect, return code %d\n", rc)

  client = mqtt_client.Client(client_id)
  client.on_connect = on_connect
  client.connect(broker, port)
  return client


def publish(client):

  # Generate a random AES key
  #aes_key = get_random_bytes(32)
  aes_key = b'I am working on 727 report, haha'
  #print(type(aes_key), len(aes_key))
  # Create an AES cipher object with the generated key using AES-256 mode
  cipher = AES.new(aes_key, AES.MODE_ECB)
  #print("start time:", time.time())
  i=1
  totaltime=0.0
  with open('nns.log') as file:
    for line in file:
      plaintext = str(i)+" "+line.rsplit("-", 1)[1]
      i+=1
      if i==1002:
         plaintext=str(totaltime)
      elif i==1003:
         break
      #print(plaintext)
#      input()
      sttime=time.time()
      ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
      #ciphertext=plaintext
      """
        print("origin:",type(ciphertext),len(ciphertext))
        input()
        tempci=ciphertext.hex()
        print("dest:",type(tempci),len(tempci))
        input()
        deco=bytes.fromhex(tempci)
        print("third:",type(deco),len(deco))
        input()
        print("equal:",ciphertext==deco)
        input()
        time.sleep(10)
        """
      result = client.publish(topic, ciphertext.hex(), qos=2)
      entime=time.time()
      totaltime=totaltime+(entime-sttime)
      # result: [0, 1]
      status = result[0]
      if status == 0:
        print(f"Send `{ciphertext.hex()}` to topic `{topic}` time conumption  '{totaltime}'")
      else:
        print(f"Failed to send message to topic {topic}")

      #print("AES Key (hexadecimal format):", aes_key.hex())
      #print("Ciphertext (hexadecimal format):", ciphertext.hex())
      #decrypted_plaintext = unpad(cipher.decrypt(ciphertext),
       #                           AES.block_size).decode()
      #print("Decrypted Plaintext:", decrypted_plaintext)
      time.sleep(1)


def run():
  client = connect_mqtt()
  client.loop_start()
  publish(client)


if __name__ == '__main__':
  run()
