def reformat_essay(input_essay):
    # Replace single quotes with double quotes
    formatted_essay = input_essay.replace("'", '"')

    # Remove newline characters and concatenate into a single line
    formatted_essay = formatted_essay.replace('\n', ' ')

    return formatted_essay

# Example usage:
if __name__ == "__main__":
    essay_input = """
        #Insert your essay here
    """
    question = "Describe an event you looked forward to which turned out to be disappointing. Explain why you were excited and why it did not live up to your expectations."


    formatted_essay = reformat_essay(essay_input)
    print("Question: {}. Answer: {}".format(question,formatted_essay))
