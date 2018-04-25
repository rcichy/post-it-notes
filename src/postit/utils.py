from postit.models import Board, BoardType, Column


DEFAULT_COLUMN_TITLES = (
    u"What went well",
    u"To improve",
    u"Action items",
)


def create_default_board(user):
    """
    Creates a board with default columns.
    :param user: User object
    :return: Board object
    """
    board_type = BoardType.objects.get(pk=1)  # TODO
    board = Board.objects.create(board_type=board_type, author=user)
    for column_title in DEFAULT_COLUMN_TITLES:
        Column.objects.create(board=board, title=column_title)
    return board
