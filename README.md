**# Regresspy**

**Name: Md. Azharul Islam**

 **ID: 181-35-2329**

- First od all i have Fork this repository in the regresspy main file.
- Then I had had cloned this repo in my desktop from the pycharm terminal.
- Then i changed the directory of regresspy.
- Then i input my mail address and username from my github id.
- Then create a new branch of this repo
- Git add . using this command and all the file added in this branch on the other hand I left a comment and finally git push of  this branch.
- **Now i changed my project portion** 
1. I took first of all **loss.py** file and created some function as like mse, sse, mae and rmse and finally run this file from pycharm terminal.
2. Then i go to my gradient descent file and change the **forward function** and run this function from pycharm terminal.
3. Then i changed the **test_loss.py** file and make some functions (test_mase, test_rmse, test_sse) here my course teacher 
already created **test_mae** function so it easy for me to create another 3 function and finally i check those function from terminal and using same values.
4. Then i go to **regression.py** file.

4.1-First of all i set weight and bios in predict function and return prediction.

4.2-Then i need to score all the (mse, rmse, mae, sse) function using if, else from the **score function** and return the score.

4.3-Actually i change self weight and bios but in the **initialize_weights** function but my course teacher already did it.

4.4-And finally i i change the **train** function using **forward** and **backward** function from the gradient descent file.

4.5-Using forward propagation (forward function) i got loss and print it.

5. Then finally i go to **model.py** file.

5.1-At first i changed the reshape in Y predict portion. I got error and again i set the reshape and run successfully.

5.2-I Used the stochastic gradient descent regressor and set iteration 100.

5.3-I trained X, Y through fit function from regression file of the stochastic gradient descent.

5.4-I predict stochastic gradient descent through predict function from regression.py file.

5.5-I calculated stochastic gradient descent rmse through rmse function from loss.py file.

5.6-And finally i got stochastic gradient descent rmse value, where the value is 0.5974190098240547
#################################################################################################

5.7-I evaluated regression value through regression function from regression.py file and set epoch/iteration 100 and also learning rate was 0.0001.

5.8-I trained X, Y through fit function from regression file of the regression value.

5.9-I predict regression value through predict function from regression.py file.

5.10-I calculated score of regression rmse through score function from regression.py file.

5.11-And finally i got RMSE value, where the value is 1.2447250539684422

- Then i created the **requirement.txt** file that which the libraries actually needed of this project.
- And i try to use a command to get all the requirement library (pip freeze > requirements.txt) but actually i got all libraries which was used to another project. hahaha
- Finally i made **setup.py** file which was import setup and find_namespace_packages
- In setup function i mentioned project name, author, mail address, version, description, long description, my github link, all packages and requirement libraries.
- And i run this **setup.py** file on my cmd for the test. 
- Finally add all the files in my branch on github using (git add .), left comment was "All the files "updated" using (git commit - m "") this command and push all files.