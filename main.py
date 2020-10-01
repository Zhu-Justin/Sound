#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Justin Zhu
# CLI Tool for creating dependency graphs
import os
import argparse
import sound

argparser = argparse.ArgumentParser(description='Get Sound Recording')

sound.main()


# argparser.add_argument('filename', metavar='path', type=str, help='the path to file')
# argparser.add_argument("-f", "--functions",
#                        action="store_true", help="view function mapping for provided file")
# argparser.add_argument("-F", "--functionsall", action="store_true", help="view all function mappings")
# argparser.add_argument("-l", "--libraries", action="store_true", help="view dependency mapping of libraries")
# argparser.add_argument("-r", "--raw", action="store_true", help="view graphs as a list")

# args = argparser.parse_args()
# homedirectory, filename = os.path.split(args.filename)

# if len(homedirectory) > 1 and homedirectory[0:2] == './':
#     homedirectory = homedirectory.replace('.', os.getcwd(), 1)

# package = filename.split('.')[0]
# if args.libraries:
#     libraries = sc.recurse(homedirectory, filename, '', package)
#     print(libraries)
# if args.functions:
#     functions = sc.getfunctions(homedirectory, filename, '')
#     print(functions)

# graphs = sc.getgraph(homedirectory, filename, '', package, nopretty=args.raw,
#                      allfunctions=args.functionsall)
# if args.raw:
#     print(graphs)



