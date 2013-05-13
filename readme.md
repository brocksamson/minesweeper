Quick and dirty python Flask server that functions as the server side for
a browser based minesweeper game.

Server handles grid generation and hit test information.  If a 0 is returned for a cell
it is the responsibility of the calling code to make additional calls to display further
cells.

Client will handle grid rendering and whether a cell is unknown, clicked or marked.
