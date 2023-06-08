"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem
from pprint import pprint


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


# Задание 1
users_messages_counter = {}


def count_user_messages(message):
    if users_messages_counter.get(message['sent_by']):
        users_messages_counter[message['sent_by']] += 1
    else:
        users_messages_counter[message['sent_by']] = 1


def get_max_posts_id(messages_dict):
    max_messages_user_index = max(
        messages_dict, key=users_messages_counter.get)
    return max_messages_user_index


# Задание 2
user_by_message = {}  # для 2 задания
user_replied_amount = {}  # для 2 задания


def count_replies(message):
    user_by_message[message['id']] = message['sent_by']
    if message.get('reply_for'):
        quoted_user_id = user_by_message[message['reply_for']]
        user_replied_amount[quoted_user_id] = user_replied_amount.get(
            quoted_user_id, 0) + 1
    return user_replied_amount


def get_most_replied_user(replied_users_dict):
    return max(replied_users_dict, key=replied_users_dict.get)


# Задание 3
users_seen_by = {}  # для 3 задания


def count_message_views(message):
    users_seen_by.setdefault(message['sent_by'], 0)
    users_seen_by[message['sent_by']] += len(message.get('seen_by'))
    return users_seen_by


def count_max_views(seen_by_dict):
    return max(seen_by_dict, key=seen_by_dict.get)


# Задание 4
messages_by_time = {
    'morning': 0,
    'afternoon': 0,
    'evening': 0
}


def count_messages_by_time_periods(message):
    if message['sent_at'].hour < 12:
        messages_by_time['morning'] += 1
    elif message['sent_at'].hour < 18:
        messages_by_time['afternoon'] += 1
    else:
        messages_by_time['evening'] += 1


def get_most_messaged_time_period(time_periods_counter):
    return max(messages_by_time, key=messages_by_time.get)


# Задание 5
most_replied_messages = {}


def count_replied_messages(message):
    most_replied_messages[message['id']] = []
    if message.get('reply_for'):
        most_replied_messages[message['reply_for']].append(
            message['id'])
        for answers in most_replied_messages.values():
            if message.get('reply_for') in answers:
                answers.append(message['id'])
    return most_replied_messages


def get_max_replied_messages(replied_messages, amount=5):
    sorted_messages = sorted(
        replied_messages.items(), key=lambda item: len(item[1]), reverse=True)
    sorted_messages = sorted_messages[:(amount)]
    sorted_messages = [message[0] for message in sorted_messages]
    return [f'Number {index} by replied messages: {message}' for index, message in enumerate(sorted_messages, start=1)]


if __name__ == "__main__":
    for index, message in enumerate(generate_chat_history()):
        count_user_messages(message)  # Задание 1
        count_replies(message)  # Задание 2
        count_message_views(message)  # Задание 3
        count_messages_by_time_periods(message)  # Задание 4
        count_replied_messages(message)  # Задание 5

    print('Max posts id: ', get_max_posts_id(
        users_messages_counter))  # Задание 1
    print('Most replied id: ', get_most_replied_user(
        user_replied_amount))  # Задание 2
    print('Most viewed user: ', count_max_views(
        users_seen_by))  # Задание 3
    print('Most messages are in the: ', get_most_messaged_time_period(
        messages_by_time))  # Задание 4
    pprint(get_max_replied_messages(
        most_replied_messages, 3))  # Задание 5
