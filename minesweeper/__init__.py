import random
from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)


@app.route('/<int:row>/<int:col>', methods=['GET'])
def find_mines(row, col):
    filename = '{0}.grid'.format(request.remote_addr)
    try:
        with open(filename) as f:
            #json f*cks up the key, makes it a string...
            grid = {int(key): value for key, value in json.loads(f.read()).iteritems()}
    except IOError:
        grid = generate_grid()
        with open(filename, 'w') as f:
            f.write(json.dumps(grid))
    return jsonify({"cell": find_mines(grid, row, col)})


@app.route('/', methods=['DEL'])
def delete_game():
    try:
        os.remove('{0}.grid'.format(request.remote_addr))
    except OSError:
        pass


def generate_grid(height=15, width=30, mines=99):
    random.seed()
    grid = {}
    i = 0
    while i < mines:
        row = random.randrange(0, height)
        col = random.randrange(0, width)
        if not row in grid.keys():
            grid[row] = []
        if not col in grid[row]:
            grid[row].append(col)
            i = i + 1
    for row, cols in grid.iteritems():
        cols.sort()
    return grid


def find_mines(grid, row, col):
    is_mine = lambda grid, row, col: row in grid.keys() and col in grid[row]
    if(is_mine(grid, row, col)):
        return True
    targets = {row-1: [col-1, col, col+1],
               row:   [col-1, col, col+1],
               row+1: [col-1, col, col+1]}
    count = 0
    for row, cols in targets.iteritems():
        for col in cols:
            if(is_mine(grid, row, col)):
                count = count + 1
    return count
