
class ModelBase:

    def __init__(self, 
                name = None, 
                version = 0, 
                description = None, 
                more_info = None):
        self.name = name
        self.version = version
        self.description = description
        self.more_info = more_info

    def predict(self): 
        raise NotImplementedError
    
    def preprocess(self): 
        raise NotImplementedError

    def postprocess(self): 
        raise NotImplementedError

    def getBasicInfo(self):
        return dict(
            model_name = self.name,
            version = self.version,
            description = self.description,
            more_info = self.more_info
        )

