import simple_draw as sd

sd.set_screen_size(1200, 600)
list_snowflakes = []


def create_snow(count):

    global list_snowflakes

    for i in range(count):
        local = [sd.random_number(500, 600), sd.random_number(100, 800), sd.random_number(10, 70)]
        list_snowflakes.append(local)


def draw_snow(color):
    global list_snowflakes
    for item in list_snowflakes:
        point = sd.get_point(item[1], item[0])
        sd.snowflake(center=point, length=item[2], color=color)


def change_point(step):
    global list_snowflakes
    list_out = []
    for item in list_snowflakes:
        local = [int(item[0]) - sd.randint(-2, step), int(item[1]) + sd.randint(-2,step), item[2]]
        list_out.append(local)
    list_snowflakes = list_out


def check_snow():
    global list_snowflakes
    del_list = []
    for id, item in enumerate(list_snowflakes):
        if (item[0] - item [2]) < 0:
            del_list.append(id)
    return del_list


def delete(del_list):
    global list_snowflakes
    for item in reversed(del_list):
        # так как из-за удаления стары индексы не валидны уже
        del list_snowflakes[item]
        #TODO честно, я не совсем понимаю, что от меня требуется. Требуется после удаления из
        # list_snowflakes по индексу, затем удалить этот индекс из del_list? Разве можно изменять набор данных,
        # по которому двигается цикл?
