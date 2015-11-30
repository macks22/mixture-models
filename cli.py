"""
Command line interface (CLI) parser functions.

"""
import logging
import argparse


def data_gen_parser(parser):
    """Add arguments specific to synthetic data generators."""
    parser.add_argument(
        '-spc', '--samples-per-comp',
        type=int, default=100,
        help='number of data samples to generate from each component')


def gibbs_parser(parser):
    """Add arguments specific to gibbs samplers."""
    parser.add_argument(
        '-ns', '--nsamples',
        type=int, default=100,
        help='number of Gibbs samples to draw'
             '; default 100')
    parser.add_argument(
        '-b', '--burnin',
        type=int, default=10,
        help='number of Gibbs samples to discard before storing the rest'
             '; default 10')
    parser.add_argument(
        '-ts', '--thin-step',
        type=int, default=2,
        help='step-size for thinning; default is 2, which means every other '
             'sample will be kept')


def make_parser(description):
    parser = argparse.ArgumentParser(
        description=description)
    parser.add_argument(
        '-v', '--verbose',
        type=int, default=1,
        help='adjust verbosity of logging output')
    parser.add_argument(
        '-im', '--init-method',
        choices=('kmeans', 'random', 'load'), default='kmeans',
        help='initialization method for gmm; defaults to kmeans')
    parser.add_argument(
        '-K', type=int, default=2,
        help='initial guess for number of components')

    data_gen_parser(parser)  # add synthetic data generation arguments
    gibbs_parser(parser)     # add gibbs sampler arguments
    return parser


def parse_args(description):
    parser = make_parser(description)
    args = parser.parse_args()

    # Setup logging.
    logging.basicConfig(
        level=(logging.DEBUG if args.verbose == 2 else
               logging.INFO if args.verbose == 1 else
               logging.ERROR),
        format="[%(asctime)s]: %(message)s")

    return args
