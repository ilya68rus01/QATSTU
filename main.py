import sys
from FlaskService import flask_server
from DialogService.DeepPavlovWrapper import DeepPavlovWrapper
#wrapper = DeepPavlovWrapper()
#print(wrapper.get_answer_on_question("В каком году образован ТГТУ?"))

def main():
    flask_server.start()


if __name__ == '__main__':
    sys.exit(main())

