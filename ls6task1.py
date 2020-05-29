# _author_ = Nikita_Savchenko


from time import sleep


class TrafficLights:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        i = 0
        while i < 3:
            color_next = TrafficLights.__color[i - 2]
            print(f'Traffic light color is: {TrafficLights.__color[i]}')
            if i == 0 and color_next == 'Yellow':
                sleep(2)
            elif i == 1 and color_next == 'Green':
                sleep(2)
            elif i == 2 and color_next == 'Red':
                sleep(2)
                i = -1
            else:
                print(f'Traffic light error! Next color is: {color_next}, and now it is {TrafficLights.__color[i]}')
                break
            i += 1


TrafficLight = TrafficLights()
TrafficLight.running()