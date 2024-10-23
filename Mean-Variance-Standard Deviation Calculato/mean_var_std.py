import numpy as np


def calculate(list):
    calculations = {}
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.array(list).reshape(3,3)
    #mean
    mean_all = np.mean(matrix)
    mean_columns = np.mean(matrix,axis = 0)
    mean_rows = np.mean(matrix,axis = 1)
    calculations['mean'] = [mean_columns.tolist(),mean_rows.tolist(), mean_all]
    #var
    var_all = np.var(matrix)
    var_columns = np.var(matrix, axis = 0)
    var_rows = np.var(matrix,axis =1)
    calculations['variance']=[var_columns.tolist(),var_rows.tolist(),var_all]
    #standart deviation
    sd_all = np.std(matrix)
    sd_columns = np.std(matrix, axis = 0)
    sd_rows = np.std(matrix,axis =1)
    calculations['standard deviation']=[sd_columns.tolist(),sd_rows.tolist(),sd_all]
    #max
    max_all = np.max(matrix)
    max_columns = np.max(matrix, axis = 0)
    max_rows = np.max(matrix,axis =1)
    calculations['max']=[max_columns.tolist(),max_rows.tolist(),max_all]
    #min
    min_all = np.min(matrix)
    min_columns = np.min(matrix, axis = 0)
    min_rows = np.min(matrix,axis =1)
    calculations['min']=[ min_columns.tolist(),min_rows.tolist(),min_all]
    #sum
    sum_all = np.sum(matrix)
    sum_columns = np.sum(matrix, axis = 0)
    sum_rows = np.sum(matrix,axis =1)
    calculations['sum']=[sum_columns.tolist(),sum_rows.tolist(),sum_all]

    return calculations
