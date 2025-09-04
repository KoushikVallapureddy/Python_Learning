class FileManager:
    def read_file(self, filename):
        return f"Reading {filename}"

    def _check_permissions(self, filename):
        return f"Checking permissions for {filename}"

    def __decrypt_content(self, content):
        return f"Decrypted: {content}"

    def get_file_content(self, filename):
        self._check_permissions(filename)
        content = f"Content of {filename}"
        return self.__decrypt_content(content)