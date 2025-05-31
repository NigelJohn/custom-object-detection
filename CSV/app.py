from flask import Flask
from flask import render_template_string
from flask import request
from flask import redirect
import csv

#web app instance
app = Flask('__name__')

#Adding the object
@app.route('/addObj', methods=['GET','POST'])
def addObj():
    #GET method
    if request.method == 'GET':
        return render_template_string("""
            <html>
                <head>
                    <!--Bootstrap CDN-->
                    <link rel = "stylesheet" href = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css">
                </head>
                <header>
                    <nav class="navbar navbar-expand-lg bg-body-tertiary" style='padding-top: 0; padding-bottom:0'>
                        <div class="container-fluid bg-dark bg-gradient">
                            <a class="navbar-brand text-white" href="/">i.Detect</a>
                        </div>
                    </nav>
                </header>
                <body class = 'bg-dark'>
                    <div class = 'container mt-5 d-flex align-items-center justify-content-center'>
                        <form class="row g-3" style = 'width: 70%' method='POST'>
                            <h1 class='text-white' style='padding-bottom: 2%'>Object Information</h1>
                            <h7 class='text-danger' style='padding-bottom: 1%'>*Note: If information not available, please type 'NA'</h7>
                            <div class="col-12">
                                <label for="inputObject" class="form-label text-white"><strong>Enter Object Name:</strong></label>
                                <input type="text" class="form-control" name="inputObject" placeholder="Eg: Microcontroller" required>
                            </div>  
                            <div class="col-md-6">
                                <label for="inputAisle" class="form-label text-white"><strong>Enter Aisle Number:</strong></label>
                                <input type="text" class="form-control" name="inputAisle" placeholder="Eg: B12" required>
                            </div>
                            <div class="col-md-6">
                                <label for="inputShelf" class="form-label text-white"><strong>Enter Shelf Number:</strong></label>
                                <input type="text" class="form-control" name="inputShelf" placeholder="Eg: 13" required>
                            </div>      
                            <div class="col-md-6">
                                <label for="inputQuant" class="form-label text-white"><strong>Enter Quantity:</strong></label>
                                <input type="text" class="form-control" name="inputQuant" placeholder="Eg: 43" required>
                            </div>   
                            <div class="col-md-6">
                                <label for="inputCat" class="form-label text-white"><strong>Select Category:</strong></label>
                                <select class="form-select" aria-label="Default select example" name="inputCat" required>
                                    <option selected>Select Category...</option>
                                    <option value="Consumer">Consumer</option>
                                    <option value="Health">Health</option>
                                    <option value="Proprietay">Proprietary</option>
                                    <option value="Spare part">Spare part</option>
                                    <option value="Electrical">Electrical</option>
                                    <option value="Other">Other</option>
                                </select>
                            </div>   
                            
                            <!--Submit Button-->
                            <div class="col-md-6 mt-4">
                                <input type='submit' class='btn btn-success' value='Submit' style='padding: 3%; font-size: 20px'/>
                            </div>       
                        </form
                </body>
            </html>
        """)
    
    #POST method
    elif request.method == 'POST':
        #extracting new data from form
        data = dict(request.form)
        
        #update CSV file
        with open('data.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())
            writer.writerow(data)

        # return str(data)
        return redirect('/')

# read data from csv
@app.route('/')
def read():
    data = []

    with open('data.csv') as f:
        reader = csv.DictReader(f)

        #looping over CS by rows
        for row in reader:
            data.append(dict(row))


    #render HTML page dynamically
    return render_template_string("""
        <html>
            <head>
                <!--Bootstrap CDN-->
                <link rel = "stylesheet" href = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css">
            </head>
            <header>
                <nav class="navbar navbar-expand-lg bg-body-tertiary" style='padding-top: 0; padding-bottom:0'>
                    <div class="container-fluid bg-dark bg-gradient">
                        <a class="navbar-brand text-white" href="/">i.Detect</a>
                    </div>
                </nav>
            </header>
            <body>
                <div class = 'container'>
                <!--CSV data-->
                    <table class="table table-hover table-dark table-boredered border-danger" style = 'width: 100%; border: 4px solid red; margin-top: 3%'>
                        <thead>
                            <tr>
                                {% for header in data[0].keys() %}
                                    <th scope="col">
                                        {%  if header == list(data[0].keys())[0] %}
                                            <a class = 'btn btn-primary' href='/addObj'>+</a>
                                        {% endif %}    
                                        {{header}}
                                    </th>
                                {% endfor %}
                            </tr>
                        </thead>
                        <tbody class = 'table-group-divider' style = 'border-top-color: red'>
                            {% for row in range(0, len(data)) %}
                                <tr id="{{row}}">
                                    {% for col in range(0, len(list(data[row].values()))) %}
                                        <td style = 'word-break:break-all'>
                                            {% if col == 0 %} 
                                                <a class="btn btn-success" style="margin-left: 2%" href="/update?id={{row}}">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pen" viewBox="0 0 16 16">
                                                        <path d="m13.498.795.149-.149a1.207 1.207 0 1 1 1.707 1.708l-.149.148a1.5 1.5 0 0 1-.059 2.059L4.854 14.854a.5.5 0 0 1-.233.131l-4 1a.5.5 0 0 1-.606-.606l1-4a.5.5 0 0 1 .131-.232l9.642-9.642a.5.5 0 0 0-.642.056L6.854 4.854a.5.5 0 1 1-.708-.708L9.44.854A1.5 1.5 0 0 1 11.5.796a1.5 1.5 0 0 1 1.998-.001zm-.644.766a.5.5 0 0 0-.707 0L1.95 11.756l-.764 3.057 3.057-.764L14.44 3.854a.5.5 0 0 0 0-.708l-1.585-1.585z"/>
                                                    </svg>
                                                </a>
                                                <a class="btn btn-danger" style="margin-left: 2%; margin-right: 2%" href="/delete?id={{row}}">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                                                        <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                                                        <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                                                    </svg>
                                                </a>
                                            {% endif %}
                                            {{ list(data[row].values())[col]}}
                                        </td>
                                    {% endfor %}
                                </tr>
                            {% endfor %}
                        </tbody>
                    </table>
            </body>
        </html>
    """, data = data, list=list, len=len)

# edit the object info
@app.route('/update', methods = ['GET', 'POST'])
def update():
    #GET method
    if request.method == 'GET':
        # updated data
        data = []
        # fields = json.loads(request.args.get('fields').replace("'", '"'))
        with open('data.csv') as uf:
            # create CSV dict reader
            reader = csv.DictReader(uf)

            #init CSV rows
            [data.append(dict(row)) for row in reader]

            # return to home page
            return render_template_string('''
            <html>
                <head>
                    <!-- Bootstrap CDN -->
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css"/>
                </head>
                <header>
                    <nav class="navbar navbar-expand-lg bg-body-tertiary" style='padding-top: 0; padding-bottom:0'>
                        <div class="container-fluid bg-dark bg-gradient">
                            <a class="navbar-brand text-white" href="/">i.Detect</a>
                        </div>
                    </nav>
                </header>
                <body class = 'bg-dark'>
                    {{data}}
                    <div class="container mt-5 d-flex align-items-center justify-content-center">
                        <form class="row g-3" style = 'width: 70%' method='POST'>
                            <h1 class='text-white' style='padding-bottom: 2%'>Update Object Information</h1>
                            <h7 class='text-danger' style='padding-bottom: 1%'>*Note: If information not available, please type 'NA'</h7>
                            <div class="col mt-2" hidden>
                                <div class="row mx-auto" style="width: 300px">
                                    <input name="Id" type="text" class="form-control" value="{{request.args.get('id')}}">
                                </div>
                            </div>
                            {% for key, val in fields.items() %}
                                <div class="col mt-2">
                                    <div class="row mx-auto" style="width: 300px">
                                        <input name="{{key}}" type="text" class="form-control" value="{{val}}">
                                    </div>
                                </div>
                            {% endfor %}
                            
                            <!--Submit Button-->
                            <div class="col-md-6 mt-4">
                                <input type='submit' class='btn btn-success mt-5' value='Submit' style='padding: 3%; font-size: 20px; margin-left: -10%'/>
                            </div>  
                        </form>
                    </div>
                </body>
              </html>
            ''', fields=data[int(request.args.get('id'))])

    # POST method
    elif request.method == 'POST':
        # updated data
        data = []
        
        # open CSV file
        with open('data.csv') as rf:
            # create CSV dictionary reader
            reader = csv.DictReader(rf)
            
            # init CSV rows
            [data.append(dict(row)) for row in reader]
        
        # updated row
        row = {}
        
        for key, val in dict(request.form).items():
            if key != 'Id':
                row[key] = val
        
        # update CSV row
        data[int(request.form.get('Id'))] = row
        
        # write update CSV file
        with open('data.csv', 'w') as wf:
            # create CSV dictionary writer
            writer = csv.DictWriter(wf, fieldnames=data[0].keys())
            
            # write CSV column names
            writer.writeheader()
            
            # write CSV rows
            writer.writerows(data)

        return redirect('/')

        
# delete the object
@app.route('/delete')
def delete():
    # Open CSV file 
    with open('data.csv') as rf:
        # updated data
        data=[]
        
        # load data
        temp_data=[]

        # create CSV dict reader
        reader = csv.DictReader(rf)

        #loop over CSV rows
        [temp_data.append(dict(row)) for row in reader]

        # create new dataet without row to delete
        [data.append(temp_data[row]) for row in range(0, len(temp_data)) if row != int(request.args.get('id'))]

        #update the csv file
        with open('data.csv', 'w') as wf:
            # create CSV dict writer
            writer = csv.DictWriter(wf, fieldnames=data[0].keys())

            #write CSV col names
            writer.writeheader()

            # write CSV rows
            writer.writerows(data)

    return redirect('/')

# run HTTP server
if __name__ == '__main__':
    app.run(debug=True, threaded = True)