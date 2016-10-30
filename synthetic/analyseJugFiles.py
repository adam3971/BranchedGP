import jug
import jug.task
from matplotlib import pyplot as plt
import numpy as np
import jugGPSamples
from BranchedGP import VBHelperFunctions as v

if __name__ == "__main__":
    jug.init('jugGPSamples.py', 'jugGPSamples.jugdata')
    resultsFull = jug.task.value(jugGPSamples.runsFull)
    resultsSparse = jug.task.value(jugGPSamples.runsSpar)
    rall = [resultsFull, resultsSparse]
    rallDescr = ['Full', 'Sparse']
    plt.close('all')
    plt.ion()
    for ir, res in enumerate(rall):
        for r in res:
            '''{'errorInBranchingPt': errorInBranchingPt,
              'logLikelihoodRatio': logLikelihoodRatio,
              'Btry': Btry, 'BgridSearch': BgridSearch,
              'mlist': mlist, 'timingInfo': timingInfo} '''
            mlist = r['mlist']
            for ml in mlist:
                # Experiment for given B, we have one fit per search grid B
                ''' {'trueBStr': bs, 'bTrue': bTrue,
                      'pt': m.t, 'Y': m.Y.value, 'mlocallist': mlocallist}) '''
                print('trueB', ml['trueB'])
                mlocall = ml['mlocallist']
                for mlocal in mlocall:
                    ''' {'candidateB': b, 'obj': obj[ib], 'Phi': Phi,
                               'ttestl': ttestl, 'mul': mul, 'varl': varl} '''
                    v.plotBranchModel(mlocal['candidateB'], ml['pt'], ml['Y'],
                                      mlocal['ttestl'], mlocal['mul'], mlocal['varl'],
                                      mlocal['Phi'], fPlotPhi=True, fPlotVar=True)
                    plt.title('%s TrueB=%s b=%g NLL=%f' % (rallDescr[ir], ml['trueB'],
                                                           mlocal['candidateB'], mlocal['obj']))