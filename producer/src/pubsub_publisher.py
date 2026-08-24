from google.cloud import pubsub_v1


class PubSubPublisher:
    def __init__(self, project_id: str, topic_id: str):
        self.topic_path = (
            pubsub_v1.PublisherClient.topic_path(
                project_id,
                topic_id,
            )
        )

        self.publisher = pubsub_v1.PublisherClient()

    def publish(self, message: bytes) -> str:
        future = self.publisher.publish(
            self.topic_path,
            message,
        )

        return future.result()