from ..core.base import IsauraBase


class Reader(IsauraBase):

    def __init__(self, model_id):
        IsauraBase.__init__(self, model_id=model_id)

    def read_by_idx(self, api_name, idxs):
        pass

    def read_by_key(self, api_name)
        pass
