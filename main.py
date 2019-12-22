from stegano import lsb

if __name__ == '__main__':
    image_location = './data/stegosaurus.jpg'
    secret = lsb.hide(image_location, "سلام")
    secret.save("./data/Lenna-secret.png")
    clear_message = lsb.reveal("./data/Lenna-secret.png")
    assert 1 == 1