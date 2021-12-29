from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import chess.engine
import chess

engines = {
    'stockfish': chess.engine.SimpleEngine.popen_uci(
        'engines/stockfish_13/stockfish'
    ),
    'komodo': chess.engine.SimpleEngine.popen_uci(
        'engines/komodo_12/komodo'
    ),
}


@api_view(['POST'])
def engineResponse(request):
    try:
        board = chess.Board(str(request.data['fen']))
        engine_name = str(request.data['engine_name'])
        result = engines[engine_name].play(
            board,
            chess.engine.Limit(time=0.1),
        )

        return Response(
            {
                'success': True,
                'engine_move': {
                    str(result.move):
                    board.san(chess.Move.from_uci(str(result.move)))
                },
            },
            status=status.HTTP_200_OK
        )

    except KeyError as ke:
        response = {'error': True}

        if 'fen' in str(ke) or 'engine_name' in str(ke):
            response['message'] = f"key {ke} is missing!"
        elif engine_name in str(ke):
            response['message'] = "chess engine name error!"
            response['description'] = f"no chess engine exists with the name: {ke}"
        else:
            response['message'] = str(ke)

        return Response(
            response,
            status=status.HTTP_400_BAD_REQUEST,
        )

    except ValueError as ve:
        return Response(
            {
                'error': True,
                'message': "fen is syntactically invalid!",
                'description': str(ve)
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
