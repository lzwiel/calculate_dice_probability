import random

def calculate_dice_probability():
    result = {}
    total_trials = 1000000  # 总试验次数

    for _ in range(total_trials):
        dice1 = random.randint(1, 6)  # 第一个筛子朝上的数字
        dice2 = random.randint(1, 6)  # 第二个筛子朝上的数字
        combination = (dice1, dice2)

        if combination in result:
            result[combination] += 1
        else:
            result[combination] = 1

    # 计算概率
    probabilities = {}
    for combination, count in result.items():
        probability = count / total_trials
        probabilities[combination] = probability

    return probabilities

probabilities = calculate_dice_probability()

# 打印结果
for combination, probability in probabilities.items():
    print(f"组合 {combination} 的概率为: {probability:.4f}")
