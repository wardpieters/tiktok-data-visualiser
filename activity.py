import pandas
import plotly.graph_objects as go

def process_file(file_name):
    data_by_day = {}
    with open(file_name) as shared_videos:
        for line in shared_videos:
            line_data = line.split(" ")
            if len(line_data) == 3 and line_data[0] == "Date:":
                date = line_data[1]
                if date not in data_by_day:
                    data_by_day[date] = 1
                else:
                    data_by_day[date] += 1
    return data_by_day


video_history_by_day = process_file("Video Browsing.txt")
shared_videos_by_day = process_file("Sharing.txt")

labels = pandas.date_range(list(video_history_by_day)[-1], list(shared_videos_by_day)[0], freq='d')
labels = labels.format(formatter=lambda x: x.strftime('%Y-%m-%d'))

video_history_data = list(video_history_by_day.values())[::-1]
shared_videos_data = []

for x in labels:
    if x in shared_videos_by_day:
        shared_videos_data.append(shared_videos_by_day[x])
    else:
        shared_videos_data.append(0)

print(labels)
print(video_history_data)
print(shared_videos_data)

fig = go.Figure(data=[
    go.Bar(name='Watched videos', x=labels, y=video_history_data),
    go.Bar(name='Shared videos', x=labels, y=list(shared_videos_by_day.values())[::-1])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()
