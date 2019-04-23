from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def show_main_page():

    text = request.form.get('studentText')

    print(text) #выводит текст ученика

    numberclass = request.form.get('studentClass')

    print(numberclass)  # выводит класс ученика

    return render_template('index.html', studentText=text, studentClass=numberclass)


@app.route('/result', methods=['POST', 'GET'])
def show_result():

    list = ["арифметич.дії з дробами", "арифметичний квадратний корінь, його властивості", "квадратне рівняння",
            "числові нерівності", "квадратична фунція", "арифметична і геометричная прогресії"]

    theme = list[4]

    return render_template('page2.html', result=theme)


if __name__ == '__main__':
    app.run()
