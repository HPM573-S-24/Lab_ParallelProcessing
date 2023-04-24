import deampy.plots.histogram as hist
import deampy.plots.sample_paths as path

import EconEvalInputData as D
import ProbabilisticSupport as Support
import ProbilisticParamClasses as P
from ParallelClasses import ParallelMultiCohort

POP_SIZE = 1000             # cohort population size
N_COHORTS = 100              # number of cohorts
therapy = P.Therapies.MONO  # selected therapy


if __name__ == '__main__':  # this line is needed to avoid errors that occur on Windows computers

    # create multiple cohort
    multiCohort = ParallelMultiCohort(
        ids=range(N_COHORTS),
        pop_size=POP_SIZE,
        therapy=therapy)

    # simulate multiple cohorts
    multiCohort.simulate(sim_length=D.SIM_LENGTH)

    # plot the sample paths
    path.plot_sample_paths(
        sample_paths=multiCohort.multiCohortOutcomes.survivalCurves,
        title='Survival Curves',
        x_label='Time-Step (Year)',
        y_label='Number Survived',
        transparency=0.5)

    # plot the histogram of average survival time
    hist.plot_histogram(
        data=multiCohort.multiCohortOutcomes.meanSurvivalTimes,
        title='Histograms of Mean Survival Time',
        x_label='Survival Time (year)',
        bin_width=0.5,
        x_range=[5, 20])

    # print the outcomes of this simulated cohort
    Support.print_outcomes(multi_cohort_outcomes=multiCohort.multiCohortOutcomes,
                           therapy_name=therapy)
