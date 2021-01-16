import numpy as np

def activate(x):
  # for example sigmoid
  return 1 / (1+np.exp(-x))

def deriv_act_fun(x):
  fx = activation_fun(x)
  return fx*(1-fx)

def mse_loss(y_true, y_pred):
  return ((y_true-y_pred)**2).mean()

class NN:
  def __init__(self):
    
    # initial weights : suppose we have 2 entry points and 1 hidden layer of 2 units
    self.w1 = np.random.normal()
    self.w2 = np.random.normal()
    self.w3 = np.random.normal()
    self.w4 = np.random.normal()
    self.w5 = np.random.normal()
    self.w6 = np.random.normal()
    
    self.b1 = np.random.normal()
    self.b2 = np.random.normal()
    self.b3 = np.random.normal()

  def feedforward(self,x):
    u1 = activate(self.w1*x[0]+self.w2*x[1]+self.b1)
    u2 = activate(self.w3*x[0]+self.w4*x[1]+self.b2)
    out = activate(self.w5*u1+self.w6*u2+self.b3)
    return out

  def train(self, data, all_y_trues):
    epochs = 1000 
    learn_rate = 0.1
    
    for epoch in range(epochs):
      for x, y_true in zip(data, all_y_trues):
          sum_u1 = self.w1*x[0] + self.w2*x[1] + self.b1
          u1 = activate(sum_u1)
          sum_u2 = self.w3*x[0] + self.w4*x[1] + self.b2
          u2 = activate(sum_u2)
          sum_out = self.w5*u1 + self.w6*u2 + self.b3
          out = activate(sum_out)
          y_pred = out

          #calculate derivatives
          #d_L_d_w1 : deriv L / deriv w1"
          d_L_d_ypred = -2*(y_true - y_pred)

          #out
          d_ypred_d_w5 = u1*deriv_act_fun(sum_out)
          d_ypred_d_w6 = u2*deriv_act_fun(sum_out)
          d_ypred_d_b3 = deriv_act_fun(sum_out)

          d_ypred_d_u1 = self.w5*deriv_act_fun(sum_out)
          d_ypred_d_u2 = self.w6*deriv_act_fun(sum_out)

          #u1
          d_u1_d_w1 = x[0] * deriv_act_fun(sum_u1)
          d_u1_d_w2 = x[1] * deriv_act_fun(sum_u1)
          d_u1_d_b1 = deriv_act_fun(sum_u1)

          #u2
          d_u2_d_w3 = x[0] * deriv_sigmoid(sum_u2)
          d_u2_d_w4 = x[1] * deriv_sigmoid(sum_u2)
          d_u2_d_b2 = deriv_act_fun(sum_u2)

          # update weights & biases
          #u1
          self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_u1 * d_u1_d_w1
          self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_u1 * d_u1_d_w2
          self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_u1 * d_u1_d_b1

          #u2
          self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
          self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
          self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2

          #out
          self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
          self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
          self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3

        # total loss at the end of the epoch
        if epoch % 10 == 0:
            y_preds = np.apply_along_axis(self.feedforward, 1, data)
            loss = mse_loss(all_y_trues, y_preds)
            print("Epoch %d loss: %.3f" % (epoch, loss))

#dataset
data = np.array(<listofdata>)
all_y_trues = np.array([listoftargetsvalues])
#train
network = NN()
network.train(data, all_y_trues)
# test
entryex=[1,2,3]
print("%.3f" % network.feedforward(entryex))

    
  
