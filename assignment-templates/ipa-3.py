'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    from_user_follows = social_graph[from_member]["following"]
    to_user_follows = social_graph[to_member]["following"]

    if from_member not in to_user_follows and to_member not in from_user_follows:
        relationship = "no relationship"
    elif from_member in to_user_follows and to_member not in from_user_follows:
        relationship = "followed by"
    elif from_member not in to_user_follows and to_member in from_user_follows:
        relationship = "follower"
    elif from_member in to_user_follows and to_member in from_user_follows:
        relationship = "friends"

    return relationship



def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    h_win = 0
    v_win = 0
    d_win = 0

    winner = ""

    #horizontal check
    for rows in board:
        for characters in rows:
            if rows.count(rows[0]) == len(board):
                h_win = 1
                return rows[0]
            else:
                h_win = 0
    
    #diagonal check
    d_list1 = []
    d_list2 = []
    i = 0 
    j = 1
    for rows in board:
        d_list1.append(rows[i])
        i = i + 1

    for rows in board:
        d_list2.append(rows[len(board) - j])
        j = j + 1

    if d_list1.count(d_list1[0]) == len(board):
        d_win = 1
        return d_list1[0]
    
    if d_list2.count(d_list2[0]) == len(board):
        d_win = 1
        return d_list2[0]

    #vertical check
    v_list = []
    for k in range (0, len(board)):
        for rows in board:
            v_list.append(rows[k])
            if len(v_list) == len(board):
                if v_list.count(v_list[0]) == len(board):
                    v_win = 1
                    return(v_list[0])
                else:
                    v_list = []
        k = k + 1

    #no winner
    if v_win == h_win == d_win == 0:
       winner = "NO WINNER"
       return winner 

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    list_legs = list(route_map.keys())

    n = 0
    travel_time = 0
    key_index = 0 

    for keys in list_legs:
        if first_stop not in keys[0]:
            key_index = key_index + 1
        if first_stop in keys[0]:
            key_index = key_index + 1
            break

    for keys in list_legs[key_index - 1:]:

        if first_stop in keys[0] and second_stop in keys[1]:
            travel_time = route_map[keys]["travel_time_mins"]
            return travel_time  
        
        elif first_stop in keys[0] and second_stop not in keys[1]:
            travel_time = travel_time + route_map[keys]["travel_time_mins"]
            n = n + 1

        elif first_stop not in keys[0] and second_stop not in keys[1]:
            travel_time = travel_time + route_map[keys]["travel_time_mins"]
            n = n + 1

        elif first_stop not in keys[0] and second_stop in keys[1]:
            travel_time = travel_time + route_map[keys]["travel_time_mins"]
            return travel_time
        
    for keys in list_legs:

        if first_stop in keys[0] and second_stop in keys[1]:
            travel_time = route_map[keys]["travel_time_mins"]
            return travel_time  
        
        elif first_stop in keys[0] and second_stop not in keys[1]:
            travel_time = travel_time + route_map[keys]["travel_time_mins"]
            n = n + 1

        elif first_stop not in keys[0] and second_stop not in keys[1]:
            travel_time = travel_time + route_map[keys]["travel_time_mins"]
            n = n + 1

        elif first_stop not in keys[0] and second_stop in keys[1]:
            travel_time = travel_time + route_map[keys]["travel_time_mins"]
            return travel_time



