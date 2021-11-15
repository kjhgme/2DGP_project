from pico2d import *
import game_world
import ball


# Boy Event
# fill here
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, DASH, DASH_UP, SPACE = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_LSHIFT) : DASH,
    (SDL_KEYDOWN, SDLK_RSHIFT) : DASH,
    (SDL_KEYUP, SDLK_LSHIFT) : DASH_UP,
    (SDL_KEYUP, SDLK_RSHIFT) : DASH_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}



# Boy States

# fill here
class IdleState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        elif event == SPACE:
            boy.fire_ball()
        boy.timer = 1000

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1 ) % 8
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)

class RunState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        elif event == SPACE:
            boy.fire_ball()
        boy.dir = boy.velocity

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)

    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)

class SleepState:
    def enter(boy, event):
        boy.frame = 0

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100,
                                          3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100,
                                          -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)

class DashState:
    def enter(boy, event):
        boy.dashtime = 150
        if event == SPACE:
            boy.fire_ball()

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        if boy.velocity == 1:
            boy.x += boy.velocity + 1
        else:
            boy.x += boy.velocity - 1
        boy.x = clamp(25, boy.x, 800 - 25)
        boy.dashtime -= 1
        if boy.dashtime == 0:
            boy.add_event(DASH_UP)

    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)

next_state_table = {
# fill here
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SLEEP_TIMER: SleepState, DASH: IdleState, DASH_UP: IdleState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState, DASH: DashState, DASH_UP: RunState, SPACE: RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState,
                 LEFT_UP: RunState, RIGHT_UP: RunState, DASH: SleepState, DASH_UP: SleepState, SPACE: IdleState},
    DashState: {LEFT_DOWN: DashState, RIGHT_DOWN: DashState, DASH: DashState, DASH_UP: RunState,
                LEFT_UP: IdleState, RIGHT_UP: IdleState, SPACE: DashState}
}



class Boy:

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        # fill here
        self.frame = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        pass


    def change_state(self,  state):
        # fill here
        pass


    def add_event(self, event):
        # fill here
        self.event_que.insert(0, event)
        pass

    def fire_ball(self):
        ball1 = ball.Ball(self.x, self.y, self.dir*3)
        game_world.add_object(ball1, 1)


    def update(self):
        # fill here
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)


    def draw(self):
        # fill here
        self.cur_state.draw(self)
        debug_print('Velocity : ' + str(self.velocity) + ' Dir : ' + str(self.dir) + 'State : ' + str(self.cur_state.__name__))
        pass

    def handle_event(self, event):
        # fill here
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass

