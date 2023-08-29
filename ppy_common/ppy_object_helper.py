class ObjectHelper:

    @staticmethod
    def copy_config_property(source, destination):
        if source and destination:
            config_map = dir(source)
            for key in config_map:
                if key.isupper() and hasattr(destination, key):
                    setattr(destination, key, getattr(source, key))
        return destination
