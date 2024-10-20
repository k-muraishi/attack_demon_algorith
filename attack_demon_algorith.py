import sys

def main():
    lines = get_stdin()

    demon_hp = int(lines[0])
    attack_point = int(lines[1])
    recovery_point = int(lines[2])

    # 回復の方が多い場合倒せないので終了
    if demon_hp > attack_point and attack_point <= recovery_point:
        print("NO")
        sys.exit(0)

    # 攻撃した段階でhpが0以下なら終了
    turn_count = 0
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

# 魔王を攻撃
def attack_demon(demon_hp, attack_point):
    return demon_hp - attack_point

# 魔王を回復させる
def recovery_demon(demon_hp, recovery_point):
    return demon_hp + recovery_point

if __name__ == "__main__":
    main()
