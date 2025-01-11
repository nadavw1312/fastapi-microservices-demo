from src.external_services.rabbitmq_client import send_message

async def notify_post_service_about_user_creation(user_id: int):
    message = {"event": "user_created", "user_id": user_id}
    send_message(queue_name="posts_queue", message=message)
