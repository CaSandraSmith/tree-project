import random
import re
from avltree import AvlTree, AvlTreeNode

class MarkovChain:
    def __init__(self, file_name):
        self.tree = AvlTree()
        self.corpus = self.proccess_corpus(file_name)
        
        self.sort_corpus()
    
    def proccess_corpus(self, file_name):
        '''
        load_corpus() function handles loading the file, reading its lines,
        and creating an array from the lines.
        '''
        # open the file
        infile = open(file_name, 'r')

        # read and store the lines from the file in a variable
        lines = infile.read()
        
        # close file
        infile.close()
        
        return lines.split()

    
    def sort_corpus(self):
        i = 0
        
        while i < len(self.corpus) - 1:
            current_word = self.corpus[i]
            next_word = self.corpus[i + 1]

            self.tree.insert(current_word, next_word)
            
            i = i + 1
            
    def walk_chain(self, length=10):
        random_start_word = random.choice(self.corpus)
        current_word = self.tree.search(random_start_word).word
                
        sentence = [current_word]
        
        while len(sentence) <= length:
            current_node = self.tree.search(current_word)
            if not current_node or not current_node.next_words:
                break
            current_word = random.choice(current_node.next_words)
            sentence.append(current_word)

        sentence[0] = sentence[0].capitalize()
        formatted_sentence = " ".join(sentence)
        formatted_sentence = re.sub(r"[^a-zA-Z' ]", '', formatted_sentence)
            
        return formatted_sentence + "."
        
            

def main():
    prideMarkov = MarkovChain("data/pride_and_prejudice.txt")
    print(prideMarkov.walk_chain())
    
if __name__ == '__main__':
    main()