# -*- coding: utf-8 -*-

import sys
from platform_core.integration.platform_bootstrap import PlatformBootstrap


def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print("python run.py <topic>")
        return

    topic = " ".join(sys.argv[1:])

    print("=" * 70)
    print("AR-Vet AI Writer")
    print("=" * 70)
    print("Topic :", topic)
    print()

    platform = PlatformBootstrap()

    article = platform.generate(topic)

    print("DONE")
    print(article)


if __name__ == "__main__":
    main()
