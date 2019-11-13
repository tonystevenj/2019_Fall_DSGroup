# -*- coding: utf-8 -*-
from . import server
from .scripts import load
from .models.data.business import Business


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Assistant for Restaurant Site Selection')
    parser.add_argument('run_type', default='run',
                        help='run: run webserver, pre: pretreatment')
    args = parser.parse_args()
    if args.run_type == 'run':
        business = Business()
        total = business.load(loadData=True)
        print('{} items loaded'.format(total))
        server.run()
    elif args.run_type == 'init':
        business = Business()
        total = business.load(loadGEO=True)
        print('{} items loaded'.format(total))
