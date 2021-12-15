from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import chess
import chess.engine

engines = {
    'stockfish': chess.engine.SimpleEngine.popen_uci(
        "engines/stockfish_13/stockfish"
    ),
    'komodo': chess.engine.SimpleEngine.popen_uci(
        "engines/komodo_12/komodo"
    ),
}


@api_view(['POST'])
def engineResponse(request):
    if 'fen' in request.data:
        board = chess.Board(request.data['fen'])

        if 'engine_name' in request.data:
            result = engines[request.data['engine_name']].play(
                board,
                chess.engine.Limit(time=0.1),
            )
            response = {
                str(result.move):
                board.san(chess.Move.from_uci(str(result.move)))
            }

            return Response(
                {
                    "success": True,
                    "engine_move": response,
                },
                status=status.HTTP_200_OK
            )

        else:
            return Response(
                {
                    "error": True,
                    "message": "'engine_name' key not found!"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    else:
        return Response(
            {
                "error": True,
                "message": "'fen' key not found!"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
