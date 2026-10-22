"""Entry point: compose the Hydra config and run SDDP.

Examples:
    uv run python main.py
    uv run python main.py case=real_4area sddp.max_iterations=10
    uv run python main.py -m sddp.n_scenarios=10,20
"""

import logging

import hydra
from omegaconf import DictConfig, OmegaConf

log = logging.getLogger(__name__)


@hydra.main(version_base="1.3", config_path="configs", config_name="config")
def main(cfg: DictConfig) -> None:
    log.info("Config:\n%s", OmegaConf.to_yaml(cfg))
    # TODO: load case -> train SDDP -> simulate -> save results
    # case = load_case(cfg.case.data_dir, areas=cfg.case.areas)
    # strategy = train(case, **cfg.sddp)
    # results = simulate(case, strategy, **cfg.simulation)


if __name__ == "__main__":
    main()
