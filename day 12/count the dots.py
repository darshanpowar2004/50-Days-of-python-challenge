def count_dots(text):
    return text.count(".")

if __name__ == "__main__":
    text1 = "h.e.l.p."
    print(f"for {text1} : {count_dots(text1)}")

    text2 = "he.lp."
    print(f"for {text2} : {count_dots(text2)}")