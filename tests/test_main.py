from MLOPS_AGH_LAB1_BSTEPNIEWSKI.config import Settings
import os

def test_envs_loading():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "mlops_agh_lab1_bstepniewski"
