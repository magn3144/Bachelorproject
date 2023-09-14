class element_type:
    def __init__(self, description, htmls, xpaths):
        self.description = description
        if len(htmls) == 1:
            self.quantity = "Single Element"
        if len(htmls) > 1:
            self.quantity = "Multiple Elements"
        self.html = htmls
        self.xpath = xpaths

    def __str__(self):
        examples_text = ""
        for i in range(len(self.html)):
            examples_text += f"HTML: {self.html[i]} | X-path: {self.xpath[i]}\n"
        return f"""Description of element: {self.description}
Quantity: {self.quantity}
Examples of these elements (HTML and X-path for each element):
{examples_text}"""