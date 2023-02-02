def canal_max(canals):
    res = max(canals.items())
    return res[0]


stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
canal = canal_max(stats)


def new_geo_logs(logs):
    ru_logs = {}
    for log in logs:
        for key, value in log.values():
            if value == 'Россия':
                ru_logs[key] = value
    logs = ru_logs.copy()
    return logs


geo_logs = [{
    'visit1': ['Москва', 'Россия']
}, {
    'visit2': ['Дели', 'Индия']
}, {
    'visit3': ['Владимир', 'Россия']
}, {
    'visit4': ['Лиссабон', 'Португалия']
}, {
    'visit5': ['Париж', 'Франция']
}, {
    'visit6': ['Лиссабон', 'Португалия']
}, {
    'visit7': ['Тула', 'Россия']
}, {
    'visit8': ['Тула', 'Россия']
}, {
    'visit9': ['Курск', 'Россия']
}, {
    'visit10': ['Архангельск', 'Россия']
}]
new_logs = new_geo_logs(geo_logs)


def unique_ids(list_id):
    list_ = list_id.values()
    newlist = []
    for i in list_:
        for j in i:
            newlist.append(j)
    return set()


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
new_ids = unique_ids(ids)
