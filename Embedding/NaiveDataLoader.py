

class NaiveDataLoader:
    def __init__(self, dataset, batch_size=64, collate_fn=default_collate):
        self.dataset = dataset
        self.batch_size = batch_size
        self.collate_fn = collate_fn
        self.index = 0
        
      
def __iter__(self):
        self.index = 0
        return self 
    
    
def __next__(self):
        if self.index >= len(self.dataset):
            # stop iteration once index is out of bounds
            raise StopIteration
        batch_size = min(len(self.dataset) - self.index, self.batch_size)
        return self.collate_fn([self.get() for _ in range(batch_size)])  
    
    
def get(self):
        item = self.dataset[self.index]
        self.index += 1
        return item
    

dataset = list(range(16))  

print(dataset)
                 