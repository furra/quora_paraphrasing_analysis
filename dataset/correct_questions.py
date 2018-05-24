#corrects question ids in original file
#TODO: read original file and change it to tab separated file
#      delete evil characters, i.e., invisible
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python3 {} <original_file> <new_file>'.format(sys.argv[0]))
        sys.exit()

    #newfile = 'questions_corrected.tsv'
    #originalfile = 'questions_bkp.tsv'
    originalfile = sys.argv[1]
    newfile = sys.argv[2]

    try:
        line2correction = {} #line id to corrected line
        questions = {}
        outfile = open(newfile, 'w')
        with open(originalfile) as infile: #original file
            first_line = infile.readline() #skip header line
            outfile.write(first_line)
            for line in infile:
                pline = line.lower().strip()
                try:
                    pair_id, qid1, qid2, question1, question2, label = pline.split('\t')
                except ValueError:
                    print("error:\n",pline)
                    break

                if question1 not in questions:
                    questions[question1] = qid1
                else:
                    qid1 = questions[question1]
                    
                if question2 not in questions:
                    questions[question2] = qid2
                else:
                    qid2 = questions[question2]

                outfile.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(pair_id, qid1, qid2, question1, question2, label))
        outfile.close()
    except FileNotFoundError:
        print('Original file not found!')
        sys.exit()

