


from collections import defaultdict

FILE_NAME = 'transcript_example.txt'
NEXT_CLASSES = 'ICS_next.json'


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
    return classes

    transcript.close()

def get_next_classes(classes):
    global next_classes
    
    possible = set()
    current_classes = set()
    for c in classes:
        if c['department'] == 'I&C SCI':
            current_classes.add(c['number'])
            if c['number'] in next_classes:
                possible = possible.union(set(next_classes[c['number']]))

    prereqs = defaultdict(set)
    
    for k, v in next_classes.items():
        same = possible.intersection(set(v))
        for c in same:
            prereqs[c].add(k)
    can_take = set()
    for k, v in prereqs.items():
        done = v.difference(current_classes)
        if len(done) == 0:
            can_take.add(k)
            
    print('\n', can_take)
    return can_take
    
    
        

if __name__ == '__main__':
    classes = run_parser()
    global next_classes
    classes_file = open(NEXT_CLASSES, 'r')
    next_classes = eval(''.join(classes_file.readlines()))
    classes_file.close()
    #print('\n', next_classes)
    get_next_classes(classes)
