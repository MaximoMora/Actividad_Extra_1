#    lista = [random.randint(1, 100) for _ in range(100)]
#    print("Original list:", lista)
#    history = CuckTailSort(lista)

    fig, ax = plt.subplots()

    for i, step in enumerate(history):
        colors = ['red' if j == len(
            step) - 2 or j == len(step) - 1 else 'lime' for j in range(len(step))]
        ax.bar(np.arange(len(step)), step, color=colors)
        ax.set_title(f'Step {i + 1}')
        plt.pause(0.01)

    plt.show()
