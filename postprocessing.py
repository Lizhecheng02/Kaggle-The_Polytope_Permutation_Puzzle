num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def save_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(data)


def solution_to_move(dimension, solution_string):
    move = []

    parts = solution_string.split(" ")
    print("The length of abbreviate solution is:", len(parts))

    for i in range(len(parts)):
        if len(parts[i]) == 1:
            if parts[i] == 'U':
                move.append(f"-d{dimension-1}")
            elif parts[i] == 'D':
                move.append(f"d0")
            elif parts[i] == 'L':
                move.append(f"-r{dimension-1}")
            elif parts[i] == 'R':
                move.append(f"r0")
            elif parts[i] == 'F':
                move.append(f"f0")
            elif parts[i] == 'B':
                move.append(f"-f{dimension-1}")
            else:
                print("Error1" + parts[i])
        elif len(parts[i]) == 2:
            if parts[i][1] == "'":
                if parts[i][0] == 'U':
                    move.append(f"d{dimension-1}")
                elif parts[i][0] == 'D':
                    move.append(f"-d0")
                elif parts[i][0] == 'L':
                    move.append(f"r{dimension-1}")
                elif parts[i][0] == 'R':
                    move.append(f"-r0")
                elif parts[i][0] == 'F':
                    move.append(f"-f0")
                elif parts[i][0] == 'B':
                    move.append(f"f{dimension-1}")
                else:
                    print("Error2" + parts[i])
            elif parts[i][1].isdigit():
                time = int(parts[i][1])
                if parts[i][0] == 'U':
                    for j in range(time):
                        move.append(f"-d{dimension-1}")
                elif parts[i][0] == 'D':
                    for j in range(time):
                        move.append(f"d0")
                elif parts[i][0] == 'L':
                    for j in range(time):
                        move.append(f"-r{dimension-1}")
                elif parts[i][0] == 'R':
                    for j in range(time):
                        move.append(f"r0")
                elif parts[i][0] == 'F':
                    for j in range(time):
                        move.append(f"f0")
                elif parts[i][0] == 'B':
                    for j in range(time):
                        move.append(f"-f{dimension-1}")
                else:
                    print("Error3" + parts[i])
            elif parts[i][1] == "w":
                num = 2
                if parts[i][0] == 'U':
                    for j in range(num):
                        move.append(f"-d{dimension-1-j}")
                elif parts[i][0] == 'D':
                    for j in range(num):
                        move.append(f"d{j}")
                elif parts[i][0] == 'L':
                    for j in range(num):
                        move.append(f"-r{dimension-1-j}")
                elif parts[i][0] == 'R':
                    for j in range(num):
                        move.append(f"r{j}")
                elif parts[i][0] == 'F':
                    for j in range(num):
                        move.append(f"f{j}")
                elif parts[i][0] == 'B':
                    for j in range(num):
                        move.append(f"-f{dimension-1-j}")
                else:
                    print("Error4" + parts[i])
            else:
                print("Error5" + parts[i])
        elif len(parts[i]) == 3:
            if parts[i][0].isdigit() and parts[i][2] == 'w':
                num = int(parts[i][0])
                if parts[i][1] == 'U':
                    for j in range(num):
                        move.append(f"-d{dimension-1-j}")
                elif parts[i][1] == 'D':
                    for j in range(num):
                        move.append(f"d{j}")
                elif parts[i][1] == 'L':
                    for j in range(num):
                        move.append(f"-r{dimension-1-j}")
                elif parts[i][1] == 'R':
                    for j in range(num):
                        move.append(f"r{j}")
                elif parts[i][1] == 'F':
                    for j in range(num):
                        move.append(f"f{j}")
                elif parts[i][1] == 'B':
                    for j in range(num):
                        move.append(f"-f{dimension-1-j}")
                else:
                    print("Error6" + parts[i])
            elif parts[i][2] == "'" and parts[i][1] == "w":
                num = 2
                if parts[i][0] == 'U':
                    for j in range(num):
                        move.append(f"d{dimension-1-j}")
                elif parts[i][0] == 'D':
                    for j in range(num):
                        move.append(f"-d{j}")
                elif parts[i][0] == 'L':
                    for j in range(num):
                        move.append(f"r{dimension-1-j}")
                elif parts[i][0] == 'R':
                    for j in range(num):
                        move.append(f"-r{j}")
                elif parts[i][0] == 'F':
                    for j in range(num):
                        move.append(f"-f{j}")
                elif parts[i][0] == 'B':
                    for j in range(num):
                        move.append(f"f{dimension-1-j}")
                else:
                    print("Error7" + parts[i])
            elif parts[i][2].isdigit() and parts[i][1] == "w":
                num = 2
                time = int(parts[i][2])
                if parts[i][0] == 'U':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"-d{dimension-1-k}")
                elif parts[i][0] == 'D':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"d{k}")
                elif parts[i][0] == 'L':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"-r{dimension-1-k}")
                elif parts[i][0] == 'R':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"r{k}")
                elif parts[i][0] == 'F':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"f{k}")
                elif parts[i][0] == 'B':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"-f{dimension-1-k}")
                else:
                    print("Error8" + parts[i])
            else:
                print("Error9" + parts[i])
        elif len(parts[i]) == 4:
            if parts[i][0].isdigit() and parts[i][3].isdigit():
                num = int(parts[i][0])
                time = int(parts[i][3])
                if parts[i][1] == 'U':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"-d{dimension-1-k}")
                elif parts[i][1] == 'D':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"d{k}")
                elif parts[i][1] == 'L':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"-r{dimension-1-k}")
                elif parts[i][1] == 'R':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"r{k}")
                elif parts[i][1] == 'F':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"f{k}")
                elif parts[i][1] == 'B':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"-f{dimension-1-k}")
                else:
                    print("ERROR10" + parts[i])
            elif parts[i][0].isdigit() and parts[i][3] == "'":
                num = int(parts[i][0])
                time = 1
                if parts[i][1] == 'U':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"d{dimension-1-k}")
                elif parts[i][1] == 'D':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"-d{k}")
                elif parts[i][1] == 'L':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"r{dimension-1-k}")
                elif parts[i][1] == 'R':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"-r{k}")
                elif parts[i][1] == 'F':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"-f{k}")
                elif parts[i][1] == 'B':
                    for k in range(num):
                        for j in range(time):
                            move.append(f"f{dimension-1-k}")
                else:
                    print("ERROR11" + parts[i])
            else:
                print("ERROR12" + parts[i])

    output = ','.join(move)
    save_to_file(output, 'output.txt')

    return output, len(move)


if __name__ == '__main__':
    origin_string = "D' L2 Bw2 Rw' D Fw' D' Rw2 U Bw2 D B L Dw2 Rw' L2 U' F D2 Dw2 Rw2 F' L2 D' Bw2 Lw2 D2 F2 R2 D' Lw2 U L D B2 L' D L B' D2 F' R2 B2 D R2 U2 R2 D2 B2 L2 D'"
    output, length = solution_to_move(4, origin_string)
    print(output)
    print(length)
