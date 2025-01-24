from controllers.task_controller import run

if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")