Check our link for its demo: https://www.youtube.com/watch?v=V6C7_id_mLk&lc=z23cfjraloe2evhg104t1aokg0ryiw4oendkx1tvkqpsrk0h00410
...

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has four major parts :
1. model.py - This contains code fot our Machine Learning model to predict employee salaries absed on trainign data in 'hiring.csv' file.
2. app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
3. templates - This folder contains the HTML template to allow user to enter  details and displays the prediction part.

### Running the project in windows os:
** First of all go to cmd prompt and enter the working location of our project.
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

You should be able to view the homepage as below :
![alt text](https://github.com/Shreyaansh-darkside/Crop-yielding-Estimator/blob/master/Sample.jpg)

Enter valid numerical values in all 2 input boxes and hit Predict.

If everything goes well, you should  be able to see the predcited days value on the HTML page!

```

