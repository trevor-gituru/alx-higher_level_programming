#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names_lists = dir(hidden_4)
    for name in names_lists:
        if name[0:2] != "__":
            print(name)
