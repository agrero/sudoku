# I think these should all 
# become their own classes 
# or a method in the dataloader

def train(dataloader, model, loss_fn, optimizer, device='cuda'):

    model.train()

    for batch, (X, y) in enumerate(dataloader):
        optimizer.zero_grad()
        X, y = X.to(device), y.to(device)

        pred = model(X)
        loss = loss_fn(pred, y) 

        loss.backward()
        optimizer.step()

        loss, current = loss.item(), (batch+1) * len(X)
        print(f'loss: {loss:>7f} [{current:<5d}/{len(dataloader.dataset):>5d}]')