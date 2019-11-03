from copy import deepcopy


def check_cycle(initial_point, parent_dfs=None):
    pass
    # point = initial_point

    # point.visited = 'explored'
    # for neighbor in point.neighbors:
    #     if neighbor.visited == 'unvisited':
    #         parent = point
    #         check_cycle(neighbor, parent)
    #     elif neighbor.visited == 'explored':
    #         if parent_dfs != None and neighbor.index == parent_dfs.index:
    #             print('two ways undirected edge: %s-%s' %
    #                   (neighbor.index, point.index))
    #         else:
    #             print('cycle: %s-%s' % (neighbor.index, point.index))
    # point.visited = 'visited'
