import os

import click

from .big_earth_net import big_earth_net


@click.group()
@click.option("--tf-log-level", type=click.Choice(["0", "1", "2", "3"]), default="2")
def main(tf_log_level):
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = tf_log_level


main.add_command(big_earth_net)

if __name__ == "__main__":
    main()
