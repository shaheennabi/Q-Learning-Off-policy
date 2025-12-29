from train import  train_qlearning
from config import EPSILON, GAMMA, ALPHA



def main():
    train = train_qlearning(1, 10, 10, 4, EPSILON, GAMMA, ALPHA)
    print(train.q_values)
    print(train.q_values.shape)    ## just to know the shape.


if __name__ == "__main__":
    main()