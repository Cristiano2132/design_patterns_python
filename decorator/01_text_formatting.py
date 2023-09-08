class IText:
    def render(self):
        pass

class PlainText(IText):
    def __init__(self, content: str):
        self.content = content

    def render(self):
        return self.content

class TextDecorator(IText):
    def __init__(self, wrapped: IText):
        self.wrapped = wrapped

    def render(self):
        return self.wrapped.render()

class BoldDecorator(TextDecorator):
    def render(self):
        return "<b>" + super().render() + "</b>"


if __name__=="__main__":
    text = PlainText("Hello, World!")
    print(text.render())  # Output: 'Hello, World!'
    formatted_text = BoldDecorator(text)
    print(formatted_text.render())  # Output: <b>Hello, World!</b>
