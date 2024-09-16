#test/<subpage>
def serve(**kwargs):
    output = ""
    for k, v in kwargs.items():
        output += f"{k}: {v}\n"
    return output

