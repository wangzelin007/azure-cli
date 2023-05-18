#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

azdev_test_result_dir = os.path.expanduser("~/.azdev/env_config/mnt/vss/_work/1/s/env")


def save_pipeline_result():
    # save pipeline result to file
    # /mnt/vss/.azdev/env_config/mnt/vss/_work/1/s/env/breaking_change_test.json
    filename = os.path.join(azdev_test_result_dir, f'breaking_change_test.json')
    from shutil import copyfile
    copyfile('./scripts/ci/breaking_change_test.json', filename)


def main():
    save_pipeline_result()


if __name__ == '__main__':
    main()