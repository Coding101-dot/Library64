def number_of_words(filename):
    try:
        with open(filename) as fn:
            contents = fn.read()

    except FileNotFoundError:
        print("Sorry,unable to locate " + filename)

    else:
        words = contents.split()
        num_o_words = len(words)

        print("The number of words in the selected files" + filename + " are " + str(num_o_words))
