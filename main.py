import os
import matplotlib.pyplot as plt
data_name = 'data'  # папка с набором данных

current_path = str(os.getcwd())  # текущий путь
data_path = os.path.join(current_path, data_name)  # путь к набору данных
list_app = os.listdir(data_path)  # список приложений
print("number of applications in the dataset:", len(list_app))

trace_count = {}  # частотный словарь
trace_all_count = 0  # количество трасс в датасете
for app in list_app:
    traces = os.listdir(os.path.join(data_path, app))  # список трасс
    for trace in traces:  # подсчет трасс
        if trace in trace_count:
            trace_count[trace] += 1
        else:
            trace_count[trace] = 1

    trace_all_count += len(traces)

print("number of traces in the dataset:", trace_all_count)

# выводим гистограмму кол-ва трасс
index_trace = []
values_trace = []
for trace in trace_count:
    index_trace.append(trace)
    values_trace.append(trace_count[trace])

plt.bar(index_trace, values_trace)
plt.show()