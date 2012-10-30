

def _patch_canonicals_cleanup():
    from plone.multilingual.storage import CanonicalStorage
    from plone.app.uuid.utils import uuidToObject   

    if getattr(CanonicalStorage, '__wcc_canonical_cleanup_patch', False):
        return

    _orig_get_canonicals = CanonicalStorage.get_canonicals
    def get_canonicals(self):
        canonicals = _orig_get_canonicals(self)
        for c in canonicals:
            obj = uuidToObject(c)
            if obj is None:
                self.remove_canonical(c)
        return _orig_get_canonicals(self)
    CanonicalStorage.get_canonicals = get_canonicals
    CanonicalStorage.__wcc_canonical_cleanup_patch = True

_patch_canonicals_cleanup()
