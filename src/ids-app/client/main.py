from flow import UI
from dashboard import Dashboard

# Define a UI object.
# Define a Dashboard object.


def main():
    ui = UI()
    db = Dashboard(ui.df)


if __name__ == '__main__':
    main()
