import time
import cv2
from kafka import SimpleProducer, KafkaClient

kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)
topic = 'video-stream'

def video_producer(video):
    video = cv2.VideoCapture(video)
    print "starting"

    while (video.isOpened):
        success, image = video.read()

        if not sucess:
            break

        ret, jpeg = cv2.imencode('.png', image)
        producer.send_messages(topic, jpeg.tobytes())

        time.sleep(0.2)

    video.release()
    print "done"

if __name__ == '__main__':
    video_producer('sample.mp4')
