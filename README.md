# README

## things to add before handing out keys
1. have a key database so i can keep track of who is who
    - generate like 100 keys and store them
    - add users to them after 

2. give hanton control over creating discord testing environments


## Run Tests
```bash
python3 test.py
```
Currently tests the operability of most classes within the Sudoku package

## Run Main
Currently inoperable until Config is fixed
```bash
python3 main.py
```

## Discord Command Schema
```markdown
# Discord Command Format
$s command1 command2 commandn

# API path schema
/command1/command2/commandn
```

## Directory Structure

#### sudoku 
├── **classes**\
│   ├── *config*\
│   │   └── SudokuConfig.py\
│   ├── *game*\
│   │   ├── Board.py\
│   ├── *labels*\
│   │   └── LabelEncoder.py\
│   ├── *load*\
│   │   ├── PuzzleLoader.py\
│   │   ├── SudokuDataset.py\
│   │   ├── SudokuLoader.py\
│   │   └── SudokuNoisedDataset.py\
│   ├── *nn*\
│   │   ├── ConvNN.py\
│   │   ├── Evaluator.py\
│   │   ├── NeuralNetwork.py\
│   │   └── Trainer.py\
│   └── *solver*\
│       ├── MlSolver.py\
│       └── Solver.py\
├── **database**\
│   ├── database.py\
│   ├── *db_funcs*\
│   │   ├── queries.py\
│   │   └── update.py\
│   ├── models.py\
├── **helper**\
│   ├── api_helper.py\
│   ├── helper.py\
│   ├── pandas_helper.py\
└── **pydantic** \
    ├── api_schemas.py\
    ├── db_schemas.py\
    ├── forms\
    │   ├── examples.py\
    └── sudoku_schemas.py

21 directories, 57 files
