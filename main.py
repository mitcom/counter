from latex import create_pdf_file, create_tex_file


def main():
    moves = [
                (0, 0, 1),
                (0, 1, 2),
                (0, 2, 3),
                (0, 3, 6),
                (0, 4, 0),
                (0, 5, 4),
                (0, 6, 5),

                (1, 0, 4),
                (1, 1, 0),
                (1, 2, 1),
                (1, 3, 2),
                (1, 4, 5),
                (1, 5, 6),
                (1, 6, 3),
            ], 'd', 2

    moves = [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 5),
                (5, 6),
                (6, 7),
                (7, 8),
                (8, 9),
                (9, 10),
                (10, 11),
                (11, 12),
                (12, 13),
                (13, 14),
                (14, 15),
                (15, 16),
                (16, 17),
                (17, 18),
                (18, 19),
                (19, 0),

            ], 'jk', 2
    # moves = [(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 9), (7, 10),
    #          (8, 11), (9, 12), (10, 13), (11, 14), (12, 15), (13, 0), (14, 1), (15, 2), ], 'd', 2

    file = 'file.tex'
    create_tex_file(*moves, file)
    print('tex_file')
    create_pdf_file(file)
    print('pdf_file')


if __name__ == '__main__':
    main()
