users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
unique_visits = set(users)

visit_statistics = {
    "Общее количество": len(users),
    "Уникальные посещения": len(unique_visits)
}

print(visit_statistics)
