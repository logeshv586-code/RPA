from app.product import PRODUCT_NAME, PRODUCT_VERSION, product_manifest


def test_product_manifest_has_single_product_identity():
    manifest = product_manifest()

    assert manifest["name"] == PRODUCT_NAME == "RPA-X"
    assert manifest["version"] == PRODUCT_VERSION
    assert len(manifest["capabilities"]) >= 8


def test_product_manifest_distinguishes_planned_capabilities():
    manifest = product_manifest()
    statuses = {capability["status"] for capability in manifest["capabilities"]}

    assert "foundation" in statuses
    assert "planned" in statuses
