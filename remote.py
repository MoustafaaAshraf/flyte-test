from main import workflow_tefa
from flytekit.configuration import Config, ImageConfig
from flytekit.remote import FlyteRemote

config = Config.auto(config_file="config-sandbox.yaml")

remote = FlyteRemote(
    config=config,
    default_project="flytesnacks",
    default_domain="development",
)

img_cfg = ImageConfig.auto(config_file=None, img_name="moustafa-test:latest")

remote.register_workflow(
    workflow_tefa,
    version="latest",
)

execution = remote.execute(
    entity=workflow_tefa,
    inputs={"name": "Moustafa"},
    project="flytesnacks",
    domain="development",
    name="workflow_tefa",
    version="latest",
    image_config=img_cfg,
    wait=True,
)

print(f"👉  Monitor your run at: {remote.generate_console_url(execution)}")
