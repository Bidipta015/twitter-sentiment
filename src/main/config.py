class Config:
    def __init__(self, config):
        self.bearer_token: str = config.get('bearer-token')
        self.access_token: str = config.get('access-token')
        self.access_token_secret: str = config.get('access-token-secret')
        self.api_key: str = config.get('api-key')
        self.api_key_secret: str = config.get('api-key-secret')

    @classmethod
    def from_file(cls, file_path):
        config = cls._initialize(file_path)
        return cls(config)

    @staticmethod
    def _initialize(conf_file_path):
        config = Config._parse_config_file(conf_file_path)
        return config

    @staticmethod
    def _parse_config_file(file_path):
        config = {}
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line by '='
                key_value = line.strip().split('=')
                if len(key_value) == 2:
                    # Extract key and value
                    key = key_value[0].strip()
                    value = key_value[1].strip().strip("'")
                    config[key] = value
        return config
