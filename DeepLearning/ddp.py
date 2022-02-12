import os
import numpy as np
import tensorflow as tf

class OUActionNoise(object):
    def __init__(self, mu, sigma=0.15, theta=0.2, dt=le-2,x0=None):
        self,theta = theta
        self.mu = mu
        self.dt = dt
        self.sigma= sigma
        self.x0= x0
        self.reset()
        
    def __call__(self):
        x = self.x_prev + self.theta*(self.mu-self.x_prev)*self.dt + self.sigma*np.sqrt(self.dt)*np.random.normal(size=self.mu.shape)
        self.x_prev=x
        return x
    
    def reset(self):
        self.x_prev = self.x0 if self.x0 is not None else np.zeros_like(self.mu)
        
        
class ReplayBuffer(object):
    def __init__(self, max_size, input_shape, n_actions):
        self.meme_size = max_size
        self.meme_cntr = 0
        self.state_memory = np.zeros((self.meme_size, *input_shape))
                
