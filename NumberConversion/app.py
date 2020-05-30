from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        forms = request.form['forms']
        if forms == "form1":
            inputBinary = request.form['binaryNum'][::-1]

            result2 = binary_to_dec(inputBinary)
            return render_template('index.html', decimalAnswer=result2)

        elif forms == "form2":
            inputDecimal = request.form['decimalNum']
            result1 = dec_to_bin(inputDecimal)
            return render_template('index.html', binaryAnswer=result1)

    else:
        return render_template('index.html')


def binary_to_dec(binaryNumber):

    result = 0
    a = 0
    for b in binaryNumber:

        result += 2**a
        a += 1
    return result


def dec_to_bin(decimalNumber):
    result = ''
    decimalNumber = int(decimalNumber)

    while decimalNumber > 0:
        num = decimalNumber % 2

        result = result + str(num)
        decimalNumber //= 2

    result = result[::-1]

    return result


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
