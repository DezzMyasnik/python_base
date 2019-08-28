import simple_draw as sd

sd.set_screen_size(1200, 600)
list = []  # TODO не используйте зарезервированные слова
def create_snow(count):

    global list

    for i in range(count):
        local = [sd.random_number(500, 600), sd.random_number(100, 800), sd.random_number(10, 70)]
        list.append(local)


def draw_snow(color):
    global list
    for item in list:
        point = sd.get_point(item[1], item[0])
        sd.snowflake(center=point, length=item[2], color=color)


def change_point(step):
    global list
    list_out = []
    for item in list:
        local = [int(item[0]) - sd.randint(2, step), int(item[1]) + sd.randint(2,step), item[2]]
        list_out.append(local)
    list = []
    list.extend(list_out)
del_list = []  # TODO это не глобальная переменная, а то что возращает check_snow, как в условии
def check_snow():
    global list, del_list
    del_list = []
    for id, item in enumerate(list):
        if (item[0] - item [2]) < 0:

            if id not in del_list:
                del_list.append(id)
                return True



def delete():  # TODO должна принимать список для удаления, как в условии
    global list, del_list
    for item in del_list:
        list.remove(list[item])
