from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset when the app starts
df = pd.read_csv('Indian_Engineering_Colleges_Dataset.csv')

# Define route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract user input for College Name and State
        college_name = request.form['College_Name']
        state = request.form['State']
        
        # Filter dataset based on College Name and State with case-insensitive partial matching
        filtered_colleges = df[(df['College_Name'].str.contains(college_name, case=False, na=False)) & 
                               (df['State'].str.contains(state, case=False, na=False))]
        
        # Convert filtered data to a list of dictionaries to pass to the template
        colleges_list = filtered_colleges.to_dict(orient='records')
        
        # User search input data
        user_data = {
            "College_Name": college_name,
            "State": state
        }

        # If no colleges match, return an empty list
        if not colleges_list:
            message = "No colleges found matching your criteria."
            return render_template('Result.html', colleges=colleges_list, user=user_data, message=message)

        # Render the results page with matching colleges
        return render_template('Result.html', colleges=colleges_list, user=user_data)

    # Render the search form when the page is first loaded
    return render_template('Index.html')

if __name__ == '__main__':
    app.run(debug=True)
