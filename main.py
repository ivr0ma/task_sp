import os
import matplotlib.pyplot as plt
data_name = 'data'  # папка с набором данных
screen_name = 'view_hierarchies'

current_path = str(os.getcwd())  # текущий путь
data_path = os.path.join(current_path, data_name)  # путь к набору данных
list_app = os.listdir(data_path)  # список приложений
print("number of applications in the dataset:", len(list_app))

trace_count = {}  # частотный словарь
trace_len = {}  # словарь длин трасс
trace_all_count = 0  # количество трасс в датасете
for app in list_app:
    app_path = os.path.join(data_path, app)
    traces = os.listdir(app_path)  # список трасс
    for trace in traces:  # подсчет трасс
        if trace in trace_count:
            trace_count[trace] += 1
        else:
            trace_count[trace] = 1

        trace_path = os.path.join(app_path, trace)
        screen_path = os.path.join(trace_path, screen_name)
        screens = os.listdir(screen_path)  # список скринов

        len_screen = len(screens)//2
        if len_screen in trace_len:
            trace_len[len_screen] += 1
        else:
            trace_len[len_screen] = 1

    trace_all_count += len(traces)

print("number of traces in the dataset:", trace_all_count)
print("traces:", trace_count)

# выводим гистограмму длин трасс
index_trace = []
values_trace = []
for len_screen in trace_len:
    index_trace.append(len_screen)
    values_trace.append(trace_len[len_screen])

plt.title('histogram of trace lengths')
plt.bar(index_trace, values_trace)
plt.show()