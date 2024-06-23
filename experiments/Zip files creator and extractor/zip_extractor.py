import zipfile


def archive_extractor(archivePath, dest_dir):
    with zipfile.ZipFile(archivePath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    archive_extractor("compressed.zip", r"C:\Users\supra\PycharmProjects\App1\experiments\dest")



