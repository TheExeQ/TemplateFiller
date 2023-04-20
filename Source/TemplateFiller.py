# Open the file for reading
with open('input.txt', 'r') as file:
    # Read the file contents
    file_contents = file.read()

    # Find all occurrences of text enclosed in square brackets
    texts_in_brackets = []
    start = 0
    while True:
        start = file_contents.find('[', start)
        if start == -1:
            break
        end = file_contents.find(']', start)
        if end == -1:
            break
        texts_in_brackets.append(file_contents[start+1:end])
        start = end + 1

    # Filter out duplicate texts
    unique_texts_in_brackets = list(set(texts_in_brackets))

    # Prompt the user for input for each unique element
    user_inputs = []
    for text in unique_texts_in_brackets:
        user_input = input(f"Enter input for [{text}]: ")
        user_inputs.append(user_input)

    # Replace the brackets and text with user input
    for i in range(len(unique_texts_in_brackets)):
        old_text = f'[{unique_texts_in_brackets[i]}]'
        new_text = user_inputs[i]
        file_contents = file_contents.replace(old_text, new_text)

    # Write the updated contents back to the file
    with open('output.txt', 'w') as file:
        file.write(file_contents)

    print("File has been updated with user input.")
