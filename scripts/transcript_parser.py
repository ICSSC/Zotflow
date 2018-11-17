




FILE_NAME = 'transcript_example.txt'



def run_parser() -> None:
    transcript = open(FILE_NAME, 'r')

    classes = []
    for line in transcript.readlines():
        line_text = line.strip().split('\t')
        if len(line_text) == 6:
            try:
                line_text[3] = float(line_text[3])
            except:
                continue
            class_dict = {}
            class_dict['department'] = line_text[1]
            class_dict['number'] = line_text[2]
            classes.append(class_dict)
    print(classes)
        

    transcript.close()


if __name__ == '__main__':
    run_parser()
