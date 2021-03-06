from bs4 import BeautifulSoup
import copy
import re


def get_sentences(fname, file):
    print("dataset :", fname)
    content = open(fname, "r", encoding="utf-8").read()
    content = re.sub(r"<fs.*>", "<fs/>", content)

    sp = BeautifulSoup(content, "html.parser")

    [sss.extract() for sss in sp("fs")]
    p = 0
    p_total = len(sp.find_all("sentence"))
    for ss in sp.find_all("sentence"):
        x = "".join(ss.findAll(text=True))
        x = re.sub(r"\t", "", x)
        x = re.sub(r"[A-Za-z]|_|\)\)\n|\(\(|[0-9]+\.[0-9]+", "", x)
        x = re.split(r"[0-9]+\n", x)
        for i in range(len(x)):
            x[i] = re.sub(r"[0-9]", "", x[i])
            x[i] = re.split("\n", x[i])[0:-1]

        temp_sentences = [""]
        for i in range(len(x)):
            t = x[i]
            if len(t) == 0:
                t = [""]
            if t[0] == ".":
                break
            # print(t[0])
            temp_sentences2 = copy.deepcopy(temp_sentences)
            temp_sentences = []
            for j in range(len(t)):
                new_word = t[j]
                if new_word != ",":
                    new_word = new_word.replace(",", "")
                    new_word = new_word.replace(".", "")
                    for k in range(len(temp_sentences2)):
                        if new_word != "":
                            ns = temp_sentences2[k] + new_word + " "
                        else:
                            ns = temp_sentences2[k]
                        temp_sentences.append(ns)
        # print(temp_sentences)
        txt = "\n".join(temp_sentences)
        txt = "\n" + txt
        file.write(txt)
        p += 1
        print("Progress ", p/p_total)
    return


data_sets = 1
sets = [i+1 for i in range(data_sets)]

for i in sets:
    # Change i here
    f = open("dataset %d.txt" % 16, "a+", encoding="utf-8")
    # get_sentences("data (%d).txt" % i, f)
    get_sentences("testing2", f)