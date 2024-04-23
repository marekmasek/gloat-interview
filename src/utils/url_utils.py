class UrlUtils:

    @staticmethod
    def get_complete_url(base_url: str, path_or_url: str) -> str:
        return path_or_url if UrlUtils.is_full_url(path_or_url) else base_url + UrlUtils.normalize_path(path_or_url)

    @staticmethod
    def is_full_url(path_or_url: str) -> bool:
        schemes = ['http://', 'https://']  # we don't need other schemes in selenium and requests
        for scheme in schemes:
            if path_or_url.startswith(scheme):
                return True
        return False

    @staticmethod
    def normalize_path(path: str) -> str:
        if not path.startswith('/'):
            return '/' + path
        return path
