# Input/Target AST Comparison

## Step 1: Compile the `gumtree-spoon-ast-diff` executable

Simply run the following in the root:

```shell
mvn package clean
```

and `cr-change-diff.jar` will be generated.

## Step 2: Install the necessary packages

If using `pip` just run:

```shell
pip install -r requirements.txt
```

With `conda`:

```shell
conda install --file requirements.txt
```

## Step 3: Run the comparison script

Instances slated for comparison are located in the `input` directory.
After running:

```shell
python compare.py
```

You will notice a progress bar appear, which displays the number of analyzed instances, as well as the remaining execution time.
Once the script finishes, the CSV containing the original instances, along with the number of AST transformations required to transform the input code into the target code, will be found in the root directory as `ast_diff.csv`.
