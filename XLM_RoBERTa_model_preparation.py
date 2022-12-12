#!/usr/bin/env python
# coding: utf-8

# In[43]:


#import global_vars
import XLM_RoBERTA_model_execution
#from XLM_RoBERTA_model_execution import *
import os


# In[41]:


model_savedir_buttons = 'V:/Uni/Thesis/Code/Thesis/buttons_model'
model_savedir_dialog = 'V:/Uni/Thesis/Code/Thesis/dialogue_model'
#classification_buttons_filename = 'V:/Uni/Thesis/Code/Thesis/Classification file for buttons.csv'
classification_buttons_filename = 'V:/Uni/Thesis/Code/Thesis/Classification file for buttons.txt'

classification_dialog_filename = 'V:/Uni/Thesis/Code/Thesis/Classification file for cookie dialog.csv'


# In[18]:


print('1: Cookie dialog model')
print('2: Buttons model model')
choice = int(input('Which model would you like to train? '))
choice_runs = int(input('How many runs do you want to do? '))


# In[45]:


if choice == 1:
    number_of_runs = choice_runs
    classification_filename = classification_dialog_filename
    model_savedir = model_savedir_dialog
    model_type = "cookie dialog"
elif choice == 2:
    number_of_runs = choice_runs
    classification_filename = classification_buttons_filename
    model_savedir = model_savedir_buttons
    model_type = "buttons"

XLM_RoBERTA_model_execution.main(number_of_runs, classification_filename, model_savedir, model_type)


# In[37]:


os.remove(model_savedir + '0')

