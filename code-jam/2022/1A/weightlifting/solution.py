# WRONG ANSWER

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    nof_exe, nof_weights = map(int, input().split())
    weigths_per_exe = [list(map(int, input().split())) for _ in range(nof_exe)]

    nof_ops = 0
    stack = []
    for i in range(nof_exe):
        state = [0] * nof_weights

        # TODO: compare this cost with the one of reshaping the stack to
        #       accomodate next exercise

        # Find layers to drop & Update last layer to keep
        drop_from_layer = 0
        to_keep = True
        while to_keep and drop_from_layer < len(stack):
            layer = stack[drop_from_layer]
            for w in range(nof_weights):
                if weigths_per_exe[i][w] < state[w] + layer[w]:
                    to_keep = False
                    # Increase ops of #weights to remove by the last layer to keep
                    nof_ops += state[w] + layer[w] - weigths_per_exe[i][w]
                    # Update last layer to keep
                    layer[w] = weigths_per_exe[i][w] - state[w]
                state[w] += layer[w]
            drop_from_layer += 1

        # Increase ops of #weights to remove
        nof_ops += sum(map(sum, stack[drop_from_layer:]))
        # Drop layers from the stack
        stack = stack[:drop_from_layer]
        # Increase ops of #new weights
        nof_ops += sum(weigths_per_exe[i]) - sum(state)

        # Add new layer of weights to the stack
        new_layer = [0] * nof_weights
        for w in range(nof_weights):
            new_layer[w] = weigths_per_exe[i][w] - state[w]
        stack.append(new_layer)

    # Summarize stack in a single state
    state = map(sum, zip(*stack))
    # Free stack of weights
    nof_ops += sum(state)

    print("Case #{}: {}".format(test, nof_ops))