import sys

def main():
    lines = get_stdin()

    attack_point = int(lines[1])
    recovery_point = int(lines[2])

    if attack_point <= recovery_point:
        print("NO")
        sys.exit(0)

    turn_count = 0
    demon_hp = int(lines[0])

    while demon_hp > 0:
        demon_hp = attack_demon(demon_hp, attack_point)
        turn_count += 1
        if demon_hp <= 0:
            break
        demon_hp = recovery_demon(demon_hp, recovery_point)

    print("YES")
    print(turn_count)
    sys.exit(0)

def get_stdin():
    input_values = input().split()
    return input_values

def attack_demon(demon_hp, attack_point):
    return demon_hp - attack_point

def recovery_demon(demon_hp, recovery_point):
    return demon_hp + recovery_point

if __name__ == "__main__":
    main()
