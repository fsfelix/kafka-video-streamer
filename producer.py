import time
import cv2
from kafka import SimpleProducer, KafkaClient

kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)
topic = 'video-stream'

def video_producer(video):
    video = cv2.VideoCapture(video)
    print "starting"
    # video.set(cv2.CAP_PROP_FRAME_WIDTH, 20)
    # video.set(cv2.CAP_PROP_FRAME_HEIGHT, 10)

    while (video.isOpened):
        success, image = video.read()

        if not success:
            break

        ret, jpeg = cv2.imencode('.png', image)
        print jpeg.size
        producer.send_messages(topic, jpeg.tobytes())


    video.release()
    print "done"

if __name__ == '__main__':
    video_producer('sample.mp4')
