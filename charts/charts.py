import matplotlib.pyplot as pylot

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax =pylot.subplots()
    ax.pie(values, labels=labels)
    pylot.savefig('chart_pie_final.png')
    pylot.close()

if __name__ == '__main__':
    labels = ['a','b','c']
    values = [10,40,800]
    generate_pie_chart(labels,values)
    