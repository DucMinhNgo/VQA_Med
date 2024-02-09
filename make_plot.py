import json
import matplotlib.pyplot as plt
import ast
import config
import re

def make_plot(history, epoch_max, path_output_chd, type_plot='loss'):
    train = history['train']
    valid = history['valid']
    fig, ax = plt.subplots()
    epochs = range(epoch_max)
    
    
    if type_plot=='loss':
        plt.plot(epochs, train, '-r', lw=2, label='Training loss')
        plt.plot(epochs, valid, '-b',lw=2, label='validation loss')
        plt.legend(borderaxespad=0.)
        plt.title('Training and Validation loss')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.savefig(path_output_chd+'/imgs/loss.png')
        
    elif type_plot == 'acc1':
    
        plt.plot(epochs, train, '-r', lw = 2, label='Training Top 1 Accuracy')
        plt.plot(epochs, valid, '-b', lw = 2, label='validation Top 1 Accuracy')
        plt.legend(borderaxespad=0.)
        plt.title('Training and Validation Top 1 Accuracy')
        plt.xlabel('Epochs')
        plt.ylabel('Top 1 Accuracy')
        plt.savefig(path_output_chd+'/imgs/acc1.png')

    elif type_plot == 'acc5':
    
        plt.plot(epochs, train, '-r', lw = 2, label='Training Top 5 Accuracy')
        plt.plot(epochs, valid, '-b', lw = 2, label='validation Top 5 Accuracy')
        plt.legend(borderaxespad=0.)
        plt.title('Training and Validation Top 5 Accuracy')
        plt.xlabel('Epochs')
        plt.ylabel('Top 5 Accuracy')
        plt.savefig(path_output_chd+'/imgs/acc5.png')
    else:
        plt.plot(epochs, train, '-r', lw = 2, label='Training blue')
        plt.plot(epochs, valid, '-b', lw = 2, label='validation blue')
        plt.legend(borderaxespad=0.)
        plt.title('Training and Validation blue')
        plt.xlabel('Epochs')
        plt.ylabel('Blue')
        plt.savefig(path_output_chd+'/imgs/blue.png')

    
    
    plt.show()

opt = config.parse_opt()
num_epochs = opt.NUM_EPOCHS
input_dir = config.path_output_chd
input_dir = "answer_classes.json"

# Reading from a text file
with open("loss_output.txt", "r") as file:
    data_read = file.read()
    loss_dict = ast.literal_eval(data_read)
    print (loss_dict['train'])
    make_plot(loss_dict, num_epochs, input_dir, type_plot='loss')

with open("acc_output.txt", "r") as file:
    data_read = file.read()
    print (data_read)
    pattern = r'\d+\.\d+'

    # Find all floating-point numbers in the string
    numbers = re.findall(pattern, data_read)
    print (numbers)