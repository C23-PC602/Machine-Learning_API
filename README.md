# Model Machine Learning
## Detection Coffee Bean

## APIs
| Endpoint       | Method |           Body Sent (JSON)          |                 Type                       |                 Description                |
|:--------------:|:------:|:-----------------------------------:|:------------------------------------------:|:------------------------------------------:|
|     /          |   GET  |                 None                |                 None                       |    Check Connection EndPoint               |
|     /predict   |  POST  | {     "file : Coffee.jpg        }   | Mutli-platform ("jpg, "JPG", "jpeg", "png")|  Return detection kematangan buah kopi     |

Checkout all our pre-trained model through [this](https://drive.google.com/file/d/1L3zBe8W1mKXgjFLN3ZwsJz3rHOJ7YtN4/view?usp=sharing)

## Install your local

- `git clone https://github.com/C23-PC602/Machine-Learning_API.git`
- `cd Machine-Learning_API`
- open your terminal type this command `pip install -r requirement.txt`
- to run this program `python main.py` type in your terminal.
- access [localhost:8080](http://localhost:8080/)

To acces detection coffee feature access endpoint this [localhost:8080/docs](http://localhost:8080/docs)

### The result

```
  {
  "result": "Matang" || "Setengah Matang" || "Mentah"
  }
```
