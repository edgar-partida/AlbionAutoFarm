from src.util.Constants import *
from src.model.Dimension import Dimension


class Screen:
    active_image = ""
    is_mouse_pressed = False
    click_coordinates = (0, 0)
    game_screen_coordinates = {Dimension(0, 0, 0, 0)}

    def __init__(self, mss, cv2, numpy, sleep, time):
        self.mss = mss
        self.cv2 = cv2
        self.numpy = numpy
        self.sleep = sleep
        self.time = time

    def get_full_screen_capture(self):
        with self.mss.mss() as sct:
            mon = sct.monitors[MONITOR_NUMBER]
            img = self.numpy.array(sct.grab(mon))
            return img

    def show_dependant_image(self, image):
        self.active_image = image
        cv2 = self.cv2
        cv2.namedWindow(TITLE)
        cv2.setMouseCallback(TITLE, self.screen_select_event_listener)

        cv2.imshow(TITLE, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def screen_select_event_listener(self, event, x, y, flags, params):
        cv2 = self.cv2

        if event == cv2.EVENT_LBUTTONDOWN:
            self.is_mouse_pressed = True
            self.click_coordinates = (x, y)
            print((x,y))
        elif event == cv2.EVENT_MOUSEMOVE and self.is_mouse_pressed:
            img_copy = self.active_image.copy()
            cv2.rectangle(img_copy, self.click_coordinates, (x, y), (0, 0, 255), 2)
            cv2.imshow(TITLE, img_copy)
        elif event == cv2.EVENT_LBUTTONUP:
            self.is_mouse_pressed = False
            print(x,y)
            game_dimensions = Dimension(top=self.click_coordinates[1]+31,
                                        left=self.click_coordinates[0]+7,
                                        width=x-self.click_coordinates[0],
                                        height=y-self.click_coordinates[1])
            cv2.destroyAllWindows()
            print("Game coordinates:")
            print(game_dimensions.to_json())
            self.game_screen_coordinates = game_dimensions.to_json()

    def get_game_screen_coordinates(self):
        return self.game_screen_coordinates
    def set_game_screen_coordinates(self,t,l,w,h):
        self.game_screen_coordinates = Dimension(t,l,w,h).to_json()

    def take_game_screenshot(self):
        with self.mss.mss() as sct:
            return self.numpy.array(sct.grab(self.game_screen_coordinates))

    def show_image(self,image):
        cv2 = self.cv2
        cv2.imshow(TITLE, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

