
import wikipedia


def main():
    title = input("Enter title or phrase: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title)
            summary = wikipedia.summary(title)
            print("Title: {}\nSummary: {}\nURL: {}".format(page.title, summary, page.url))
        except wikipedia.DisambiguationError as e:
            print(e.options)
        title = input("Enter title or phrase: ").strip()


if __name__ == '__main__':
    main()