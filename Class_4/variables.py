def outer(y):
    def answer(y):
        print("'y' exists before assigning" if 'y' in locals() else "'y' does not exist before assigning")
        y = 12
        print("'y' exists after assigning" if 'y' in locals() else "'y' does not exist after assigning")
        return y
    answer(y)
    return "Done!"

print("'y' exists before the function" if 'y' in locals() else "'y' does not exist before the function")

print(outer(10))