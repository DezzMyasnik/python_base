# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...



import room_1
import room_2 as secondroom

print("В комнате " + room_1.__name__ + " живут: " + " и ".join(room_1.folks))
print("В комнате " + secondroom.__name__ + " живут: " + " и ".join(secondroom.folks))

#зачет!