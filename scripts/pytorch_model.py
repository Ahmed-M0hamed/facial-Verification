import torch 
from torch import nn 

class L1Dist(nn.Module):
    
    def __init__(self, **kwargs):
        super().__init__()
       
    # Magic happens here - similarity calculation
    def forward(self, input_embedding, validation_embedding):
        return torch.abs(input_embedding - validation_embedding)
    
class embedding(nn.Module) : 
    def __init__(self ) : 
        super().__init__()
        self.b1 =  nn.Sequential(nn.Conv2d(3 , 64 , (10 ,10 ) ) 
                               , nn.ReLU()
                               ,nn.MaxPool2d((2,2)) )
        self.b2 =  nn.Sequential(nn.Conv2d(64 , 128 , (7 ,7 ) ) 
                               , nn.ReLU()
                               ,nn.MaxPool2d((2,2)) )
        self.b3 =  nn.Sequential(nn.Conv2d(128 , 128 , (4 ,4 ) ) 
                               , nn.ReLU()
                               ,nn.MaxPool2d((2,2)) )
        
        self.b4 = nn.Sequential(nn.Conv2d(128 , 256 , (4 ,4 ) ) 
                               , nn.ReLU()
                               ,nn.Flatten() )
        
        self.out = nn.Linear(6400 , 4096) 
        self.s = nn.Sigmoid()
        
    def forward(self , x) : 
        x = self.b1(x)
        x = self.b2(x)
        x = self.b3(x)
        x = self.b4(x)
        x = self.s(self.out(x))
        return x 

class Model(nn.Module): 
    def __init__(self) : 
        super().__init__()
        self.embedding  = embedding()
        self.distance = L1Dist()
        self.out = nn.Linear(4096 , 1)
        self.s = nn.Sigmoid()
    def forward(self , x_1 , x_2)  : 
        return self.s(self.out(self.distance(self.embedding(x_1) , self.embedding(x_2))))
        
        