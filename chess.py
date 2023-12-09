# chess pieces - unicode characters
# https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode
chess_pieces = '♔♕♖♗♘♙♚♛♜♝♞♟'

# chess pieces - shortcuts 
# https://www.chess.com/terms/chess-notation#whatiscn
# plus P, p for pawns
# white pieces - uppercase letters, black - lowercase
chess_shortcuts = "KQRBNPkqrbnp" 

# starting position
# https://www.chess.com/terms/chess-pieces
chessboard = [
["r", "n", "b", "q", "k", "b", "n", "r"],
["p", "p", "p", "p", "p", "p", "p", "p"], 
[" ", " ", " ", " ", " ", " ", " ", " "],  
[" ", " ", " ", " ", " ", " ", " ", " "],  
[" ", " ", " ", " ", " ", " ", " ", " "],  
[" ", " ", " ", " ", " ", " ", " ", " "],  
["P", "P", "P", "P", "P", "P", "P", "P"], 
["R", "N", "B", "Q", "K", "B", "N", "R"],
]

"""
Name	Symbol	Code point	HTML (decimal)	HTML (hex)
white chess king	♔	U+2654	&#9812;	&#x2654;
white chess queen	♕	U+2655	&#9813;	&#x2655;
white chess rook	♖	U+2656	&#9814;	&#x2656;
white chess bishop	♗	U+2657	&#9815;	&#x2657;
white chess knight	♘	U+2658	&#9816;	&#x2658;
white chess pawn	♙	U+2659	&#9817;	&#x2659;
black chess king	♚	U+265A	&#9818;	&#x265A;
black chess queen	♛	U+265B	&#9819;	&#x265B;
black chess rook	♜	U+265C	&#9820;	&#x265C;
black chess bishop	♝	U+265D	&#9821;	&#x265D;
black chess knight	♞	U+265E	&#9822;	&#x265E;
black chess pawn	♟︎	U+265F	&#9823;	&#x265F;
"""

pieces_table = [
["short", "name",         "symbol",     "code_point",   "html_dec",     "html_hex"], 
["K",     "white king",   "♔",         "U+2654",       "&#9812;",      "&#x2654;"],  
["Q",     "white queen",  "♕",         "U+2655",       "&#9813;",      "&#x2655;"],  
["R",     "white rook",   "♖",         "U+2656",       "&#9814;",      "&#x2656;"],  
["B",     "white bishop", "♗",         "U+2657",       "&#9815;",      "&#x2657;"],  
["N",     "white knight", "♘",         "U+2658",       "&#9816;",      "&#x2658;"],  
["P",     "white pawn",   "♙",         "U+2659",       "&#9817;",      "&#x2659;"],  
["k",     "black king",   "♚",         "U+265A",       "&#9818;",      "&#x265A;"],  
["q",     "black queen",  "♛",         "U+265B",       "&#9819;",      "&#x265B;"],  
["r",     "black rook",   "♜",         "U+265C",       "&#9820;",      "&#x265C;"],  
["b",     "black bishop", "♝",         "U+265D",       "&#9821;",      "&#x265D;"],  
["n",     "black knight", "♞",         "U+265E",       "&#9822;",      "&#x265E;"],  
["p",     "black pawn",   "♟",         "U+265F",       "&#9823;",      "&#x265F;"],  
]

pieces = {row[0]: {pieces_table[0][i]: value for i, value in enumerate(row)} 
    for row in pieces_table[1:]}

"""
[['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
 ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
 ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']]
"""
chessboard_sym = [[ch if ch not in pieces else pieces[ch]["symbol"] 
    for ch in row] for row in chessboard]

row_coordinates = [8, 7, 6, 5, 4, 3, 2, 1]                   # 8 - row_index
col_coordinates = ["a", "b", "c", "d", "e", "f", "g", "h"]   # chr(ord("a" + col_index)
"""
[['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
 ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
 ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
 ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
 ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
 ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
 ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
 ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']]
"""
coords = [[chr(ord("a")+col_index) + str(8 - row_index) 
    for col_index in range(8)] for row_index in range(8)]

"""
[['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'],
 ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'],
 ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'],
 ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'],
 ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'],
 ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'],
 ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'],
 ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w']]
"""
chessboard_colors = [
    ["b" if (irow + icol) % 2 else "w"
    for icol in range(8)] for irow in range(8)]



