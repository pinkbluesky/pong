import math

def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):

    # add new ball position
    pong_ai.ball_pos.append(ball_frect)
    if len(pong_ai.ball_pos) > 5:
        # pop off oldest ball position
        pong_ai.ball_pos.pop(0)

    # calculate the direction vector of ball
    dir_vector = (pong_ai.ball_pos[len(pong_ai.ball_pos) - 1].pos[0] - pong_ai.ball_pos[0].pos[0],
                  pong_ai.ball_pos[len(pong_ai.ball_pos) - 1].pos[1] - pong_ai.ball_pos[0].pos[1])

    prediction_vector = (ball_frect.pos[0], ball_frect.pos[1])

    # check that direction vector is not (0, 0)
    if dir_vector[0] != 0:

        # count limits the number of iterations - w/o count, it takes way too long
        count = 0
        # while prediction vector x-value doesn't exceed table
        while table_size[0] > prediction_vector[0] >= 0 and count < 50:
            count += 1
            # add direction vector
            prediction_vector = add_tuple(prediction_vector, dir_vector)

            # if adding dir_vector to ball position exceeds table...
            if table_size[1] > prediction_vector[1] <= 0:
                # undo the addition
                prediction_vector = add_tuple(prediction_vector, (-dir_vector[0], -dir_vector[1]))

                # add the reflected direction vector
                dir_vector = (dir_vector[0], -dir_vector[1])
                prediction_vector = add_tuple(prediction_vector, dir_vector)

    projected_y = prediction_vector[1]

    # check if it's an attack
    x1 = ball_frect.pos[0] - paddle_frect.pos[0]
    x2 = pong_ai.ball_pos[0].pos[0] - ball_frect.pos[0]
    # uses abs to check if the signs are same
    is_ball_attack = True if \
        (abs(x1 + x2) == abs(x1) + abs(x2)) \
        else False

    # adjust for projection
    if is_ball_attack:
        if paddle_frect.pos[1] + paddle_frect.size[1] / 2 > projected_y:
            return "up"
        else:
            return "down"
    # go to the middle of the table
    else:
        if paddle_frect.pos[1] + paddle_frect.size[1] / 2 > table_size[1] / 2:
            return "up"
        else:
            return "down"

# function that adds two tuples together because + doesn't work
def add_tuple(t1, t2):
    return tuple(map(lambda i, j: i + j, t1, t2))

# array to store the past 5 ball positions
pong_ai.ball_pos = []
