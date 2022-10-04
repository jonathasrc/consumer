
from dynaconf import Dynaconf 

settings = Dynaconf(
    envvar_prefix="CONSUMER",
    settings_files=['settings.toml', '.secrets.toml'],

)

# m`envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
