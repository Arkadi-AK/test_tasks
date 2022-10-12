def check_relation(net, first, second):
    names = {}
    visit = set()
    for i in net:
        names.setdefault(i[0], set())
        names[i[0]].add(i[1])
        names.setdefault(i[1], set())
        names[i[1]].add(i[0])

    # DFS
    def dfs(visited, graph, node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(visited, graph, neighbor)
        return True if first in visited else False

    return dfs(visit, names, second)


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
