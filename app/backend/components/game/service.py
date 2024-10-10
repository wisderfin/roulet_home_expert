import random

async def get_present():
    items = [
    {'name': 'item1', 'level': '1', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item2', 'level': '3', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item3', 'level': '2', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item4', 'level': '1', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item5', 'level': '2', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item6', 'level': '3', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item7', 'level': '1', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item8', 'level': '1', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item9', 'level': '2', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item10', 'level': '3', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item11', 'level': '1', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item12', 'level': '2', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item13', 'level': '3', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item14', 'level': '1', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item15', 'level': '2', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item16', 'level': '1', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item17', 'level': '3', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item18', 'level': '2', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item19', 'level': '1', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item20', 'level': '2', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item21', 'level': '3', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item22', 'level': '1', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item23', 'level': '2', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item24', 'level': '1', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item25', 'level': '3', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item26', 'level': '2', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item27', 'level': '1', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item28', 'level': '3', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item29', 'level': '2', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'},
    {'name': 'item30', 'level': '1', 'img': 'https://avatars.mds.yandex.net/i?id=326c8b41e835b671fdc79d0c40e4f44a0389d2ff-10131513-images-thumbs&n=13'}
]
    weights = []

    for item in items:
        level = item['level']
        if level == '1':
            weights.append(80)
        elif level == '2':
            weights.append(15)
        elif level == '3':
            weights.append(5)
        else:
            raise ValueError("Уровень должен быть от 1 до 3")

    # Выбор элемента с учетом весов
    res = []
    for i in range(21):
        res.append(random.choices(items, weights=weights, k=1)[0])
    return res[:-2] + [random.choices(items, weights=weights, k=1)[0]] + [res[-1]]
