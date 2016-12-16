from latex import create_pdf_file, create_tex_file


def main():
    moves = [
                (0, 0, 3),
                (0, 1, 4),
                (0, 2, 5),
                (0, 3, 6),
                (0, 4, 7),
                (0, 5, 8),
                (0, 6, 9),
                (0, 7, 10),
                (0, 8, 11),
                (0, 9, 12),
                (0, 10, 13),
                (0, 11, 14),
                (0, 12, 15),
                (0, 13, 16),
                (0, 14, 17),
                (0, 15, 18),
                (0, 16, 19),
                (0, 17, 20),
                (0, 18, 21),
                (0, 19, 22),
                (0, 20, 23),
                (0, 21, 24),
                (0, 22, 25),
                (0, 23, 26),
                (0, 24, 27),
                (0, 25, 28),
                (0, 26, 29),
                (0, 27, 30),
                (0, 28, 31),
                (0, 29, 0),
                (0, 30, 1),
                (0, 31, 2),

                (1, 0, 31),
                (1, 1, 0),
                (1, 2, 1),
                (1, 3, 2),
                (1, 4, 3),
                (1, 5, 4),
                (1, 6, 5),
                (1, 7, 6),
                (1, 8, 7),
                (1, 9, 8),
                (1, 10, 9),
                (1, 11, 10),
                (1, 12, 11),
                (1, 13, 12),
                (1, 14, 13),
                (1, 15, 14),
                (1, 16, 15),
                (1, 17, 16),
                (1, 18, 17),
                (1, 19, 18),
                (1, 20, 19),
                (1, 21, 20),
                (1, 22, 21),
                (1, 23, 22),
                (1, 24, 23),
                (1, 25, 24),
                (1, 26, 25),
                (1, 27, 26),
                (1, 28, 27),
                (1, 29, 28),
                (1, 30, 29),
                (1, 31, 30),
            ], 'jk'

    file = 'file.tex'
    create_tex_file(*moves, file)
    print('tex_file')
    create_pdf_file(file)
    print('pdf_file')


if __name__ == '__main__':
    main()
