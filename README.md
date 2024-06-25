# Sudoku To Do



## Hyperparameter Optimzation

### Needs
1. ~~Start Training~~
    - ~~Fix Data Reading~~
    
### Notes
- The paper we are working off of uses 15 conv layers
- Maybe watch some videos

#### Hyperparemeter Optimization Psuedocode
```
This is a placeholder
```

#### Proposed Fixes
This is a placeholder
#### Potential Issues
This is a placeholder

------------------ 

## Data Efficiency
Might be more efficient to load from disk directly.

### Needs
    1. Start Training
        - Fix Data Reading
    
### Notes
Not really important

#### Testing Pseudocode
```python
batch_sizes = [1,2,3,4,5]
for i in range(batch_sizes):
    %%timeit
    run("model with disk loading", batch_size)

for i in range(batch_sizes):
    %%timeit
    run("model with all data loaded", bath_size)
```
#### Proposed Fixes
1. Method of directly loading from disk
2. Method for testing the speed of both 
    - Really just seeing which can complete N epochs faster over a span of M batch_sizes


#### Potential Issues
lol theres a few

------------------

# To Do Format!
Below is the format you should follow when adding to this document.

## Problem or Feature

### Needs
1. Numerical List of things
2. Things on this document that require finishing prior to this feature being fixed/implemented
3. Somethings may have multiple dependencies that are required before starting
    - If something in this list requires things itself you should put them below like so!

### Notes
This can really by anything so long as it has at least some text. Could be a wishlist or rough thoughts that 

#### Original or Blank Code Block
```python
print('You should put the code/psuedocode') 
print('in a box here like this!')
```
#### Proposed Fixes
1. I like numerical lists but this will likely be replaced by checkboxes 

#### Potential Issues
1. Numerical lists are the go to for here.
2. After this don't forget the page/line break thing below!
3. This also doesn't have to explicitly be issues, it could be something like a potential workaround you don't have fully worked out yet! <mark>(this might require an alternative section)<mark/>
---

# Completed! 
Finished sections should go here!

## Fix Data Reading

### Dependent On
1. None

### Notes
Notes for fixing data reading
#### SudokuDataset 

##### Original SudokuDataset
```py

class SudokuDataset(Dataset):
    def __init__(self, data) -> None:

        self.data = data
        self.labels = labels
        super().__init__()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        data = self.data[index, :81].astype('float32')

        return data
```
##### Proposed Fixes
1. Add labels as an extra input
2. Change **\_\_getitem\_\_** indexing to take all columns instead of just 81
3. Labels indexing should just be the same as the data

##### Potential Later Issues
1. Deciding to have one hot encoded labels may require some datatype finagling such that it works with categorical crossentropy

##### New SudokuDataset
```python
class SudokuDataset(Dataset):
    def __init__(self, data, labels) -> None:

        self.data = data
        self.labels = labels
        super().__init__()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        # may want to encode the labels right here
        # inheriting the label encoder and just doing the transform
        # # Be warned as the label encoder is usually for dataframes
        # # but here we are moreso worried about 
        label = self.data[index].astype('int32')
        data = self.data[index].astype('float32')

        return data, label
```


--- 
## Start Training

### Dependent On
- ~~Fix Data Reading~~ 

### Notes
- Most likely need to modify training function to work with pre-encoded labels. 
- In the future I would also like to implement a trainer class that inherits from the dataset class. 
- I'm 99% sure <mark>pytorch has its own trainer class</mark>, so using that might be more effective for learning and efficiency. 
- I'm unsure if using the pytorch trainer class is the best option. May get more versatility and readability with a simple custom class.
- I think we go back to only having 9 features

#### Original Training Function
```python
def train(dataloader, model, loss_fn, optimizer, batch_print=100, device='cuda'):

    size = len(dataloader.dataset)
    model.train()

    for batch, (X, y) in enumerate(dataloader):
        optimizer.zero_grad()
        X, y = X.to(device), y.to(device)
        y = y - 1 # accounting for index 0

        pred = model(X)
        pred = pred.view(-1, 81, 9) # reshape to [batch,81,9]

        loss = loss_fn(pred.permute(0, 2, 1), y) # Permute to [batch,9,81]
        loss.backward()
        optimizer.step()

        if batch % batch_print == 0:
            loss, current = loss.item(), (batch+1) * len(X)
            print(f'loss: {loss:>7f} [{current:<5d}/{size:>5d}]')
```

#### Proposed Fixes
1. I don't think we really need the size listed here, waste o' memory
2. Remove the y alterations
3. The Data should be pre-reshaped to (batch, 10, 81)
    - This allows us to keep 0 in there. It should learn pretty quick that 0 is never the right answer. 
        - This may result in problems when training as it adds an extra n parameters
4. The reshaping question
    - Three options
        1. No reshaping at all in training
            - Best possible option
            - ~~Labels should be preshaped and predictions should be reshaped as part of their forward function~~
                - I get an extra dimension doing this in the \_\_getitem\_\_ attribute (batch,1,81,n_features). <mark>Calling it in the forward method with how we have to concat the dummy numbers is the problem.<mark/>  
                - <mark> If we could encode variables without the dummy numbers this would work.<mark/>

        2. Encode the labels as a part of the training function.
            - Decreases reusability of the training function which is suboptimal
            - It does confirmed work
            - Limits batch size as encoding the labels is EXPENSIVE

        3. Make a lazy encode method so I can just pre-encode all of this. *
            - Encode in batches and store as like an int16


#### Potential Issues
I really really really don't want to encode these as part of the training function

#### Current Training Function (In Progress)
This is more of a placeholder for me to try and figure out how to write these the best
```
{< readfile file="/home/alex/coding-projects/sudoku/hello_world.py" >}
```

---