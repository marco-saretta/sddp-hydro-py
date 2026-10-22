from hydra import compose, initialize


def test_config_composes():
    with initialize(version_base="1.3", config_path="../configs"):
        cfg = compose(config_name="config", overrides=["case=real_4area"])
    assert cfg.case.name == "real_4area"
    assert cfg.sddp.n_stages > 0
