time = int(input("Сколько минут готовится одна сторона? "))
summary = int(input("Сколько котлет вмещается на сковородку? "))
count = int(input("Сколько всего котлет нужно пожарить? "))

time = 2 * time

if count % summary == 0:
    a = count // summary
    time = time * a
    print("Время приготовления составит", time, "минут")
elif count % summary != 0:
    a = count // summary + 1
    time = time * a
    print("Время приготовления составит", time, "минут")