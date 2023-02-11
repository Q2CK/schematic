import mcschematic


def rearrange(lines: list[str]):
    output: list[str] = []

    for element in lines:

        line = element.strip()
        temp = ""

        line_left = line[0:8]
        line_right = line[8:16]

        for i in range(0, 8):
            temp += line_left[i] + line_right[i]

        output.append(temp[::-1])

    return output


def main():
    schem = mcschematic.MCSchematic()

    bin_file = rearrange(open("bin.txt", "r").readlines())

    for line in bin_file:
        print(line)

    for line_nr, line in enumerate(bin_file[0:8]):

        for bit, char in enumerate(line):
            if char == "0":
                schem.setBlock((bit + 2 + (2 * line_nr), bit - (2 * line_nr), 2), "minecraft:white_stained_glass")
            elif char == "1":
                schem.setBlock((bit + 2 + (2 * line_nr), bit - (2 * line_nr), 2), "minecraft:repeater[facing=north]")

    for line_nr, line in enumerate(bin_file[8:15]):

        for bit, char in enumerate(line):
            if char == "0":
                schem.setBlock((bit + 3 + (2 * line_nr), bit - (2 * line_nr) - 1, 2), "minecraft:white_stained_glass")
            elif char == "1":
                schem.setBlock((bit + 3 + (2 * line_nr), bit - (2 * line_nr) - 1, 2), "minecraft:repeater[facing=north]")

    for line_nr, line in enumerate(bin_file[16:24]):

        for bit, char in enumerate(line):
            if char == "0":
                schem.setBlock((bit + 2 + (2 * line_nr), bit - (2 * line_nr), 5), "minecraft:white_stained_glass")
            elif char == "1":
                schem.setBlock((bit + 2 + (2 * line_nr), bit - (2 * line_nr), 5), "minecraft:repeater[facing=south]")

    for line_nr, line in enumerate(bin_file[24:31]):

        for bit, char in enumerate(line):
            if char == "0":
                schem.setBlock((bit + 3 + (2 * line_nr), bit - (2 * line_nr) - 1, 5), "minecraft:white_stained_glass")
            elif char == "1":
                schem.setBlock((bit + 3 + (2 * line_nr), bit - (2 * line_nr) - 1, 5), "minecraft:repeater[facing=south]")

    for line_nr, line in enumerate(bin_file[32:40]):
        pass

    for line_nr, line in enumerate(bin_file[40:47]):
        pass

    for line_nr, line in enumerate(bin_file[48:56]):
        pass

    for line_nr, line in enumerate(bin_file[56:63]):
        pass

    schem.save("C:/Users/Oem/PycharmProjects/schematic", "ms", mcschematic.Version.JE_1_16_5)


if __name__ == "__main__":
    main()
