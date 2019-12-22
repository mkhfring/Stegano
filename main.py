from stegano import lsb

if __name__ == '__main__':
    image_location = './data/1.jpg'
    secret = lsb.hide(image_location, "سلام")
    secret.save("test.png")
    clear_message = lsb.reveal("./test.png")
    print(clear_message)

    assert 1 == 1