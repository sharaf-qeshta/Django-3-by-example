
def order_created(order_id):
    """Task to send an e-mail notification when an order is
 successfully created.
 """
    from .models import Order
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    from django.core.mail import send_mail
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    print(mail_sent)  # printing the message on console
    return mail_sent
