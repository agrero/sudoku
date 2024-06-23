# I think these should all 
# become their own classes 
# or a method in the dataloader

def train(dataloader, model, loss_fn, optimizer, batch_print=100, device='cuda'):
    size = len(dataloader.dataset)
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        optimizer.zero_grad()
        X, y = X.to(device), y.to(device)

        pred = model(X)
        pred = pred.view(-1, 81, 9) # reshape to [batch, 81, 9]

        loss = loss_fn(pred.permute(0, 2, 1), y) # Permute to [batch, 9, 81]
        loss.backward()
        optimizer.step()

        if batch % batch_print == 0:
            loss, current = loss.item(), (batch+1) * len(X)
            print(f'loss: {loss:>7f} [{current:<5d}/{size:>5d}]')